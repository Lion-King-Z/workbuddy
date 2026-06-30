#!/usr/bin/env python3
"""
Batch upload 2026-06-25 output files to IMA 聚宝盆.
Uses Node.js scripts from ima-skill.
"""
import json, subprocess, os, sys, time

SKILL_DIR = "C:/Users/Administrator/.workbuddy/skills/ima-skill"
KB_ID = "9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g="
OPTS = json.dumps({
    "clientId": open(os.path.expanduser("~/.config/ima/client_id")).read().strip(),
    "apiKey": open(os.path.expanduser("~/.config/ima/api_key")).read().strip()
})

# ── Upload jobs: (local_path, target_folder_id, description) ──
JOBS = [
    ("G:/锅师/深度研究/0622-0628/2026-06-25_每日信息推送.md",
     "folder_7474808711298069", "深度研究/0622-0628"),
    ("G:/锅师/深度研究/0622-0628/2026-06-25_窄门筛股_v4.1.md",
     "folder_7474808711298069", "深度研究/0622-0628"),
    ("G:/锅师/浑水调研/0622-0628/2026-06-25_紧缺度日报.md",
     "folder_7474808711308297", "浑水调研/0622-0628"),
    ("G:/锅师/浑水调研/浑水跟踪_2026-06.md",
     "folder_7471884757106786", "浑水调研/根"),
    ("G:/锅师/浑水调研/紧缺度追踪总表.md",
     "folder_7471884757106786", "浑水调研/根"),
]

def run_api(api_path, body):
    """Execute ima_api.cjs and return parsed JSON response."""
    cmd = [
        "node.exe", f"{SKILL_DIR}/ima_api.cjs", api_path,
        json.dumps(body), OPTS
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, shell=True, cwd=SKILL_DIR)
    if r.returncode != 0:
        err = r.stderr.strip()
        if err:
            try:
                return json.loads(err), True  # (data, is_error)
            except json.JSONDecodeError:
                return {"msg": err}, True
    # stdout is response JSON
    try:
        resp = json.loads(r.stdout.strip())
        return resp, resp.get("code", -1) != 0
    except json.JSONDecodeError:
        return {"msg": f"stdout: {r.stdout[:200]}"}, True

def upload_file(file_path, target_folder, desc):
    """Upload a single file using the standard 5-step IMA upload flow."""
    fname = os.path.basename(file_path)
    print(f"\n{'='*60}")
    print(f"📤 [{desc}] 上传: {fname}")
    print(f"{'='*60}")

    # Step 0: Check file exists
    if not os.path.exists(file_path):
        print(f"  ❌ 文件不存在: {file_path}")
        return False
    fsize = os.path.getsize(file_path)
    print(f"  ✅ 文件大小: {fsize} bytes")

    # Step 1: Preflight check
    print(f"  🔍 Preflight...", end=" ", flush=True)
    r = subprocess.run(
        ["node.exe", f"{SKILL_DIR}/knowledge-base/scripts/preflight-check.cjs", "--file", file_path],
        capture_output=True, text=True, shell=True
    )
    if r.returncode != 0:
        print(f"❌ failed: {r.stderr[:200]}")
        return False
    preflight = json.loads(r.stdout.strip())
    file_ext = preflight["file_ext"]
    media_type = preflight["media_type"]
    content_type = preflight["content_type"]
    print(f"✅ (ext={file_ext}, type={media_type}, ct={content_type})")

    # Step 2: Check repeated names
    print(f"  🔍 查重...", end=" ", flush=True)
    resp, err = run_api("openapi/wiki/v1/check_repeated_names", {
        "params": [{"name": fname, "media_type": media_type}],
        "knowledge_base_id": KB_ID,
        "folder_id": target_folder
    })
    if not err and resp.get("data", {}).get("is_repeated"):
        existing = resp["data"].get("repeated_names_info", [])
        print(f"⚠️ 重名: {[e.get('name','?') for e in existing]}")
        print(f"  → 追加时间戳重新上传")
        # Append timestamp to avoid collision
        ts = time.strftime("%Y%m%d%H%M%S")
        base, ext = os.path.splitext(fname)
        fname_dup = f"{base}_{ts}{ext}"

        # Retry with new name
        resp2, err2 = run_api("openapi/wiki/v1/check_repeated_names", {
            "params": [{"name": fname_dup, "media_type": media_type}],
            "knowledge_base_id": KB_ID,
            "folder_id": target_folder
        })
        if err2:
            print(f"  ⚠️ 查重失败 (继续): {resp2.get('msg','')}")
        elif resp2.get("data", {}).get("is_repeated"):
            print(f"  ⚠️ 时间戳名也重复，跳过：{fname_dup}")
            return False
        fname = fname_dup  # use dedup name
        print(f"  → 使用重命名: {fname}")
    else:
        print(f"✅ 无重名")

    # Step 3: Create media
    print(f"  📝 Create media...", end=" ", flush=True)
    resp, err = run_api("openapi/wiki/v1/create_media", {
        "file_name": fname,
        "file_size": fsize,
        "content_type": content_type,
        "knowledge_base_id": KB_ID,
        "file_ext": file_ext
    })
    if err:
        print(f"❌ failed: {resp.get('msg','unknown')}")
        return False
    media_id = resp["data"]["media_id"]
    cred = resp["data"]["cos_credential"]
    cos_info = resp["data"].get("cos_info", {})

    # Determine bucket and cos_key (handle API version differences)
    # bucket_name already includes appid suffix (e.g., "ima-share-kb-1258344701")
    bucket = cred.get("bucket_name") or cred.get("bucket", "")

    # cos_key from either cos_info or cos_credential (API version dependent)
    cos_key = cos_info.get("cos_key") or cred.get("cos_key", "") or media_id.replace("markdown_", "") + ".md"
    region = cred.get("region", "ap-shanghai")
    secret_id = cred.get("tmp_secret_id") or cred.get("secret_id")
    secret_key = cred.get("tmp_secret_key") or cred.get("secret_key")
    token = cred.get("token") or cred.get("session_token", "")
    start_time = cred.get("start_time", "0")
    expired_time = cred.get("expired_time", "0")

    print(f"✅ (media_id={media_id[:20]}...)")

    # Step 4: COS upload
    print(f"  ☁️  COS上传...", end=" ", flush=True)
    cos_args = [
        "node.exe", f"{SKILL_DIR}/knowledge-base/scripts/cos-upload.cjs",
        "--file", file_path,
        "--secret-id", secret_id,
        "--secret-key", secret_key,
        "--token", token,
        "--bucket", bucket,
        "--region", region,
        "--cos-key", cos_key,
        "--content-type", content_type,
        "--start-time", start_time,
        "--expired-time", expired_time,
        "--timeout", "300000"
    ]
    r = subprocess.run(cos_args, capture_output=True, text=True, shell=True)
    if r.returncode != 0:
        print(f"❌ failed: {r.stderr[:200]}")
        return False
    print(f"✅")

    # Step 5: Add knowledge
    print(f"  📚 Add knowledge...", end=" ", flush=True)
    resp, err = run_api("openapi/wiki/v1/add_knowledge", {
        "media_type": media_type,
        "media_id": media_id,
        "title": fname,
        "knowledge_base_id": KB_ID,
        "folder_id": target_folder,
        "file_info": {
            "cos_key": cos_key,
            "file_size": fsize,
            "file_name": fname
        }
    })
    if err:
        print(f"❌ failed: {resp.get('msg','unknown')}")
        return False
    print(f"✅ SUCCESS!")

    print(f"  ✅ [{desc}] {fname} → IMA 完成")
    return True

# ── Main: execute all upload jobs ──
success = 0
fail = 0
for fp, fid, desc in JOBS:
    ok = upload_file(fp, fid, desc)
    if ok:
        success += 1
    else:
        fail += 1

print(f"\n{'='*60}")
print(f"📊 上传完成: ✅ {success} 成功 / ❌ {fail} 失败")
print(f"{'='*60}")
if fail > 0:
    sys.exit(1)

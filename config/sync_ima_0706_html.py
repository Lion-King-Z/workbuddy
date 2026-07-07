"""Upload missing HTML files for week 0706-0712 to IMA聚宝盆.

IMA API rejects local HTML via preflight (web must be URL). Fallback: upload as
media_type=7 (markdown-type file) — same approach already used for the 2 HTML
files already present in 深度研究/0706-0712.
"""
import json, subprocess, os

KB_ID = "9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g="
SKILL_DIR = "C:/Users/Administrator/.workbuddy/skills/ima-skill"
TARGET = "folder_7479461721159006"  # 深度研究/0706-0712

FILES = [
    "G:/锅师/深度研究/0706-0712/2026-07-07_每日窄门筛股.html",
    "G:/锅师/深度研究/0706-0712/2026-07-07_半导体材料六剑客深度评估.html",
]


def api(method, payload):
    cmd = ["node", f"{SKILL_DIR}/ima_api.cjs", f"openapi/wiki/v1/{method}", json.dumps(payload)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    out = r.stdout.strip()
    start = out.find('{')
    return json.loads(out[start:])


for filepath in FILES:
    if not os.path.exists(filepath):
        print(f"❌ 不存在: {filepath}")
        continue
    FNAME = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    print(f"\n🌐 {FNAME} (as media_type=7)")

    # check_repeated_names
    resp = api("check_repeated_names", {
        "params": [{"name": FNAME, "media_type": 7}],
        "knowledge_base_id": KB_ID, "folder_id": TARGET})
    is_rep = resp.get("data", {}).get("results", [{}])[0].get("is_repeated", False)
    if is_rep:
        print("  ⚠️ 已存在同名，跳过")
        continue

    # create_media
    resp = api("create_media", {
        "file_name": FNAME, "file_size": filesize, "content_type": "text/html",
        "knowledge_base_id": KB_ID, "file_ext": "html"})
    if resp.get("code", 0) != 0:
        print(f"  ❌ create_media失败: {resp.get('msg', '')}")
        continue
    media_id = resp["data"]["media_id"]
    cred = resp["data"]["cos_credential"]

    # cos upload
    cos = subprocess.run([
        "node", f"{SKILL_DIR}/knowledge-base/scripts/cos-upload.cjs",
        "--file", filepath, "--secret-id", cred["secret_id"], "--secret-key", cred["secret_key"],
        "--token", cred["token"], "--bucket", cred["bucket_name"], "--region", cred["region"],
        "--cos-key", cred["cos_key"], "--content-type", "text/html",
        "--start-time", str(cred["start_time"]), "--expired-time", str(cred["expired_time"]),
        "--timeout", "300000"], capture_output=True, text=True, timeout=600)
    if cos.returncode != 0:
        print(f"  ❌ COS失败: {cos.stderr[:200]}")
        continue

    # add_knowledge
    resp = api("add_knowledge", {
        "media_type": 7, "media_id": media_id, "title": FNAME,
        "knowledge_base_id": KB_ID, "folder_id": TARGET,
        "file_info": {"cos_key": cred["cos_key"], "file_size": filesize, "file_name": FNAME}})
    if resp.get("code", 0) == 0:
        print("  ✅ 成功同步")
    else:
        print(f"  ❌ add_knowledge失败: {resp.get('msg', '')}")

print("\n=== HTML 上传完成 ===")

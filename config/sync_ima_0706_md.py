"""Sync missing MD files for week 0706-0712 to IMA聚宝盆

上传链路: preflight-check → check_repeated_names → create_media → cos-upload → add_knowledge
目标文件夹:
  深度研究/0706-0712  → folder_7479461721159006
  浑水调研/0706-0712  → folder_7479461725352539
"""
import json, subprocess, os

KB_ID = "9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g="
SKILL_DIR = "C:/Users/Administrator/.workbuddy/skills/ima-skill"

# (本地路径, 目标IMA folder_id)
TASKS = [
    # 深度研究/0706-0712
    ("G:/锅师/深度研究/0706-0712/2026-07-06_功率半导体产业链全景分析.md", "folder_7479461721159006"),
    ("G:/锅师/深度研究/0706-0712/2026-07-06_天岳先进_五Skill深度研报.md", "folder_7479461721159006"),
    ("G:/锅师/深度研究/0706-0712/2026-07-06_每日信息推送.md", "folder_7479461721159006"),
    ("G:/锅师/深度研究/0706-0712/2026-07-07_每日信息推送.md", "folder_7479461721159006"),
    # 浑水调研/0706-0712
    ("G:/锅师/浑水调研/0706-0712/2026-07-06_紧缺度日报.md", "folder_7479461725352539"),
    ("G:/锅师/浑水调研/0706-0712/2026-07-07_紧缺度日报.md", "folder_7479461725352539"),
]


def api(method, payload):
    cmd = ["node", f"{SKILL_DIR}/ima_api.cjs", f"openapi/wiki/v1/{method}", json.dumps(payload)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    out = r.stdout.strip()
    start = out.find('{')
    if start < 0:
        raise RuntimeError(f"No JSON in response: {out[:200]}")
    return json.loads(out[start:])


ok, fail = [], []

for filepath, folder_id in TASKS:
    if not os.path.exists(filepath):
        print(f"❌ 文件不存在: {filepath}")
        fail.append(filepath)
        continue
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    print(f"\n📤 {filename} → {folder_id}")

    # 1. preflight
    pf = subprocess.run(
        ["node", f"{SKILL_DIR}/knowledge-base/scripts/preflight-check.cjs", "--file", filepath],
        capture_output=True, text=True, timeout=15)
    if pf.returncode != 0:
        print(f"  ❌ preflight失败: {pf.stderr[:150]}")
        fail.append(filepath)
        continue
    try:
        pf_data = json.loads(pf.stdout.strip())
    except Exception:
        print(f"  ❌ preflight解析失败: {pf.stdout[:150]}")
        fail.append(filepath)
        continue

    file_name = pf_data.get("file_name", filename)
    file_ext = pf_data.get("file_ext", "md")
    content_type = pf_data.get("content_type", "text/markdown")
    media_type_val = pf_data.get("media_type", 7)
    print(f"  preflight: media_type={media_type_val} content_type={content_type}")

    # 2. check_repeated_names
    try:
        resp = api("check_repeated_names", {
            "params": [{"name": file_name, "media_type": media_type_val}],
            "knowledge_base_id": KB_ID, "folder_id": folder_id})
        is_rep = resp.get("data", {}).get("results", [{}])[0].get("is_repeated", False)
        if is_rep:
            print(f"  ⚠️ 已存在同名，跳过: {file_name}")
            ok.append(f"{filename} (已存在)")
            continue
    except Exception as e:
        print(f"  ⚠️ check_repeated异常，继续: {e}")

    # 3. create_media
    resp = api("create_media", {
        "file_name": file_name, "file_size": filesize, "content_type": content_type,
        "knowledge_base_id": KB_ID, "file_ext": file_ext})
    if resp.get("code", 0) != 0:
        print(f"  ❌ create_media失败: {resp.get('msg', '')}")
        fail.append(filepath)
        continue
    media_id = resp["data"]["media_id"]
    cred = resp["data"]["cos_credential"]

    # 4. cos upload
    cos = subprocess.run([
        "node", f"{SKILL_DIR}/knowledge-base/scripts/cos-upload.cjs",
        "--file", filepath,
        "--secret-id", cred["secret_id"], "--secret-key", cred["secret_key"],
        "--token", cred["token"], "--bucket", cred["bucket_name"],
        "--region", cred["region"], "--cos-key", cred["cos_key"],
        "--content-type", content_type,
        "--start-time", str(cred["start_time"]), "--expired-time", str(cred["expired_time"]),
        "--timeout", "300000"], capture_output=True, text=True, timeout=600)
    if cos.returncode != 0:
        print(f"  ❌ COS上传失败: {cos.stderr[:200]}")
        fail.append(filepath)
        continue
    print(f"  COS上传成功 ✅")

    # 5. add_knowledge
    resp = api("add_knowledge", {
        "media_type": media_type_val, "media_id": media_id, "title": file_name,
        "knowledge_base_id": KB_ID, "folder_id": folder_id,
        "file_info": {"cos_key": cred["cos_key"], "file_size": filesize, "file_name": file_name}})
    if resp.get("code", 0) == 0:
        print(f"  ✅ 成功同步")
        ok.append(filename)
    else:
        print(f"  ❌ add_knowledge失败: {resp.get('msg', '')}")
        fail.append(filepath)

print(f"\n=== 结果: 成功 {len(ok)} / 失败 {len(fail)} ===")
for f in ok:
    print("  ✅", f)
for f in fail:
    print("  ❌", f)

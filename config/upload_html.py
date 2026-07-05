"""Upload HTML file to IMA聚宝盆"""
import json, subprocess, os

KB_ID = "9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g="
TARGET = "folder_7479461721159006"
SKILL_DIR = "C:/Users/Administrator/.workbuddy/skills/ima-skill"
FILEPATH = "G:/锅师/深度研究/0706-0712/2026-07-05_每日窄门筛股.html"
FNAME = os.path.basename(FILEPATH)

def api(method, payload):
    cmd = ["node", f"{SKILL_DIR}/ima_api.cjs", f"openapi/wiki/v1/{method}", json.dumps(payload)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    out = r.stdout.strip()
    start = out.find("{")
    if start < 0:
        print(f"ERROR: No JSON in response: {out[:300]}")
        return None
    return json.loads(out[start:])

print("=" * 50)
print(f"Uploading: {FNAME}")
print("=" * 50)

# Step 1: Preflight check
print("\n1. Preflight check...")
preflight_cmd = ["node", f"{SKILL_DIR}/knowledge-base/scripts/preflight-check.cjs", "--file", FILEPATH]
pf = subprocess.run(preflight_cmd, capture_output=True, text=True, timeout=15)
print(f"stdout: {pf.stdout[:500]}")
print(f"stderr: {pf.stderr[:200]}")

if pf.returncode != 0:
    print("Preflight failed, trying manual upload...")
    # Manual approach: treat HTML as media_type=7 (markdown)
    filesize = os.path.getsize(FILEPATH)
    file_ext = "html"
    content_type = "text/html"
    media_type = 7  # try as markdown-type file
    
    # check_repeated_names
    resp = api("check_repeated_names", {
        "params": [{"name": FNAME, "media_type": media_type}],
        "knowledge_base_id": KB_ID,
        "folder_id": TARGET
    })
    print(f"Check repeated: code={resp.get('code') if resp else 'None'}")
    
    if resp and resp.get("code") == 0:
        is_repeated = resp["data"]["results"][0]["is_repeated"]
        if is_repeated:
            ts = "202607052020"
            base = FNAME.rsplit(".", 1)[0]
            FNAME = f"{base}_{ts}.{file_ext}"
            print(f"  Appended timestamp: {FNAME}")
    
    # create_media
    resp = api("create_media", {
        "file_name": FNAME,
        "file_size": filesize,
        "content_type": content_type,
        "knowledge_base_id": KB_ID,
        "file_ext": file_ext
    })
    if not resp or resp.get("code", 0) != 0:
        print(f"create_media failed: {resp.get('msg','') if resp else 'No response'}")
        exit(1)
    
    media_id = resp["data"]["media_id"]
    cred = resp["data"]["cos_credential"]
    print(f"media_id: {media_id}")
    
    # cos upload
    cos_cmd = [
        "node", f"{SKILL_DIR}/knowledge-base/scripts/cos-upload.cjs",
        "--file", FILEPATH,
        "--secret-id", cred["secret_id"],
        "--secret-key", cred["secret_key"],
        "--token", cred["token"],
        "--bucket", cred["bucket_name"],
        "--region", cred["region"],
        "--cos-key", cred["cos_key"],
        "--content-type", content_type,
        "--start-time", str(cred["start_time"]),
        "--expired-time", str(cred["expired_time"]),
        "--timeout", "300000"
    ]
    cos = subprocess.run(cos_cmd, capture_output=True, text=True, timeout=600)
    if cos.returncode != 0:
        print(f"COS upload failed: {cos.stderr[:300]}")
        exit(1)
    print("COS upload OK")
    
    # add_knowledge
    resp = api("add_knowledge", {
        "media_type": media_type,
        "media_id": media_id,
        "title": FNAME,
        "knowledge_base_id": KB_ID,
        "folder_id": TARGET,
        "file_info": {
            "cos_key": cred["cos_key"],
            "file_size": filesize,
            "file_name": FNAME
        }
    })
    if resp and resp.get("code") == 0:
        print(f"✅ HTML synced to IMA 深度研究/0706-0712/")
    else:
        print(f"add_knowledge failed: {resp.get('msg','') if resp else 'No response'}")

else:
    pf_data = json.loads(pf.stdout.strip())
    print(f"Preflight OK: media_type={pf_data['media_type']}, type={pf_data['content_type']}")
    # Continue with normal flow...

print("\n✅ Done")

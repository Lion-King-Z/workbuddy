"""Upload 0706-0712 narrow door screening files to IMA聚宝盆"""
import json, subprocess, os, re
from datetime import date, timedelta

KB_ID = "9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g="
DEEP_PARENT = "folder_7471884144740883"
SKILL_DIR = "C:/Users/Administrator/.workbuddy/skills/ima-skill"
WEEK_FOLDER = "0706-0712"

with open(f"{SKILL_DIR}/ima_api.cjs") as f:
    pass

def api(method, payload):
    cmd = ["node", f"{SKILL_DIR}/ima_api.cjs", f"openapi/wiki/v1/{method}", json.dumps(payload)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        raise RuntimeError(f"API failed: {r.stderr}")
    # Parse response - might have leading non-JSON
    out = r.stdout.strip()
    # Find JSON start
    start = out.find('{')
    if start < 0:
        raise RuntimeError(f"No JSON in response: {out[:200]}")
    return json.loads(out[start:])

# Step 1: Find/create 0706-0712 folder under 深度研究
print(f"🔍 查找IMA文件夹: 深度研究/{WEEK_FOLDER}")
resp = api("search_knowledge", {
    "knowledge_base_id": KB_ID, "query": WEEK_FOLDER, "cursor": "", "limit": 50
})

target_id = None
for m in resp.get("data", {}).get("info_list", []):
    if m.get("media_type") == 99 and m.get("title") == WEEK_FOLDER \
       and m.get("parent_folder_id") == DEEP_PARENT:
        target_id = m["media_id"]
        print(f"✅ 找到现有文件夹: {target_id}")
        break

if not target_id:
    print(f"🆕 创建文件夹: 深度研究/{WEEK_FOLDER}")
    resp = api("create_folder", {
        "knowledge_base_id": KB_ID, "name": WEEK_FOLDER,
        "folder_id": DEEP_PARENT
    })
    target_id = resp["data"]["media_id"]
    print(f"✅ 创建成功: {target_id}")

TARGET_FOLDER = target_id

# Step 2: Upload MD file
files = [
    "G:/锅师/深度研究/0706-0712/2026-07-05_每日窄门筛股.md",
    "G:/锅师/深度研究/0706-0712/2026-07-05_每日窄门筛股.html"
]

for filepath in files:
    filename = os.path.basename(filepath)
    ext = filename.rsplit('.', 1)[1].lower()
    filesize = os.path.getsize(filepath)
    
    # media type: md=7, html=2(web)
    media_type = 7 if ext == "md" else 2
    
    if ext == "html":
        print(f"🌐 HTML文件需通过import_urls或客户端上传，跳过标准流程")
        print(f"   → {filepath}")
        continue
    
    print(f"\n📤 上传: {filename} ({filesize} bytes)")
    
    # preflight
    preflight_cmd = ["node", f"{SKILL_DIR}/knowledge-base/scripts/preflight-check.cjs", "--file", filepath]
    pf = subprocess.run(preflight_cmd, capture_output=True, text=True, timeout=15)
    if pf.returncode != 0:
        print(f"❌ Preflight失败: {pf.stderr}")
        continue
    pf_data = json.loads(pf.stdout.strip())
    if not pf_data.get("pass"):
        print(f"❌ Preflight拒绝: {pf_data.get('reason','')}")
        continue
    
    file_name = pf_data["file_name"]
    file_ext = pf_data["file_ext"]
    file_size = pf_data["file_size"]
    content_type = pf_data["content_type"]
    media_type_val = pf_data["media_type"]
    
    print(f"   类型: media_type={media_type_val}, content_type={content_type}")
    
    # check_repeated_names
    resp = api("check_repeated_names", {
        "params": [{"name": file_name, "media_type": media_type_val}],
        "knowledge_base_id": KB_ID,
        "folder_id": TARGET_FOLDER
    })
    is_repeated = resp["data"]["results"][0]["is_repeated"]
    if is_repeated:
        # append timestamp
        ts = date.today().strftime("%Y%m%d%H%M%S")
        base = file_name.rsplit('.', 1)[0]
        file_name = f"{base}_{ts}.{file_ext}"
        print(f"   ⚠️ 同名文件存在，追加时间戳: {file_name}")
    
    # create_media
    resp = api("create_media", {
        "file_name": file_name,
        "file_size": file_size,
        "content_type": content_type,
        "knowledge_base_id": KB_ID,
        "file_ext": file_ext
    })
    if resp.get("code", 0) != 0:
        print(f"❌ create_media失败: {resp.get('msg','')}")
        continue
    
    media_id = resp["data"]["media_id"]
    cred = resp["data"]["cos_credential"]
    print(f"   media_id: {media_id}")
    
    # cos upload
    cos_cmd = [
        "node", f"{SKILL_DIR}/knowledge-base/scripts/cos-upload.cjs",
        "--file", filepath,
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
        print(f"❌ COS上传失败: {cos.stderr[:200]}")
        continue
    print(f"   COS上传成功 ✅")
    
    # add_knowledge
    resp = api("add_knowledge", {
        "media_type": media_type_val,
        "media_id": media_id,
        "title": file_name,
        "knowledge_base_id": KB_ID,
        "folder_id": TARGET_FOLDER,
        "file_info": {
            "cos_key": cred["cos_key"],
            "file_size": file_size,
            "file_name": file_name
        }
    })
    if resp.get("code", 0) == 0:
        print(f"   ✅ 已同步到IMA聚宝盆 深度研究/{WEEK_FOLDER}/")
    else:
        print(f"   ❌ add_knowledge失败: {resp.get('msg','')}")

print("\n✅ IMA同步完成")

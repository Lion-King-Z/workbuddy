#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMA 知识库搜索 helper（mcp__ima-mcp 替代方案）

背景：mcp__ima-mcp__search_knowledge 连续多日返回 220001 参数错误，
      而 ima-skill 的 ima_api.cjs 调用 openapi/wiki/v1/search_knowledge 正常。
      本脚本封装 ima_api.cjs，提供稳定的 IMA 搜索能力。

用法：
  python ima_search_helper.py search <knowledge_base_id> <query> [cursor]
  python ima_search_helper.py media <media_id>
  python ima_search_helper.py list <knowledge_base_id> [folder_id] [cursor] [limit]

输出：统一 JSON 到 stdout（包含 code/data 或 error）
"""

import json
import subprocess
import sys
from pathlib import Path

IMA_API_CJS = Path.home() / ".workbuddy" / "skills" / "ima-skill" / "ima_api.cjs"


def run_ima_api(api_path: str, body: dict) -> dict:
    if not IMA_API_CJS.exists():
        return {"code": -1, "error": f"ima_api.cjs not found: {IMA_API_CJS}"}

    cmd = [
        "node",
        str(IMA_API_CJS),
        api_path,
        json.dumps(body, ensure_ascii=False),
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(IMA_API_CJS.parent),
        )
    except Exception as e:
        return {"code": -1, "error": str(e)}

    if result.returncode != 0:
        return {"code": -1, "error": result.stderr.strip() or "unknown node error"}

    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return {"code": -1, "error": "invalid JSON response", "raw": result.stdout.strip()}


def search(knowledge_base_id: str, query: str, cursor: str = ""):
    return run_ima_api(
        "openapi/wiki/v1/search_knowledge",
        {"knowledge_base_id": knowledge_base_id, "query": query, "cursor": cursor},
    )


def media_info(media_id: str):
    return run_ima_api("openapi/wiki/v1/get_media_info", {"media_id": media_id})


def list_kb(knowledge_base_id: str, folder_id: str = "", cursor: str = "", limit: int = 20):
    body = {"knowledge_base_id": knowledge_base_id, "cursor": cursor, "limit": limit}
    if folder_id:
        body["folder_id"] = folder_id
    return run_ima_api("openapi/wiki/v1/get_knowledge_list", body)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    action = sys.argv[1]

    if action == "search" and len(sys.argv) >= 4:
        kb_id = sys.argv[2]
        query = sys.argv[3]
        cursor = sys.argv[4] if len(sys.argv) > 4 else ""
        print(json.dumps(search(kb_id, query, cursor), ensure_ascii=False, indent=2))
    elif action == "media" and len(sys.argv) >= 3:
        print(json.dumps(media_info(sys.argv[2]), ensure_ascii=False, indent=2))
    elif action == "list" and len(sys.argv) >= 3:
        kb_id = sys.argv[2]
        folder_id = sys.argv[3] if len(sys.argv) > 3 else ""
        cursor = sys.argv[4] if len(sys.argv) > 4 else ""
        limit = int(sys.argv[5]) if len(sys.argv) > 5 else 20
        print(json.dumps(list_kb(kb_id, folder_id, cursor, limit), ensure_ascii=False, indent=2))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()

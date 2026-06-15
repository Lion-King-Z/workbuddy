# IMA OpenAPI 已知可用接口（聚宝盆知识库）

## 文件夹操作

| 接口 | 说明 |
|------|------|
| `openapi/wiki/v1/create_folder` | 创建子文件夹。参数：`knowledge_base_id`, `folder_id`(父文件夹), `name` |

## 知识库操作

| 接口 | 说明 |
|------|------|
| `openapi/wiki/v1/search_knowledge_base` | 搜索知识库列表 |
| `openapi/wiki/v1/get_knowledge_base` | 获取知识库信息 |
| `openapi/wiki/v1/get_knowledge_list` | 浏览知识库内容（支持 folder_id 进入子文件夹） |
| `openapi/wiki/v1/search_knowledge` | 在知识库中搜索 |
| `openapi/wiki/v1/get_addable_knowledge_base_list` | 获取可添加的知识库列表 |

## 文件操作

| 接口 | 说明 |
|------|------|
| `openapi/wiki/v1/create_media` | 创建媒体（获取COS凭证） |
| `openapi/wiki/v1/add_knowledge` | 添加知识（文件上传最后一步，支持 folder_id） |
| `openapi/wiki/v1/check_repeated_names` | 检查文件名重复 |
| `openapi/wiki/v1/delete_knowledge` | 删除知识条目（media_ids 数组） |
| `openapi/wiki/v1/get_media_info` | 获取媒体原文内容 |

## URL 操作

| 接口 | 说明 |
|------|------|
| `openapi/wiki/v1/import_urls` | 添加网页/微信文章到知识库 |

# Crawlora Xiaohongshu Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `4`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xiaohongshu | `xiaohongshu.explore` | `xiaohongshu-explore` | `GET /xiaohongshu/explore` | `channel_id` (query String) | `ApiKeyAuth` | `XiaohongshuExploreResponse` |  |
| xiaohongshu | `xiaohongshu.note` | `xiaohongshu-note` | `GET /xiaohongshu/note` | `url` (query String)<br>`note_id` (query String)<br>`xsec_token` (query String) | `ApiKeyAuth` | `XiaohongshuNoteResponse` |  |
| xiaohongshu | `xiaohongshu.note_comments` | `xiaohongshu-note-comments` | `GET /xiaohongshu/note-comments` | `url` (query String)<br>`note_id` (query String)<br>`xsec_token` (query String)<br>`cursor` (query String) | `ApiKeyAuth` | `XiaohongshuNoteCommentsResponse` |  |
| xiaohongshu | `xiaohongshu.search_suggest` | `xiaohongshu-search-suggest` | `GET /xiaohongshu/search-suggest` | `keyword` (query String required) | `ApiKeyAuth` | `XiaohongshuSearchSuggestResponse` |  |

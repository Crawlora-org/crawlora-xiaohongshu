# Crawlora Xiaohongshu JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `4`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xiaohongshu | `xiaohongshu.explore` | `xiaohongshu-explore` | `GET /xiaohongshu/explore` | `channel_id` (query string) | `ApiKeyAuth` | `XiaohongshuExploreResponse` |  |
| xiaohongshu | `xiaohongshu.note` | `xiaohongshu-note` | `GET /xiaohongshu/note` | `url` (query string)<br>`note_id` (query string)<br>`xsec_token` (query string) | `ApiKeyAuth` | `XiaohongshuNoteResponse` |  |
| xiaohongshu | `xiaohongshu.noteComments` | `xiaohongshu-note-comments` | `GET /xiaohongshu/note-comments` | `url` (query string)<br>`note_id` (query string)<br>`xsec_token` (query string)<br>`cursor` (query string) | `ApiKeyAuth` | `XiaohongshuNoteCommentsResponse` |  |
| xiaohongshu | `xiaohongshu.searchSuggest` | `xiaohongshu-search-suggest` | `GET /xiaohongshu/search-suggest` | `keyword` (query string required) | `ApiKeyAuth` | `XiaohongshuSearchSuggestResponse` |  |

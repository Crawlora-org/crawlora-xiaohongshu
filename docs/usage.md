# Xiaohongshu API endpoint reference and client usage

This reference lists all 4 public Xiaohongshu API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/xiaohongshu`, `crawlora-xiaohongshu`, and `crawlora-xiaohongshu` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Xiaohongshu locally; Crawlora is independent from and not endorsed by Xiaohongshu or its owners.

The package tracks the public API contract revision `sha256:d16e12aef9b5fee56869277f565b679d424fab368cc5241b543e5a063fa81afa` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `xiaohongshu`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `explore` | `explore` | `xiaohongshu.explore` | `GET /xiaohongshu/explore` | `channel_id` (query, optional) | Anonymous Xiaohongshu explore/channel feed |
| `note` | `note` | `xiaohongshu.note` | `GET /xiaohongshu/note` | `url` (query, optional), `note_id` (query, optional), `xsec_token` (query, optional) | Anonymous Xiaohongshu note detail |
| `noteComments` | `note_comments` | `xiaohongshu.note_comments` | `GET /xiaohongshu/note-comments` | `url` (query, optional), `note_id` (query, optional), `xsec_token` (query, optional), `cursor` (query, optional) | Anonymous Xiaohongshu note comments |
| `searchSuggest` | `search_suggest` | `xiaohongshu.search_suggest` | `GET /xiaohongshu/search-suggest` | `keyword` (query, required) | Anonymous Xiaohongshu search suggestions |

## Client forms

- JavaScript: import `XiaohongshuClient` (also exported as `Client`) from `@crawlora-org/xiaohongshu`; use `new XiaohongshuClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `XiaohongshuClient` (also exported as `Client`) from `crawlora_xiaohongshu`; use `with XiaohongshuClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncXiaohongshuClient`, used with `async with` and `await`.
- Rust: add `crawlora-xiaohongshu` with Cargo; import `Client` and the generated operation parameter struct, then call `client.xiaohongshu.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-xiaohongshu/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.

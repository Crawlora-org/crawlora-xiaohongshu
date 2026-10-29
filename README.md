# Xiaohongshu clients for Crawlora

Official Crawlora client packages for the hosted Xiaohongshu API. Access 4 API endpoints covering public explore feeds, note details, comments, and search suggestions from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Xiaohongshu locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Xiaohongshu or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/xiaohongshu`](javascript/README.md)
- Python: [`crawlora-xiaohongshu`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-xiaohongshu`](go.mod)
- Ruby: [`crawlora-xiaohongshu`](ruby/README.md)
- Java: [`net.crawlora:crawlora-xiaohongshu:0.1.0`](java/README.md)
- PHP: [`crawlora/xiaohongshu`](php/README.md)
- Rust: [`crawlora-xiaohongshu`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 4 selected public Xiaohongshu API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/xiaohongshu/explore` | `xiaohongshu-explore` | Anonymous Xiaohongshu explore/channel feed |
| `GET` | `/xiaohongshu/note` | `xiaohongshu-note` | Anonymous Xiaohongshu note detail |
| `GET` | `/xiaohongshu/note-comments` | `xiaohongshu-note-comments` | Anonymous Xiaohongshu note comments |
| `GET` | `/xiaohongshu/search-suggest` | `xiaohongshu-search-suggest` | Anonymous Xiaohongshu search suggestions |

## License

MIT. See [LICENSE](LICENSE).

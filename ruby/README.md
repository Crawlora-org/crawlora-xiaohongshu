# Crawlora Xiaohongshu API client for Ruby (`crawlora-xiaohongshu`)

This Ruby gem calls Crawlora's hosted Xiaohongshu API at `https://api.crawlora.net/api/v1`. It exposes 4 endpoints covering public explore feeds, note details, comments, and search suggestions; it does not call or scrape Xiaohongshu directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-xiaohongshu"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/xiaohongshu"

client = Crawlora::Xiaohongshu::Client.new
result = client.request("xiaohongshu-explore", JSON.parse("{}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 4 API operations.

```ruby
client = Crawlora::Xiaohongshu::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Xiaohongshu API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-xiaohongshu/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/xiaohongshu/explore` | `xiaohongshu-explore` | Anonymous Xiaohongshu explore/channel feed |
| `GET` | `/xiaohongshu/note` | `xiaohongshu-note` | Anonymous Xiaohongshu note detail |
| `GET` | `/xiaohongshu/note-comments` | `xiaohongshu-note-comments` | Anonymous Xiaohongshu note comments |
| `GET` | `/xiaohongshu/search-suggest` | `xiaohongshu-search-suggest` | Anonymous Xiaohongshu search suggestions |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-xiaohongshu) for account setup, the API operation reference, and release history.

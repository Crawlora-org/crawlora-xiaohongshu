# @crawlora-org/xiaohongshu — Xiaohongshu API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Xiaohongshu API.
It exposes 4 API endpoints for public explore feeds, note details, comments, and search suggestions through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-javascript-homepage). It does not run a browser or scrape Xiaohongshu locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Xiaohongshu or its owners.

## Install

```sh
npm install @crawlora-org/xiaohongshu
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { XiaohongshuClient } from "@crawlora-org/xiaohongshu";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new XiaohongshuClient({ apiKey });
const result1 = await client.explore({});
console.log(result1);
const result2 = await client.searchSuggest({ keyword: "coffee" });
console.log(result2);
```

The client also exports `Client` as an alias for `XiaohongshuClient`. Operation
methods are available directly in camelCase and through the `xiaohongshu`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-xiaohongshu/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-xiaohongshu/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Xiaohongshu API endpoints

This package exposes each route below as a direct method and through the `xiaohongshu` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-xiaohongshu/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/xiaohongshu/explore` | `xiaohongshu-explore` | Anonymous Xiaohongshu explore/channel feed |
| `GET` | `/xiaohongshu/note` | `xiaohongshu-note` | Anonymous Xiaohongshu note detail |
| `GET` | `/xiaohongshu/note-comments` | `xiaohongshu-note-comments` | Anonymous Xiaohongshu note comments |
| `GET` | `/xiaohongshu/search-suggest` | `xiaohongshu-search-suggest` | Anonymous Xiaohongshu search suggestions |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.

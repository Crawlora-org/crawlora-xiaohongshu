import { XiaohongshuClient } from "../src/index.js";

const client = new XiaohongshuClient({ apiKey: "test-key" });
void client.searchSuggest({"keyword": "sample"});
void client.request("xiaohongshu-search-suggest", {"keyword": "sample"});
const streamResponse: Promise<Response> = client.request("xiaohongshu-search-suggest", {"keyword": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("xiaohongshu-search-suggest", {"keyword": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.searchSuggest({"keyword": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("xiaohongshu-search-suggest", {"keyword": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("xiaohongshu-search-suggest", {"keyword": "sample"}, { responseType: "text" });
void rawText;


void client.explore();
void client.request("xiaohongshu-explore");
// @ts-expect-error The selected operation requires its documented params.
void client.searchSuggest();

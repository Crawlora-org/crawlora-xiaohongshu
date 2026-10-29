import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class XiaohongshuClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-xiaohongshu-js/0.1.0" });
    this["explore"] = (...args) => this.request("xiaohongshu-explore", ...args);
    this["note"] = (...args) => this.request("xiaohongshu-note", ...args);
    this["noteComments"] = (...args) => this.request("xiaohongshu-note-comments", ...args);
    this["searchSuggest"] = (...args) => this.request("xiaohongshu-search-suggest", ...args);
  }
}

export { XiaohongshuClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default XiaohongshuClient;

import os

from crawlora_xiaohongshu import XiaohongshuClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with XiaohongshuClient(api_key=api_key) as client:
    explore = client.explore()
    print('explore', explore)
    search_suggest = client.search_suggest(keyword='coffee')
    print('search_suggest', search_suggest)

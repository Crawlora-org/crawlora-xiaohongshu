"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class XiaohongshuClient(CrawloraClient):
    """Synchronous Xiaohongshu API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-xiaohongshu-python/0.1.0')
        super().__init__(*args, **kwargs)

    def explore(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('xiaohongshu-explore', params, response_type=response_type, timeout=timeout, headers=headers)

    def note(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('xiaohongshu-note', params, response_type=response_type, timeout=timeout, headers=headers)

    def note_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('xiaohongshu-note-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('xiaohongshu-search-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncXiaohongshuClient(AsyncCrawloraClient):
    """Asynchronous Xiaohongshu API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-xiaohongshu-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def explore(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('xiaohongshu-explore', params, response_type=response_type, timeout=timeout, headers=headers)

    async def note(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('xiaohongshu-note', params, response_type=response_type, timeout=timeout, headers=headers)

    async def note_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('xiaohongshu-note-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('xiaohongshu-search-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

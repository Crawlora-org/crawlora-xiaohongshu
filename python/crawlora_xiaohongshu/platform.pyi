from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelXiaohongshuSuggestResponseDoc = TypedDict('ModelXiaohongshuSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelXiaohongshuSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelXiaohongshuSuggestResponse = TypedDict('ModelXiaohongshuSuggestResponse', {
    'count': NotRequired[int],
    'items': NotRequired[list[ModelXiaohongshuSuggestItem]],
    'keyword': NotRequired[str],
    'search_cpl_id': NotRequired[str],
    'word_request_id': NotRequired[str],
}, total=False)

ModelXiaohongshuSuggestItem = TypedDict('ModelXiaohongshuSuggestItem', {
    'highlight_flags': NotRequired[list[bool]],
    'search_type': NotRequired[str],
    'text': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelXiaohongshuCommentsResponseDoc = TypedDict('ModelXiaohongshuCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelXiaohongshuCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelXiaohongshuCommentsResponse = TypedDict('ModelXiaohongshuCommentsResponse', {
    'count': NotRequired[int],
    'cursor': NotRequired[str],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[ModelXiaohongshuComment]],
    'note_id': NotRequired[str],
}, total=False)

ModelXiaohongshuComment = TypedDict('ModelXiaohongshuComment', {
    'author': NotRequired[ModelXiaohongshuCommentAuthor],
    'comment_id': NotRequired[str],
    'content': NotRequired[str],
    'created_at': NotRequired[int],
    'ip_location': NotRequired[str],
    'like_count': NotRequired[int],
    'sub_comment_count': NotRequired[int],
    'sub_comments': NotRequired[list[ModelXiaohongshuComment]],
}, total=False)

ModelXiaohongshuCommentAuthor = TypedDict('ModelXiaohongshuCommentAuthor', {
    'avatar_url': NotRequired[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelXiaohongshuNoteResponseDoc = TypedDict('ModelXiaohongshuNoteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelXiaohongshuNoteResponse],
    'msg': NotRequired[str],
}, total=False)

ModelXiaohongshuNoteResponse = TypedDict('ModelXiaohongshuNoteResponse', {
    'author': NotRequired[ModelXiaohongshuNoteAuthor],
    'description': NotRequired[str],
    'image_urls': NotRequired[list[str]],
    'note_id': NotRequired[str],
    'published_at': NotRequired[str],
    'stats': NotRequired[ModelXiaohongshuNoteStats],
    'tags': NotRequired[list[ModelXiaohongshuNoteTag]],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
    'video_duration_seconds': NotRequired[int],
    'video_url': NotRequired[str],
}, total=False)

ModelXiaohongshuNoteTag = TypedDict('ModelXiaohongshuNoteTag', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelXiaohongshuNoteStats = TypedDict('ModelXiaohongshuNoteStats', {
    'collected_count': NotRequired[int],
    'comment_count': NotRequired[int],
    'liked_count': NotRequired[int],
    'share_count': NotRequired[int],
}, total=False)

ModelXiaohongshuNoteAuthor = TypedDict('ModelXiaohongshuNoteAuthor', {
    'avatar_url': NotRequired[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelXiaohongshuExploreResponseDoc = TypedDict('ModelXiaohongshuExploreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelXiaohongshuExploreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelXiaohongshuExploreResponse = TypedDict('ModelXiaohongshuExploreResponse', {
    'channel_id': NotRequired[str],
    'channels': NotRequired[list[ModelXiaohongshuChannel]],
    'count': NotRequired[int],
    'items': NotRequired[list[ModelXiaohongshuExploreCard]],
}, total=False)

ModelXiaohongshuExploreCard = TypedDict('ModelXiaohongshuExploreCard', {
    'author': NotRequired[ModelXiaohongshuNoteAuthor],
    'cover_url': NotRequired[str],
    'liked_count': NotRequired[int],
    'note_id': NotRequired[str],
    'note_url': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'xsec_token': NotRequired[str],
}, total=False)

ModelXiaohongshuChannel = TypedDict('ModelXiaohongshuChannel', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

XiaohongshuExploreResponse = ModelXiaohongshuExploreResponseDoc
XiaohongshuExploreParams = TypedDict('XiaohongshuExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'channel_id': NotRequired[str],
}, total=False)

XiaohongshuNoteResponse = ModelXiaohongshuNoteResponseDoc
XiaohongshuNoteParams = TypedDict('XiaohongshuNoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
}, total=False)

XiaohongshuNoteCommentsResponse = ModelXiaohongshuCommentsResponseDoc
XiaohongshuNoteCommentsParams = TypedDict('XiaohongshuNoteCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

XiaohongshuSearchSuggestResponse = ModelXiaohongshuSuggestResponseDoc
XiaohongshuSearchSuggestParams = TypedDict('XiaohongshuSearchSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

class XiaohongshuGroup:
    @overload
    def explore(self, **params: Unpack[XiaohongshuExploreStreamParams]) -> BinaryIO: ...
    @overload
    def explore(self, **params: Unpack[XiaohongshuExploreTextResponseParams]) -> str: ...
    @overload
    def explore(self, **params: Unpack[XiaohongshuExploreDefaultParams]) -> XiaohongshuExploreResponse: ...
    @overload
    def note(self, **params: Unpack[XiaohongshuNoteStreamParams]) -> BinaryIO: ...
    @overload
    def note(self, **params: Unpack[XiaohongshuNoteTextResponseParams]) -> str: ...
    @overload
    def note(self, **params: Unpack[XiaohongshuNoteDefaultParams]) -> XiaohongshuNoteResponse: ...
    @overload
    def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsTextResponseParams]) -> str: ...
    @overload
    def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsDefaultParams]) -> XiaohongshuNoteCommentsResponse: ...
    @overload
    def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestTextResponseParams]) -> str: ...
    @overload
    def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestDefaultParams]) -> XiaohongshuSearchSuggestResponse: ...

OperationId = Literal[
    'xiaohongshu-explore',
    'xiaohongshu-note',
    'xiaohongshu-note-comments',
    'xiaohongshu-search-suggest',
]

class CrawloraClient:
    xiaohongshu: XiaohongshuGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['xiaohongshu-explore'],
        params: XiaohongshuExploreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuExploreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['xiaohongshu-note'],
        params: XiaohongshuNoteParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuNoteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['xiaohongshu-note-comments'],
        params: XiaohongshuNoteCommentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuNoteCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['xiaohongshu-search-suggest'],
        params: XiaohongshuSearchSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuSearchSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['xiaohongshu-explore'],
        params: XiaohongshuExploreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuExploreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['xiaohongshu-note'],
        params: XiaohongshuNoteParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuNoteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['xiaohongshu-note-comments'],
        params: XiaohongshuNoteCommentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuNoteCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['xiaohongshu-search-suggest'],
        params: XiaohongshuSearchSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> XiaohongshuSearchSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class XiaohongshuClient(CrawloraClient):
    def __enter__(self) -> XiaohongshuClient: ...
    @overload
    def explore(self, **params: Unpack[XiaohongshuExploreStreamParams]) -> BinaryIO: ...
    @overload
    def explore(self, **params: Unpack[XiaohongshuExploreTextResponseParams]) -> str: ...
    @overload
    def explore(self, **params: Unpack[XiaohongshuExploreDefaultParams]) -> XiaohongshuExploreResponse: ...
    @overload
    def note(self, **params: Unpack[XiaohongshuNoteStreamParams]) -> BinaryIO: ...
    @overload
    def note(self, **params: Unpack[XiaohongshuNoteTextResponseParams]) -> str: ...
    @overload
    def note(self, **params: Unpack[XiaohongshuNoteDefaultParams]) -> XiaohongshuNoteResponse: ...
    @overload
    def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsTextResponseParams]) -> str: ...
    @overload
    def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsDefaultParams]) -> XiaohongshuNoteCommentsResponse: ...
    @overload
    def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestTextResponseParams]) -> str: ...
    @overload
    def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestDefaultParams]) -> XiaohongshuSearchSuggestResponse: ...

class AsyncXiaohongshuClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncXiaohongshuClient: ...
    xiaohongshu: _AsyncXiaohongshuGroup
    @overload
    async def explore(self, **params: Unpack[XiaohongshuExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def explore(self, **params: Unpack[XiaohongshuExploreTextResponseParams]) -> str: ...
    @overload
    async def explore(self, **params: Unpack[XiaohongshuExploreDefaultParams]) -> XiaohongshuExploreResponse: ...
    @overload
    async def note(self, **params: Unpack[XiaohongshuNoteStreamParams]) -> BinaryIO: ...
    @overload
    async def note(self, **params: Unpack[XiaohongshuNoteTextResponseParams]) -> str: ...
    @overload
    async def note(self, **params: Unpack[XiaohongshuNoteDefaultParams]) -> XiaohongshuNoteResponse: ...
    @overload
    async def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsTextResponseParams]) -> str: ...
    @overload
    async def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsDefaultParams]) -> XiaohongshuNoteCommentsResponse: ...
    @overload
    async def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestTextResponseParams]) -> str: ...
    @overload
    async def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestDefaultParams]) -> XiaohongshuSearchSuggestResponse: ...

class _AsyncXiaohongshuGroup:
    @overload
    async def explore(self, **params: Unpack[XiaohongshuExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def explore(self, **params: Unpack[XiaohongshuExploreTextResponseParams]) -> str: ...
    @overload
    async def explore(self, **params: Unpack[XiaohongshuExploreDefaultParams]) -> XiaohongshuExploreResponse: ...
    @overload
    async def note(self, **params: Unpack[XiaohongshuNoteStreamParams]) -> BinaryIO: ...
    @overload
    async def note(self, **params: Unpack[XiaohongshuNoteTextResponseParams]) -> str: ...
    @overload
    async def note(self, **params: Unpack[XiaohongshuNoteDefaultParams]) -> XiaohongshuNoteResponse: ...
    @overload
    async def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsTextResponseParams]) -> str: ...
    @overload
    async def note_comments(self, **params: Unpack[XiaohongshuNoteCommentsDefaultParams]) -> XiaohongshuNoteCommentsResponse: ...
    @overload
    async def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestTextResponseParams]) -> str: ...
    @overload
    async def search_suggest(self, **params: Unpack[XiaohongshuSearchSuggestDefaultParams]) -> XiaohongshuSearchSuggestResponse: ...

XiaohongshuExploreDefaultParams = TypedDict('XiaohongshuExploreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'channel_id': NotRequired[str],
}, total=False)

XiaohongshuExploreTextResponseParams = TypedDict('XiaohongshuExploreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'channel_id': NotRequired[str],
}, total=False)

XiaohongshuExploreStreamParams = TypedDict('XiaohongshuExploreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'channel_id': NotRequired[str],
}, total=False)

XiaohongshuNoteDefaultParams = TypedDict('XiaohongshuNoteDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
}, total=False)

XiaohongshuNoteTextResponseParams = TypedDict('XiaohongshuNoteTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
}, total=False)

XiaohongshuNoteStreamParams = TypedDict('XiaohongshuNoteStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
}, total=False)

XiaohongshuNoteCommentsDefaultParams = TypedDict('XiaohongshuNoteCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

XiaohongshuNoteCommentsTextResponseParams = TypedDict('XiaohongshuNoteCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

XiaohongshuNoteCommentsStreamParams = TypedDict('XiaohongshuNoteCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': NotRequired[str],
    'note_id': NotRequired[str],
    'xsec_token': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

XiaohongshuSearchSuggestDefaultParams = TypedDict('XiaohongshuSearchSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
}, total=False)

XiaohongshuSearchSuggestTextResponseParams = TypedDict('XiaohongshuSearchSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
}, total=False)

XiaohongshuSearchSuggestStreamParams = TypedDict('XiaohongshuSearchSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
}, total=False)

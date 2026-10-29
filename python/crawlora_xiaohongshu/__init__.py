"""Typed Xiaohongshu client for the Crawlora hosted API."""

from .platform import XiaohongshuClient, AsyncXiaohongshuClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = XiaohongshuClient
AsyncClient = AsyncXiaohongshuClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Xiaohongshu'
PLATFORM = 'xiaohongshu'
CONTRACT_REVISION = 'sha256:d16e12aef9b5fee56869277f565b679d424fab368cc5241b543e5a063fa81afa'

__all__ = [
    "XiaohongshuClient", "AsyncXiaohongshuClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]

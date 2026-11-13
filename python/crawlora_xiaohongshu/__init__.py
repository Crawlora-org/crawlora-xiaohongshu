"""Typed Xiaohongshu client for the Crawlora hosted API."""

from .platform import XiaohongshuClient, AsyncXiaohongshuClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = XiaohongshuClient
AsyncClient = AsyncXiaohongshuClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Xiaohongshu'
PLATFORM = 'xiaohongshu'
CONTRACT_REVISION = 'sha256:3668547685acbee974c5c9c0a546daf2c0ed7be4ba0331f6ddf82d6c7686b41e'

__all__ = [
    "XiaohongshuClient", "AsyncXiaohongshuClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]

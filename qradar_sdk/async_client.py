"""Asynchronous wrappers for the QRadar SDK."""

from __future__ import annotations

import asyncio
from functools import partial
from typing import Any, Dict

from .client import QRadarClient


class _AsyncProxy:
    """Wrap SDK objects and execute callable members in a worker thread."""

    def __init__(self, target: Any) -> None:
        self._target = target
        self._cache: Dict[str, Any] = {}

    def __getattr__(self, name: str) -> Any:
        if name in self._cache:
            return self._cache[name]

        attr = getattr(self._target, name)
        if callable(attr):
            async def _call(*args: Any, **kwargs: Any) -> Any:
                call = partial(attr, *args, **kwargs)
                return await asyncio.to_thread(call)

            self._cache[name] = _call
            return _call

        if getattr(attr.__class__, "__module__", "").startswith("qradar_sdk"):
            proxy = _AsyncProxy(attr)
            self._cache[name] = proxy
            return proxy

        return attr


class AsyncQRadarClient(_AsyncProxy):
    """Async facade over :class:`qradar_sdk.client.QRadarClient`."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(QRadarClient(*args, **kwargs))

    async def close(self) -> None:
        """Close the underlying HTTP session."""
        await asyncio.to_thread(self._target.close)

    async def __aenter__(self) -> "AsyncQRadarClient":
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

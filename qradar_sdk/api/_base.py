"""Shared primitives for the resource-oriented public API."""

from __future__ import annotations

from .._http import QRadarSession


class ResourceBase:
    """Base class for API resources backed by one QRadar session."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

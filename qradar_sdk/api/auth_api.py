"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class LogoutResource(ResourceBase):
    """Operations below ``/auth/logout``."""

    def create(self, **kwargs: Any) -> Any:
        'Invoke this method as an authorized user and your session will be invalidated.'
        url = '/auth/logout'
        return self._s.post(url, **kwargs)


class AuthAPI(ResourceBase):
    """Resource-oriented client for the ``auth_api`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.logout: LogoutResource = LogoutResource(session)

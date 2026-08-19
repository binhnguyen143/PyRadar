"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class LoginAttemptsResource(ResourceBase):
    """Operations below ``/access/login_attempts``."""

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of login attempts.'
        url = '/access/login_attempts'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class AccessAPI(ResourceBase):
    """Resource-oriented client for the ``access`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.login_attempts: LoginAttemptsResource = LoginAttemptsResource(session)

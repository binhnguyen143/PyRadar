"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class SecurityDataCountResource(ResourceBase):
    """Operations below ``/health_data/security_data_count``."""

    def get(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves count of security artifacts in QRadar'
        url = '/health_data/security_data_count'
        return self._s.get(url, fields=fields, **kwargs)


class TopOffensesResource(ResourceBase):
    """Operations below ``/health_data/top_offenses``."""

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves Top Offenses in the system sorted by update count.'
        url = '/health_data/top_offenses'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class TopRulesResource(ResourceBase):
    """Operations below ``/health_data/top_rules``."""

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves Top Rules in the system sorted by response count.'
        url = '/health_data/top_rules'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class HealthDataAPI(ResourceBase):
    """Resource-oriented client for the ``health_data`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.security_data_count: SecurityDataCountResource = SecurityDataCountResource(session)
        self.top_offenses: TopOffensesResource = TopOffensesResource(session)
        self.top_rules: TopRulesResource = TopRulesResource(session)

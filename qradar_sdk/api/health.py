"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class MetricsQradarMetricsResource(ResourceBase):
    """Operations below ``/health/metrics/qradar_metrics``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the QRadar health metric identified by ID.'
        url = f'/health/metrics/qradar_metrics/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of QRadar component metrics'
        url = '/health/metrics/qradar_metrics'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the time_resolution and enable field of a QRadar metric identified by metric ID.'
        url = f'/health/metrics/qradar_metrics/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MetricsQradarMetricsGlobalConfigResource(ResourceBase):
    """Operations below ``/health/metrics/qradar_metrics_global_config``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the frequency and enabled fields of all the qradar metrics.'
        url = '/health/metrics/qradar_metrics_global_config'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MetricsSystemMetricsResource(ResourceBase):
    """Operations below ``/health/metrics/system_metrics``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the system health metric identified by metric ID.'
        url = f'/health/metrics/system_metrics/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of system metrics.'
        url = '/health/metrics/system_metrics'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Enable or disable a system metric identified by metric ID'
        url = f'/health/metrics/system_metrics/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MetricsSystemMetricsGlobalConfigResource(ResourceBase):
    """Operations below ``/health/metrics/system_metrics_global_config``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the frequency and enabled value of all the qradar metrics identified by metric_id parameter.'
        url = '/health/metrics/system_metrics_global_config'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MetricsResource(ResourceBase):
    """Operations below ``/metrics``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.qradar_metrics: MetricsQradarMetricsResource = MetricsQradarMetricsResource(session)
        self.qradar_metrics_global_config: MetricsQradarMetricsGlobalConfigResource = MetricsQradarMetricsGlobalConfigResource(session)
        self.system_metrics: MetricsSystemMetricsResource = MetricsSystemMetricsResource(session)
        self.system_metrics_global_config: MetricsSystemMetricsGlobalConfigResource = MetricsSystemMetricsGlobalConfigResource(session)


class HealthAPI(ResourceBase):
    """Resource-oriented client for the ``health`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.metrics: MetricsResource = MetricsResource(session)

"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class EndpointsResource(ResourceBase):
    """Operations below ``/help/endpoints``."""

    def get(self, endpoint_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a single endpoint documentation object.'
        url = f'/help/endpoints/{endpoint_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of endpoint documentation objects that are currently in the system.'
        url = '/help/endpoints'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class ResourcesResource(ResourceBase):
    """Operations below ``/help/resources``."""

    def get(self, resource_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a single resource documentation object.'
        url = f'/help/resources/{resource_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of resource documentation objects currently in the system.'
        url = '/help/resources'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class VersionsResource(ResourceBase):
    """Operations below ``/help/versions``."""

    def get(self, version_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a single version documentation object.'
        url = f'/help/versions/{version_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of version documentation objects currently in the system.'
        url = '/help/versions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class HelpAPI(ResourceBase):
    """Resource-oriented client for the ``help_api`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.endpoints: EndpointsResource = EndpointsResource(session)
        self.resources: ResourcesResource = ResourcesResource(session)
        self.versions: VersionsResource = VersionsResource(session)

"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class ArielCopyProfilesResource(ResourceBase):
    """Operations below ``/disaster_recovery/ariel_copy_profiles``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new Ariel Copy Profile.'
        url = '/disaster_recovery/ariel_copy_profiles'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a Ariel Copy Profile by ID.'
        url = f'/disaster_recovery/ariel_copy_profiles/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a Ariel Copy Profile by ID.'
        url = f'/disaster_recovery/ariel_copy_profiles/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of the Ariel Copy Profiles.'
        url = '/disaster_recovery/ariel_copy_profiles'
        return self._s.get(url, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a Ariel Copy Profile by ID.'
        url = f'/disaster_recovery/ariel_copy_profiles/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class DisasterRecoveryAPI(ResourceBase):
    """Resource-oriented client for the ``disaster_recovery`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.ariel_copy_profiles: ArielCopyProfilesResource = ArielCopyProfilesResource(session)

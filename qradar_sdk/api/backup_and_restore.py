"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class BackupsResource(ResourceBase):
    """Operations below ``/backup_and_restore/backups``."""

    def create(self, body: Optional[Any]=None, backup_type: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Submits a request to the Backup and Restore Engine to create a new backup.'
        url = '/backup_and_restore/backups'
        headers = {'backup_type': backup_type, 'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Sends a request to the Backup and Restore Engine to delete an existing backup.'
        url = f'/backup_and_restore/backups/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an individual backup by ID.'
        url = f'/backup_and_restore/backups/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, sort: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of backups.'
        url = '/backup_and_restore/backups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing backup.'
        url = f'/backup_and_restore/backups/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class HaActionResource(ResourceBase):
    """Operations below ``/backup_and_restore/haAction/{flag}``."""

    def get(self, flag, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Done an individual HA Action as per passing flag.'
        url = f'/backup_and_restore/haAction/{flag}'
        return self._s.get(url, fields=fields, **kwargs)


class RestoresResource(ResourceBase):
    """Operations below ``/backup_and_restore/restores``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a restore object in the PENDING state.'
        url = '/backup_and_restore/restores'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes an individual restore by ID.'
        url = f'/backup_and_restore/restores/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an individual restore by ID.'
        url = f'/backup_and_restore/restores/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, sort: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of restores.'
        url = '/backup_and_restore/restores'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing restore by ID.'
        url = f'/backup_and_restore/restores/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class UpdateiptablesprefileResource(ResourceBase):
    """Operations below ``/backup_and_restore/updateiptablesprefile``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Done an individual HA Action as per passing flag.'
        url = '/backup_and_restore/updateiptablesprefile'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class BackupAndRestoreAPI(ResourceBase):
    """Resource-oriented client for the ``backup_and_restore`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.backups: BackupsResource = BackupsResource(session)
        self.haAction: HaActionResource = HaActionResource(session)
        self.restores: RestoresResource = RestoresResource(session)
        self.updateiptablesprefile: UpdateiptablesprefileResource = UpdateiptablesprefileResource(session)

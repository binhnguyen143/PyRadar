"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class SetBulkUpdateTasksResultsResource(ResourceBase):
    """Operations below ``/reference_data_collections/set_bulk_update_tasks/{task_status_id}/results``."""

    def list(self, task_status_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the results of the Bulk Update task'
        url = f'/reference_data_collections/set_bulk_update_tasks/{task_status_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class SetDependentsTasksResultsResource(ResourceBase):
    """Operations below ``/reference_data_collections/set_dependents_tasks/{task_status_id}/results``."""

    def list(self, task_status_id, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the results of the Get Dependents task'
        url = f'/reference_data_collections/set_dependents_tasks/{task_status_id}/results'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class SetsDependentsResource(ResourceBase):
    """Operations below ``/reference_data_collections/sets/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create an asynchronous task to get the dependents of a Set'
        url = f'/reference_data_collections/sets/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class SetBulkUpdateTasksResource(ResourceBase):
    """Operations below ``/reference_data_collections/set_bulk_update_tasks/{task_status_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: SetBulkUpdateTasksResultsResource = SetBulkUpdateTasksResultsResource(session)

    def get(self, task_status_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the Bulk Update status'
        url = f'/reference_data_collections/set_bulk_update_tasks/{task_status_id}'
        return self._s.get(url, fields=fields, **kwargs)


class SetDeleteTasksResource(ResourceBase):
    """Operations below ``/reference_data_collections/set_delete_tasks/{task_status_id}``."""

    def get(self, task_status_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get results of the asynchronous delete Set task'
        url = f'/reference_data_collections/set_delete_tasks/{task_status_id}'
        return self._s.get(url, fields=fields, **kwargs)


class SetDependentsTasksResource(ResourceBase):
    """Operations below ``/reference_data_collections/set_dependents_tasks/{task_status_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: SetDependentsTasksResultsResource = SetDependentsTasksResultsResource(session)

    def get(self, task_status_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the status of the Get Dependents task'
        url = f'/reference_data_collections/set_dependents_tasks/{task_status_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_status_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancel the Get Dependents request'
        url = f'/reference_data_collections/set_dependents_tasks/{task_status_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class SetEntriesResource(ResourceBase):
    """Operations below ``/reference_data_collections/set_entries``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create an entry within a set'
        url = '/reference_data_collections/set_entries'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Delete a set entry'
        url = f'/reference_data_collections/set_entries/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a set entry'
        url = f'/reference_data_collections/set_entries/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, entry_type: Optional[Any]=None, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a list of set entries which match a search criteria.'
        url = '/reference_data_collections/set_entries'
        params = {'entry_type': entry_type}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a Set Entry given the properties based in the body DTO. Only the notes field\ncan be modified in an existing entry. The source and last_seen timestamp will be updated\nautomatically.'
        url = f'/reference_data_collections/set_entries/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_many(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Perform asynchronous bulk update - series of add and updates'
        url = '/reference_data_collections/set_entries'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.patch(url, headers=headers, json_body=body, **kwargs)


class SetsResource(ResourceBase):
    """Operations below ``/reference_data_collections/sets``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: SetsDependentsResource = SetsDependentsResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a set given the properties based in the body DTO'
        url = '/reference_data_collections/sets'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Delete a set by starting an asynchronous task'
        url = f'/reference_data_collections/sets/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the meta data information for a specific set'
        url = f'/reference_data_collections/sets/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a list of set meta data information based on search criteria'
        url = '/reference_data_collections/sets'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a Set given the properties based in the body DTO'
        url = f'/reference_data_collections/sets/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class ReferenceDataCollectionsAPI(ResourceBase):
    """Resource-oriented client for the ``reference_data_collections`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.set_bulk_update_tasks: SetBulkUpdateTasksResource = SetBulkUpdateTasksResource(session)
        self.set_delete_tasks: SetDeleteTasksResource = SetDeleteTasksResource(session)
        self.set_dependents_tasks: SetDependentsTasksResource = SetDependentsTasksResource(session)
        self.set_entries: SetEntriesResource = SetEntriesResource(session)
        self.sets: SetsResource = SetsResource(session)

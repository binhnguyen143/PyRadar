"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class MapDependentTasksResultsResource(ResourceBase):
    """Operations below ``/reference_data/map_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the reference data map dependent task results.'
        url = f'/reference_data/map_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class MapOfSetsBulkLoadResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets/bulk_load/{namespace}/{name}/{domain_id}``."""

    def update_in_domain(self, namespace, name, domain_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds or updates data in a reference map of sets.'
        url = f'/reference_data/map_of_sets/bulk_load/{namespace}/{name}/{domain_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_name(self, name, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds or updates data in a reference map of sets.'
        url = f'/reference_data/map_of_sets/bulk_load/{name}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MapOfSetsDependentsResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets/{name}/dependents``."""

    def list(self, name, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the reference data map of sets.'
        url = f'/reference_data/map_of_sets/{name}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class MapOfSetsDescriptionResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets/{name}/description``."""

    def create(self, name, namespace: Optional[Any]=None, description: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update description a reference map of sets.'
        url = f'/reference_data/map_of_sets/{name}/description'
        params = {'namespace': namespace, 'description': description}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class MapOfSetsDependentTasksResultsResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the reference data map of sets dependent task results.'
        url = f'/reference_data/map_of_sets_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class MapsBulkLoadResource(ResourceBase):
    """Operations below ``/reference_data/maps/bulk_load/{namespace}/{name}/{domain_id}``."""

    def update_in_domain(self, namespace, name, domain_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds or updates data in a reference map.'
        url = f'/reference_data/maps/bulk_load/{namespace}/{name}/{domain_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_name(self, name, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds or updates data in a reference map.'
        url = f'/reference_data/maps/bulk_load/{name}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MapsDependentsResource(ResourceBase):
    """Operations below ``/reference_data/maps/{name}/dependents``."""

    def list(self, name, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the reference data map.'
        url = f'/reference_data/maps/{name}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class MapsDescriptionResource(ResourceBase):
    """Operations below ``/reference_data/maps/{name}/description``."""

    def create(self, name, namespace: Optional[Any]=None, description: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update description a reference map.'
        url = f'/reference_data/maps/{name}/description'
        params = {'namespace': namespace, 'description': description}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class SetsBulkLoadResource(ResourceBase):
    """Operations below ``/reference_data/sets/bulk_load/{namespace}/{name}/{domain_id}``."""

    def update(self, namespace, name, domain_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update data in a reference set.'
        url = f'/reference_data/sets/bulk_load/{namespace}/{name}/{domain_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class TablesBulkLoadResource(ResourceBase):
    """Operations below ``/reference_data/tables/bulk_load/{namespace}/{name}/{domain_id}``."""

    def update_in_domain(self, namespace, name, domain_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds or updates data in a reference table.'
        url = f'/reference_data/tables/bulk_load/{namespace}/{name}/{domain_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def update_name(self, name, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds or updates data in a reference table.'
        url = f'/reference_data/tables/bulk_load/{name}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class TablesDependentsResource(ResourceBase):
    """Operations below ``/reference_data/tables/{name}/dependents``."""

    def list(self, name, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Find the objects that depend on the Reference Data Tables'
        url = f'/reference_data/tables/{name}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class TablesDescriptionResource(ResourceBase):
    """Operations below ``/reference_data/tables/{name}/description``."""

    def create(self, name, namespace: Optional[Any]=None, description: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update description for a reference table.'
        url = f'/reference_data/tables/{name}/description'
        params = {'namespace': namespace, 'description': description}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class TablesDependentTasksResultsResource(ResourceBase):
    """Operations below ``/reference_data/tables_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the Reference Data Tables Dependent Task Results'
        url = f'/reference_data/tables_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class MapDeleteTasksResource(ResourceBase):
    """Operations below ``/reference_data/map_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete reference data map task status.'
        url = f'/reference_data/map_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class MapDependentTasksResource(ResourceBase):
    """Operations below ``/reference_data/map_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: MapDependentTasksResultsResource = MapDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent reference data map task status.'
        url = f'/reference_data/map_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the dependent reference data map task.'
        url = f'/reference_data/map_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MapOfSetsResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.bulk_load: MapOfSetsBulkLoadResource = MapOfSetsBulkLoadResource(session)
        self.dependents: MapOfSetsDependentsResource = MapOfSetsDependentsResource(session)
        self.description: MapOfSetsDescriptionResource = MapOfSetsDescriptionResource(session)

    def create(self, name: Optional[Any]=None, element_type: Optional[Any]=None, key_label: Optional[Any]=None, value_label: Optional[Any]=None, timeout_type: Optional[Any]=None, time_to_live: Optional[Any]=None, description: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new reference map of sets.'
        url = '/reference_data/map_of_sets'
        params = {'name': name, 'element_type': element_type, 'key_label': key_label, 'value_label': value_label, 'timeout_type': timeout_type, 'time_to_live': time_to_live, 'description': description}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def delete_key(self, name, key, namespace: Optional[Any]=None, value: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Remove a value from a reference map of sets.'
        url = f'/reference_data/map_of_sets/{name}/{key}'
        params = {'namespace': namespace, 'value': value, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def delete_name(self, name, namespace: Optional[Any]=None, purge_only: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Removes a map of sets or purges its contents.'
        url = f'/reference_data/map_of_sets/{name}'
        params = {'namespace': namespace, 'purge_only': purge_only}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def get(self, name, namespace: Optional[Any]=None, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Return the reference map of sets identified by name.'
        url = f'/reference_data/map_of_sets/{name}'
        params = {'namespace': namespace}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of all reference map of sets.'
        url = '/reference_data/map_of_sets'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, name, namespace: Optional[Any]=None, key: Optional[Any]=None, value: Optional[Any]=None, source: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update an element in a reference map of sets.'
        url = f'/reference_data/map_of_sets/{name}'
        params = {'namespace': namespace, 'key': key, 'value': value, 'source': source, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class MapOfSetsDeleteTasksResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete reference data map of sets task status.'
        url = f'/reference_data/map_of_sets_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class MapOfSetsDependentTasksResource(ResourceBase):
    """Operations below ``/reference_data/map_of_sets_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: MapOfSetsDependentTasksResultsResource = MapOfSetsDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent reference data map of sets task status.'
        url = f'/reference_data/map_of_sets_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the dependent reference data map of sets task.'
        url = f'/reference_data/map_of_sets_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class MapsResource(ResourceBase):
    """Operations below ``/reference_data/maps``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.bulk_load: MapsBulkLoadResource = MapsBulkLoadResource(session)
        self.dependents: MapsDependentsResource = MapsDependentsResource(session)
        self.description: MapsDescriptionResource = MapsDescriptionResource(session)

    def create(self, name: Optional[Any]=None, key_label: Optional[Any]=None, value_label: Optional[Any]=None, element_type: Optional[Any]=None, timeout_type: Optional[Any]=None, time_to_live: Optional[Any]=None, description: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new reference map.'
        url = '/reference_data/maps'
        params = {'name': name, 'key_label': key_label, 'value_label': value_label, 'element_type': element_type, 'timeout_type': timeout_type, 'time_to_live': time_to_live, 'description': description}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def delete_key(self, name, key, namespace: Optional[Any]=None, value: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Remove a value from a reference map.'
        url = f'/reference_data/maps/{name}/{key}'
        params = {'namespace': namespace, 'value': value, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def delete_name(self, name, namespace: Optional[Any]=None, purge_only: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Removes a reference map or purges its contents.'
        url = f'/reference_data/maps/{name}'
        params = {'namespace': namespace, 'purge_only': purge_only}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def get(self, name, namespace: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the reference map identified by name.'
        url = f'/reference_data/maps/{name}'
        params = {'namespace': namespace}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of all reference maps.'
        url = '/reference_data/maps'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, name, namespace: Optional[Any]=None, key: Optional[Any]=None, value: Optional[Any]=None, source: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update an element in a reference map.'
        url = f'/reference_data/maps/{name}'
        params = {'namespace': namespace, 'key': key, 'value': value, 'source': source, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class SetsResource(ResourceBase):
    """Operations below ``/reference_data/sets``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.bulk_load: SetsBulkLoadResource = SetsBulkLoadResource(session)

    def create(self, name: Optional[Any]=None, element_type: Optional[Any]=None, timeout_type: Optional[Any]=None, time_to_live: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new reference set.'
        url = '/reference_data/sets'
        params = {'name': name, 'element_type': element_type, 'timeout_type': timeout_type, 'time_to_live': time_to_live}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def delete_name(self, name, namespace: Optional[Any]=None, purge_only: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Removes a reference set or purges its contents.'
        url = f'/reference_data/sets/{name}'
        params = {'namespace': namespace, 'purge_only': purge_only}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def delete_value(self, name, value, namespace: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Remove a value from a reference set.'
        url = f'/reference_data/sets/{name}/{value}'
        params = {'namespace': namespace, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def get(self, name, namespace: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the reference set identified by name.'
        url = f'/reference_data/sets/{name}'
        params = {'namespace': namespace}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of all reference sets.'
        url = '/reference_data/sets'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, name, namespace: Optional[Any]=None, value: Optional[Any]=None, source: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update an element in a reference set.'
        url = f'/reference_data/sets/{name}'
        params = {'namespace': namespace, 'value': value, 'source': source, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class TablesResource(ResourceBase):
    """Operations below ``/reference_data/tables``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.bulk_load: TablesBulkLoadResource = TablesBulkLoadResource(session)
        self.dependents: TablesDependentsResource = TablesDependentsResource(session)
        self.description: TablesDescriptionResource = TablesDescriptionResource(session)

    def create(self, name: Optional[Any]=None, element_type: Optional[Any]=None, outer_key_label: Optional[Any]=None, timeout_type: Optional[Any]=None, time_to_live: Optional[Any]=None, key_name_types: Optional[Any]=None, description: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new reference table.'
        url = '/reference_data/tables'
        params = {'name': name, 'element_type': element_type, 'outer_key_label': outer_key_label, 'timeout_type': timeout_type, 'time_to_live': time_to_live, 'key_name_types': key_name_types, 'description': description}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def delete_inner_key(self, name, outer_key, inner_key, namespace: Optional[Any]=None, value: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Remove a value from a reference table.'
        url = f'/reference_data/tables/{name}/{outer_key}/{inner_key}'
        params = {'namespace': namespace, 'value': value, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def delete_name(self, name, namespace: Optional[Any]=None, purge_only: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Remove a reference table or purge its contents.'
        url = f'/reference_data/tables/{name}'
        params = {'namespace': namespace, 'purge_only': purge_only}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.delete(url, params=params, fields=fields, **kwargs)

    def get(self, name, namespace: Optional[Any]=None, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Return the reference table identified by name.'
        url = f'/reference_data/tables/{name}'
        params = {'namespace': namespace}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of all reference tables.'
        url = '/reference_data/tables'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, name, namespace: Optional[Any]=None, outer_key: Optional[Any]=None, inner_key: Optional[Any]=None, value: Optional[Any]=None, source: Optional[Any]=None, domain_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add or update an element in a reference table.'
        url = f'/reference_data/tables/{name}'
        params = {'namespace': namespace, 'outer_key': outer_key, 'inner_key': inner_key, 'value': value, 'source': source, 'domain_id': domain_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class TablesDeleteTasksResource(ResourceBase):
    """Operations below ``/reference_data/tables_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the delete the Reference Data Tables task status.'
        url = f'/reference_data/tables_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class TablesDependentTasksResource(ResourceBase):
    """Operations below ``/reference_data/tables_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: TablesDependentTasksResultsResource = TablesDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the dependent the Reference Data Tables task status.'
        url = f'/reference_data/tables_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancel the dependent the Reference Data Tables task.'
        url = f'/reference_data/tables_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class ReferenceDataAPI(ResourceBase):
    """Resource-oriented client for the ``reference_data`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.map_delete_tasks: MapDeleteTasksResource = MapDeleteTasksResource(session)
        self.map_dependent_tasks: MapDependentTasksResource = MapDependentTasksResource(session)
        self.map_of_sets: MapOfSetsResource = MapOfSetsResource(session)
        self.map_of_sets_delete_tasks: MapOfSetsDeleteTasksResource = MapOfSetsDeleteTasksResource(session)
        self.map_of_sets_dependent_tasks: MapOfSetsDependentTasksResource = MapOfSetsDependentTasksResource(session)
        self.maps: MapsResource = MapsResource(session)
        self.sets: SetsResource = SetsResource(session)
        self.tables: TablesResource = TablesResource(session)
        self.tables_delete_tasks: TablesDeleteTasksResource = TablesDeleteTasksResource(session)
        self.tables_dependent_tasks: TablesDependentTasksResource = TablesDependentTasksResource(session)

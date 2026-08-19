"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class ProcessorsAqlMetadataResource(ResourceBase):
    """Operations below ``/ariel/processors/aql_metadata``."""

    def create(self, query_expression: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Parses the AQL query expression and returns metadata for this query'
        url = '/ariel/processors/aql_metadata'
        params = {'query_expression': query_expression}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class SavedSearchDependentTasksResultsResource(ResourceBase):
    """Operations below ``/ariel/saved_search_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the Ariel saved search dependent task results.'
        url = f'/ariel/saved_search_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class SavedSearchesDependentsResource(ResourceBase):
    """Operations below ``/ariel/saved_searches/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on the Ariel saved search.'
        url = f'/ariel/saved_searches/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class SearchesMetadataResource(ResourceBase):
    """Operations below ``/ariel/searches/{search_id}/metadata``."""

    def list(self, search_id, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the columns that are defined for a specific Ariel search id.'
        url = f'/ariel/searches/{search_id}/metadata'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class SearchesResultsResource(ResourceBase):
    """Operations below ``/ariel/searches/{search_id}/results``."""

    def list(self, search_id, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves search results in the requested format.'
        url = f'/ariel/searches/{search_id}/results'
        return self._s.get(url, range_header=range_header, **kwargs)


class ValidatorsAqlResource(ResourceBase):
    """Operations below ``/ariel/validators/aql``."""

    def create(self, query_expression: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Validates the AQL query expression.'
        url = '/ariel/validators/aql'
        params = {'query_expression': query_expression}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class DatabasesResource(ResourceBase):
    """Operations below ``/ariel/databases``."""

    def get(self, database_name, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve the columns that are defined for a specific Ariel database.'
        url = f'/ariel/databases/{database_name}'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of available Ariel database names'
        url = '/ariel/databases'
        return self._s.get(url, range_header=range_header, filter_expr=filter, **kwargs)


class EventSavedSearchGroupsResource(ResourceBase):
    """Operations below ``/ariel/event_saved_search_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes an event Ariel saved search group.'
        url = f'/ariel/event_saved_search_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an event Ariel saved search group.'
        url = f'/ariel/event_saved_search_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list the event Ariel saved search groups.'
        url = '/ariel/event_saved_search_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of an event Ariel saved search group.'
        url = f'/ariel/event_saved_search_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowSavedSearchGroupsResource(ResourceBase):
    """Operations below ``/ariel/flow_saved_search_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a flow Ariel saved search group.'
        url = f'/ariel/flow_saved_search_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a flow Ariel saved search group.'
        url = f'/ariel/flow_saved_search_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of flow Ariel saved search groups.'
        url = '/ariel/flow_saved_search_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of a flow Ariel saved search group.'
        url = f'/ariel/flow_saved_search_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowVlansResource(ResourceBase):
    """Operations below ``/ariel/flow_vlans``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new flow VLAN field as specified by input parameters.'
        url = '/ariel/flow_vlans'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        "Deletes a flow VLAN ID with specified enterprise and customer VLAN ID's and removes any associated domain mappings."
        url = f'/ariel/flow_vlans/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a flow VLAN ID object by VLAN ID.'
        url = f'/ariel/flow_vlans/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of available flow VLAN IDs in the Ariel database.'
        url = '/ariel/flow_vlans'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class FunctionsResource(ResourceBase):
    """Operations below ``/ariel/functions``."""

    def get(self, function_name, database: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves AQL Function with given name for a given database.'
        url = f'/ariel/functions/{function_name}'
        params = {'database': database}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, fields=fields, **kwargs)

    def list(self, database: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves AQL Functions for given .'
        url = '/ariel/functions'
        params = {'database': database}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, fields=fields, **kwargs)


class LookupsResource(ResourceBase):
    """Operations below ``/ariel/lookups``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new tagged field lookup.'
        url = '/ariel/lookups'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, name, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes a tagged field lookup with particular name.'
        url = f'/ariel/lookups/{name}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, name, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a tagged field lookup by name.'
        url = f'/ariel/lookups/{name}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all tagged field lookups.'
        url = '/ariel/lookups'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, name, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a tagged field lookup with particular name.'
        url = f'/ariel/lookups/{name}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class ParserKeywordsResource(ResourceBase):
    """Operations below ``/ariel/parser_keywords``."""

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves keywords applicable to AQL Parser.'
        url = '/ariel/parser_keywords'
        return self._s.get(url, fields=fields, **kwargs)


class ProcessorsResource(ResourceBase):
    """Operations below ``/processors``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.aql_metadata: ProcessorsAqlMetadataResource = ProcessorsAqlMetadataResource(session)


class SavedSearchDeleteTasksResource(ResourceBase):
    """Operations below ``/ariel/saved_search_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete the Ariel saved search task status.'
        url = f'/ariel/saved_search_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class SavedSearchDependentTasksResource(ResourceBase):
    """Operations below ``/ariel/saved_search_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: SavedSearchDependentTasksResultsResource = SavedSearchDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent the Ariel saved search task status.'
        url = f'/ariel/saved_search_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the dependent Ariel saved search task.'
        url = f'/ariel/saved_search_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class SavedSearchesResource(ResourceBase):
    """Operations below ``/ariel/saved_searches``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: SavedSearchesDependentsResource = SavedSearchesDependentsResource(session)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes an Ariel saved search. To ensure safe deletion, a dependency check is carried out. The check might take some time. An asynchronous task is started to do this check.'
        url = f'/ariel/saved_searches/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an Ariel saved search.'
        url = f'/ariel/saved_searches/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of Ariel saved searches.'
        url = '/ariel/saved_searches'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the Ariel saved search.'
        url = f'/ariel/saved_searches/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class SearchesResource(ResourceBase):
    """Operations below ``/ariel/searches``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.metadata: SearchesMetadataResource = SearchesMetadataResource(session)
        self.results: SearchesResultsResource = SearchesResultsResource(session)

    def create(self, query_expression: Optional[Any]=None, saved_search_id: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new asynchronous Ariel search.'
        url = '/ariel/searches'
        params = {'query_expression': query_expression, 'saved_search_id': saved_search_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, **kwargs)

    def delete(self, search_id, **kwargs: Any) -> Any:
        'Deletes an Ariel search.'
        url = f'/ariel/searches/{search_id}'
        return self._s.delete(url, **kwargs)

    def get(self, search_id, prefer: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves information about an Ariel search.'
        url = f'/ariel/searches/{search_id}'
        headers = {'Prefer': prefer}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.get(url, headers=headers, **kwargs)

    def list(self, db_name: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of Ariel searches. Search IDs for completed and active searches are returned.'
        url = '/ariel/searches'
        params = {'db_name': db_name}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, filter_expr=filter, **kwargs)

    def update(self, search_id, status: Optional[Any]=None, save_results: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an Ariel search.'
        url = f'/ariel/searches/{search_id}'
        params = {'status': status, 'save_results': save_results}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, **kwargs)


class TaggedfieldcategoriesResource(ResourceBase):
    """Operations below ``/ariel/taggedfieldcategories``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new category for tagged fields. To use this endpoint, you must have System Administrator or Security Admin permissions.'
        url = '/ariel/taggedfieldcategories'
        return self._s.post(url, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Removes the category for tagged fields from the system. To use this endpoint, you must have System Administrator or Security Admin permissions.'
        url = f'/ariel/taggedfieldcategories/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets a category for tagged fields.'
        url = f'/ariel/taggedfieldcategories/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of categories for tagged fields.'
        url = '/ariel/taggedfieldcategories'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a category for tagged fields. To use this endpoint, you must have System Administrator or Security Admin permissions.'
        url = f'/ariel/taggedfieldcategories/{id}'
        return self._s.post(url, json_body=body, **kwargs)


class TaggedfieldsResource(ResourceBase):
    """Operations below ``/ariel/taggedfields``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new tagged field. To use this endpoint, you must have System Administrator or Security Admin permissions.'
        url = '/ariel/taggedfields'
        return self._s.post(url, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Removes a tagged field from the system. To use this endpoint, you must have System Administrator or Security Admin permissions.'
        url = f'/ariel/taggedfields/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual tagged field.'
        url = f'/ariel/taggedfields/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of tagged fields.'
        url = '/ariel/taggedfields'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a tagged field specified by an id. You must have the ADMIN | SAASADMIN capability to use this endpoint.'
        url = f'/ariel/taggedfields/{id}'
        return self._s.post(url, json_body=body, **kwargs)


class ValidatorsResource(ResourceBase):
    """Operations below ``/validators``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.aql: ValidatorsAqlResource = ValidatorsAqlResource(session)


class ArielAPI(ResourceBase):
    """Resource-oriented client for the ``ariel`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.databases: DatabasesResource = DatabasesResource(session)
        self.event_saved_search_groups: EventSavedSearchGroupsResource = EventSavedSearchGroupsResource(session)
        self.flow_saved_search_groups: FlowSavedSearchGroupsResource = FlowSavedSearchGroupsResource(session)
        self.flow_vlans: FlowVlansResource = FlowVlansResource(session)
        self.functions: FunctionsResource = FunctionsResource(session)
        self.lookups: LookupsResource = LookupsResource(session)
        self.parser_keywords: ParserKeywordsResource = ParserKeywordsResource(session)
        self.processors: ProcessorsResource = ProcessorsResource(session)
        self.saved_search_delete_tasks: SavedSearchDeleteTasksResource = SavedSearchDeleteTasksResource(session)
        self.saved_search_dependent_tasks: SavedSearchDependentTasksResource = SavedSearchDependentTasksResource(session)
        self.saved_searches: SavedSearchesResource = SavedSearchesResource(session)
        self.searches: SearchesResource = SearchesResource(session)
        self.taggedfieldcategories: TaggedfieldcategoriesResource = TaggedfieldcategoriesResource(session)
        self.taggedfields: TaggedfieldsResource = TaggedfieldsResource(session)
        self.validators: ValidatorsResource = ValidatorsResource(session)

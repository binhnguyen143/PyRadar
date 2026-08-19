"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class OffenseSavedSearchDependentTasksResultsResource(ResourceBase):
    """Operations below ``/siem/offense_saved_search_dependent_tasks/{task_id}/results``."""

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the offense saved search dependent task results.'
        url = f'/siem/offense_saved_search_dependent_tasks/{task_id}/results'
        return self._s.get(url, fields=fields, **kwargs)


class OffenseSavedSearchesDependentsResource(ResourceBase):
    """Operations below ``/siem/offense_saved_searches/{id}/dependents``."""

    def list(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the objects that depend on an offense saved search.'
        url = f'/siem/offense_saved_searches/{id}/dependents'
        return self._s.get(url, fields=fields, **kwargs)


class OffensesAssignableActorsResource(ResourceBase):
    """Operations below ``/siem/offenses/{offense_id}/assignable_actors``."""

    def list(self, offense_id, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve assignable actors.'
        url = f'/siem/offenses/{offense_id}/assignable_actors'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class OffensesNotesResource(ResourceBase):
    """Operations below ``/siem/offenses/{offense_id}/notes``."""

    def create(self, offense_id, note_text: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a note on an offense.'
        url = f'/siem/offenses/{offense_id}/notes'
        params = {'note_text': note_text}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get(self, offense_id, note_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a note for an offense.'
        url = f'/siem/offenses/{offense_id}/notes/{note_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, offense_id, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of notes for an offense.'
        url = f'/siem/offenses/{offense_id}/notes'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class LocalDestinationAddressesResource(ResourceBase):
    """Operations below ``/siem/local_destination_addresses``."""

    def get(self, local_destination_address_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an offense local destination address.'
        url = f'/siem/local_destination_addresses/{local_destination_address_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list offense local destination addresses currently in the system.'
        url = '/siem/local_destination_addresses'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class OffenseClosingReasonsResource(ResourceBase):
    """Operations below ``/siem/offense_closing_reasons``."""

    def create(self, reason: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create an offense closing reason.'
        url = '/siem/offense_closing_reasons'
        params = {'reason': reason}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get(self, closing_reason_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an offense closing reason.'
        url = f'/siem/offense_closing_reasons/{closing_reason_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, include_reserved: Optional[Any]=None, include_deleted: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of all offense closing reasons.'
        url = '/siem/offense_closing_reasons'
        params = {'include_reserved': include_reserved, 'include_deleted': include_deleted}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class OffenseSavedSearchDeleteTasksResource(ResourceBase):
    """Operations below ``/siem/offense_saved_search_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete the offense saved search task status.'
        url = f'/siem/offense_saved_search_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class OffenseSavedSearchDependentTasksResource(ResourceBase):
    """Operations below ``/siem/offense_saved_search_dependent_tasks/{task_id}``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: OffenseSavedSearchDependentTasksResultsResource = OffenseSavedSearchDependentTasksResultsResource(session)

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the dependent the offense saved search task status.'
        url = f'/siem/offense_saved_search_dependent_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, task_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the dependent the offense saved search task.'
        url = f'/siem/offense_saved_search_dependent_tasks/{task_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class OffenseSavedSearchGroupsResource(ResourceBase):
    """Operations below ``/siem/offense_saved_search_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes an offense saved search group.'
        url = f'/siem/offense_saved_search_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an offense saved search group.'
        url = f'/siem/offense_saved_search_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of offense saved search groups.'
        url = '/siem/offense_saved_search_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of an offense saved search group.'
        url = f'/siem/offense_saved_search_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class OffenseSavedSearchesResource(ResourceBase):
    """Operations below ``/siem/offense_saved_searches``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dependents: OffenseSavedSearchesDependentsResource = OffenseSavedSearchesDependentsResource(session)

    def delete(self, id, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes an offense saved search. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.'
        url = f'/siem/offense_saved_searches/{id}'
        return self._s.delete(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get(self, id, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an offense saved search.'
        url = f'/siem/offense_saved_searches/{id}'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of offense saved searches.'
        url = '/siem/offense_saved_searches'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the offense saved search owner only.'
        url = f'/siem/offense_saved_searches/{id}'
        headers = {'filter': filter, 'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, range_header=range_header, json_body=body, **kwargs)


class OffenseTypesResource(ResourceBase):
    """Operations below ``/siem/offense_types``."""

    def get(self, offense_type_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an offense type structure that describes the properties of an offense type.'
        url = f'/siem/offense_types/{offense_type_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve all the Offense Types'
        url = '/siem/offense_types'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class OffensesResource(ResourceBase):
    """Operations below ``/siem/offenses``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.assignable_actors: OffensesAssignableActorsResource = OffensesAssignableActorsResource(session)
        self.notes: OffensesNotesResource = OffensesNotesResource(session)

    def get(self, offense_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an offense structure that describes  properties of an offense'
        url = f'/siem/offenses/{offense_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of offenses currently in the system.'
        url = '/siem/offenses'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, offense_id, protected: Optional[Any]=None, follow_up: Optional[Any]=None, status: Optional[Any]=None, closing_reason_id: Optional[Any]=None, assigned_to: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update an offense.'
        url = f'/siem/offenses/{offense_id}'
        params = {'protected': protected, 'follow_up': follow_up, 'status': status, 'closing_reason_id': closing_reason_id, 'assigned_to': assigned_to}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class OffensesOcsfResource(ResourceBase):
    """Operations below ``/siem/offenses_ocsf``."""

    def list(self, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of offenses currently in the system in OCSF format.'
        url = '/siem/offenses_ocsf'
        return self._s.get(url, range_header=range_header, **kwargs)


class SourceAddressesResource(ResourceBase):
    """Operations below ``/siem/source_addresses``."""

    def get(self, source_address_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an offense source address.'
        url = f'/siem/source_addresses/{source_address_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list offense source addresses currently in the system.'
        url = '/siem/source_addresses'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class SiemAPI(ResourceBase):
    """Resource-oriented client for the ``siem`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.local_destination_addresses: LocalDestinationAddressesResource = LocalDestinationAddressesResource(session)
        self.offense_closing_reasons: OffenseClosingReasonsResource = OffenseClosingReasonsResource(session)
        self.offense_saved_search_delete_tasks: OffenseSavedSearchDeleteTasksResource = OffenseSavedSearchDeleteTasksResource(session)
        self.offense_saved_search_dependent_tasks: OffenseSavedSearchDependentTasksResource = OffenseSavedSearchDependentTasksResource(session)
        self.offense_saved_search_groups: OffenseSavedSearchGroupsResource = OffenseSavedSearchGroupsResource(session)
        self.offense_saved_searches: OffenseSavedSearchesResource = OffenseSavedSearchesResource(session)
        self.offense_types: OffenseTypesResource = OffenseTypesResource(session)
        self.offenses: OffensesResource = OffensesResource(session)
        self.offenses_ocsf: OffensesOcsfResource = OffensesOcsfResource(session)
        self.source_addresses: SourceAddressesResource = SourceAddressesResource(session)

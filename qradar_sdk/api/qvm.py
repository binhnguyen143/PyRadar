"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class SavedSearchesVulnInstancesResultsAssetsResource(ResourceBase):
    """Operations below ``/qvm/saved_searches/vuln_instances/{task_id}/results/assets``."""

    def list(self, task_id, filter: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Lists the Vulnerability Instances assets that are returned from the vulnerability instance saved search.'
        url = f'/qvm/saved_searches/vuln_instances/{task_id}/results/assets'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class SavedSearchesVulnInstancesResultsVulnInstancesResource(ResourceBase):
    """Operations below ``/qvm/saved_searches/vuln_instances/{task_id}/results/vuln_instances``."""

    def list(self, task_id, filter: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Lists the Vulnerability Instances returned from a vulnerability instance saved search.'
        url = f'/qvm/saved_searches/vuln_instances/{task_id}/results/vuln_instances'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class SavedSearchesVulnInstancesResultsVulnerabilitiesResource(ResourceBase):
    """Operations below ``/qvm/saved_searches/vuln_instances/{task_id}/results/vulnerabilities``."""

    def list(self, task_id, filter: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'List the Vulnerability Instances vulnerabilities returned from the saved search.'
        url = f'/qvm/saved_searches/vuln_instances/{task_id}/results/vulnerabilities'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class SavedSearchesVulnInstancesResultsResource(ResourceBase):
    """Operations below ``/saved_searches/vuln_instances/results``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.assets: SavedSearchesVulnInstancesResultsAssetsResource = SavedSearchesVulnInstancesResultsAssetsResource(session)
        self.vuln_instances: SavedSearchesVulnInstancesResultsVulnInstancesResource = SavedSearchesVulnInstancesResultsVulnInstancesResource(session)
        self.vulnerabilities: SavedSearchesVulnInstancesResultsVulnerabilitiesResource = SavedSearchesVulnInstancesResultsVulnerabilitiesResource(session)


class SavedSearchesVulnInstancesStatusResource(ResourceBase):
    """Operations below ``/qvm/saved_searches/vuln_instances/{task_id}/status``."""

    def create(self, task_id, status: Optional[Any]=None, retention_period_in_days: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the status of a vulnerability instance saved search.'
        url = f'/qvm/saved_searches/vuln_instances/{task_id}/status'
        params = {'status': status, 'retention_period_in_days': retention_period_in_days}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def list(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the current status of a vulnerability instance search that was initiated.'
        url = f'/qvm/saved_searches/vuln_instances/{task_id}/status'
        return self._s.get(url, fields=fields, **kwargs)


class SavedSearchesVulnInstancesResource(ResourceBase):
    """Operations below ``/qvm/saved_searches/{saved_search_id}/vuln_instances``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: SavedSearchesVulnInstancesResultsResource = SavedSearchesVulnInstancesResultsResource(session)
        self.status: SavedSearchesVulnInstancesStatusResource = SavedSearchesVulnInstancesStatusResource(session)

    def list(self, saved_search_id, filter: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates the Vulnerability Instances search. This search will return a maximum of 100,000 results.'
        url = f'/qvm/saved_searches/{saved_search_id}/vuln_instances'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class TicketsAssignResource(ResourceBase):
    """Operations below ``/qvm/tickets/assign``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update the remediation ticket for the assigned vulnerability'
        url = '/qvm/tickets/assign'
        return self._s.post(url, json_body=body, **kwargs)


class AssetsResource(ResourceBase):
    """Operations below ``/qvm/assets``."""

    def list(self, saved_search_id: Optional[Any]=None, saved_search_name: Optional[Any]=None, filters: Optional[Any]=None, **kwargs: Any) -> Any:
        'List the assets with discovered vulnerabilities present in the asset model.  The response will contain all available RESTful resources'
        url = '/qvm/assets'
        params = {'savedSearchId': saved_search_id, 'savedSearchName': saved_search_name, 'filters': filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)


class FiltersResource(ResourceBase):
    """Operations below ``/qvm/filters``."""

    def list(self, **kwargs: Any) -> Any:
        'Get a list of the allowable filters that can be used or applied against the:'
        url = '/qvm/filters'
        return self._s.get(url, **kwargs)


class NetworkResource(ResourceBase):
    """Operations below ``/qvm/network``."""

    def list(self, saved_search_id: Optional[Any]=None, saved_search_name: Optional[Any]=None, filters: Optional[Any]=None, **kwargs: Any) -> Any:
        'List the networks present in the asset model with vulnerabilities present.  The response will contain all available RESTful resources'
        url = '/qvm/network'
        params = {'savedSearchId': saved_search_id, 'savedSearchName': saved_search_name, 'filters': filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)


class OpenservicesResource(ResourceBase):
    """Operations below ``/qvm/openservices``."""

    def list(self, saved_search_id: Optional[Any]=None, saved_search_name: Optional[Any]=None, filters: Optional[Any]=None, **kwargs: Any) -> Any:
        'List the openservices present in the asset model with vulnerabilities present.  The response will contain all available RESTful resources'
        url = '/qvm/openservices'
        params = {'savedSearchId': saved_search_id, 'savedSearchName': saved_search_name, 'filters': filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)


class SavedSearchGroupsResource(ResourceBase):
    """Operations below ``/qvm/saved_search_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a vulnerability saved search group.'
        url = f'/qvm/saved_search_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a vulnerability saved search group.'
        url = f'/qvm/saved_search_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, filter: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of vulnerability saved search groups.'
        url = '/qvm/saved_search_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of an vulnerability saved search group.'
        url = f'/qvm/saved_search_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class SavedSearchesResource(ResourceBase):
    """Operations below ``/qvm/saved_searches``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.vuln_instances: SavedSearchesVulnInstancesResource = SavedSearchesVulnInstancesResource(session)

    def delete(self, saved_search_id, **kwargs: Any) -> Any:
        'Deletes a vulnerability saved search.'
        url = f'/qvm/saved_searches/{saved_search_id}'
        return self._s.delete(url, **kwargs)

    def get(self, saved_search_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a vulnerability instance saved search.'
        url = f'/qvm/saved_searches/{saved_search_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, filter: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of  vulnerability instance saved searches.'
        url = '/qvm/saved_searches'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, saved_search_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the vulnerability saved search owner only.'
        url = f'/qvm/saved_searches/{saved_search_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class TicketsResource(ResourceBase):
    """Operations below ``/tickets``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.assign: TicketsAssignResource = TicketsAssignResource(session)


class VulnsResource(ResourceBase):
    """Operations below ``/qvm/vulns``."""

    def list(self, saved_search_id: Optional[Any]=None, saved_search_name: Optional[Any]=None, filters: Optional[Any]=None, **kwargs: Any) -> Any:
        'List the Vulnerabilities present in the asset model.  The response will contain all available RESTful resources'
        url = '/qvm/vulns'
        params = {'savedSearchId': saved_search_id, 'savedSearchName': saved_search_name, 'filters': filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)


class QvmAPI(ResourceBase):
    """Resource-oriented client for the ``qvm`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.assets: AssetsResource = AssetsResource(session)
        self.filters: FiltersResource = FiltersResource(session)
        self.network: NetworkResource = NetworkResource(session)
        self.openservices: OpenservicesResource = OpenservicesResource(session)
        self.saved_search_groups: SavedSearchGroupsResource = SavedSearchGroupsResource(session)
        self.saved_searches: SavedSearchesResource = SavedSearchesResource(session)
        self.tickets: TicketsResource = TicketsResource(session)
        self.vulns: VulnsResource = VulnsResource(session)

"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class ModelGroupsResource(ResourceBase):
    """Operations below ``/qrm/model_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a model group.'
        url = f'/qrm/model_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a model group.'
        url = f'/qrm/model_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of model groups.'
        url = '/qrm/model_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of a model group.'
        url = f'/qrm/model_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class QrmSavedSearchGroupsResource(ResourceBase):
    """Operations below ``/qrm/qrm_saved_search_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a QRM saved search group.'
        url = f'/qrm/qrm_saved_search_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a QRM saved search group.'
        url = f'/qrm/qrm_saved_search_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of QRM saved search groups.'
        url = '/qrm/qrm_saved_search_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of a QRM saved search group.'
        url = f'/qrm/qrm_saved_search_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class QuestionGroupsResource(ResourceBase):
    """Operations below ``/qrm/question_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a question group.'
        url = f'/qrm/question_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a question group.'
        url = f'/qrm/question_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of question groups.'
        url = '/qrm/question_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of a question group.'
        url = f'/qrm/question_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class SimulationGroupsResource(ResourceBase):
    """Operations below ``/qrm/simulation_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a simulation group.'
        url = f'/qrm/simulation_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a simulation group.'
        url = f'/qrm/simulation_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a of list the simulation groups.'
        url = '/qrm/simulation_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of a simulation group.'
        url = f'/qrm/simulation_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class TopologySavedSearchGroupsResource(ResourceBase):
    """Operations below ``/qrm/topology_saved_search_groups``."""

    def delete(self, group_id, **kwargs: Any) -> Any:
        'Deletes a topology saved search group.'
        url = f'/qrm/topology_saved_search_groups/{group_id}'
        return self._s.delete(url, **kwargs)

    def get(self, group_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a topology saved search group.'
        url = f'/qrm/topology_saved_search_groups/{group_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of topology saved search groups.'
        url = '/qrm/topology_saved_search_groups'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, group_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the owner of an topology saved search group.'
        url = f'/qrm/topology_saved_search_groups/{group_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class QrmAPI(ResourceBase):
    """Resource-oriented client for the ``qrm`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.model_groups: ModelGroupsResource = ModelGroupsResource(session)
        self.qrm_saved_search_groups: QrmSavedSearchGroupsResource = QrmSavedSearchGroupsResource(session)
        self.question_groups: QuestionGroupsResource = QuestionGroupsResource(session)
        self.simulation_groups: SimulationGroupsResource = SimulationGroupsResource(session)
        self.topology_saved_search_groups: TopologySavedSearchGroupsResource = TopologySavedSearchGroupsResource(session)

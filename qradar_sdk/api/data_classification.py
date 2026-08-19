"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class DsmEventMappingsResource(ResourceBase):
    """Operations below ``/data_classification/dsm_event_mappings``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new custom DSM event mapping.'
        url = '/data_classification/dsm_event_mappings'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, dsm_event_mapping_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a DSM event mapping based on the supplied DSM event mapping ID.'
        url = f'/data_classification/dsm_event_mappings/{dsm_event_mapping_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a list of DSM event mappings.'
        url = '/data_classification/dsm_event_mappings'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, dsm_event_mapping_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing custom DSM event mapping.'
        url = f'/data_classification/dsm_event_mappings/{dsm_event_mapping_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class HighLevelCategoriesResource(ResourceBase):
    """Operations below ``/data_classification/high_level_categories``."""

    def get(self, high_level_category_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a high level category based on the supplied high level category ID.'
        url = f'/data_classification/high_level_categories/{high_level_category_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of high level categories.'
        url = '/data_classification/high_level_categories'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class LowLevelCategoriesResource(ResourceBase):
    """Operations below ``/data_classification/low_level_categories``."""

    def get(self, low_level_category_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a low level category based on the supplied low level category ID.'
        url = f'/data_classification/low_level_categories/{low_level_category_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of low level categories.'
        url = '/data_classification/low_level_categories'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class QidRecordsResource(ResourceBase):
    """Operations below ``/data_classification/qid_records``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new QID record.'
        url = '/data_classification/qid_records'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, qid_record_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a QID record that is based on the supplied qid_record_id.'
        url = f'/data_classification/qid_records/{qid_record_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of QID records.'
        url = '/data_classification/qid_records'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, qid_record_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing QID record.'
        url = f'/data_classification/qid_records/{qid_record_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class DataClassificationAPI(ResourceBase):
    """Resource-oriented client for the ``data_classification`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dsm_event_mappings: DsmEventMappingsResource = DsmEventMappingsResource(session)
        self.high_level_categories: HighLevelCategoriesResource = HighLevelCategoriesResource(session)
        self.low_level_categories: LowLevelCategoriesResource = LowLevelCategoriesResource(session)
        self.qid_records: QidRecordsResource = QidRecordsResource(session)

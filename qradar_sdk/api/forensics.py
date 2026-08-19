"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class CaptureRecoveriesResource(ResourceBase):
    """Operations below ``/forensics/capture/recoveries``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new capture recovery.'
        url = '/forensics/capture/recoveries'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a recovery based on the supplied ID.'
        url = f'/forensics/capture/recoveries/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, filter: Optional[Any]=None, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of capture recoveries.'
        url = '/forensics/capture/recoveries'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class CaptureRecoveryTasksResource(ResourceBase):
    """Operations below ``/forensics/capture/recovery_tasks``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a recovery task based on the supplied ID.'
        url = f'/forensics/capture/recovery_tasks/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, filter: Optional[Any]=None, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of recovery tasks.'
        url = '/forensics/capture/recovery_tasks'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class CaseManagementCaseCreateTasksResource(ResourceBase):
    """Operations below ``/forensics/case_management/case_create_tasks/{id}``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a case create task based on the supplied id.'
        url = f'/forensics/case_management/case_create_tasks/{id}'
        return self._s.get(url, fields=fields, **kwargs)


class CaseManagementCasesResource(ResourceBase):
    """Operations below ``/forensics/case_management/cases``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new case.'
        url = '/forensics/case_management/cases'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a case based on the supplied id.'
        url = f'/forensics/case_management/cases/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, filter: Optional[Any]=None, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of cases.'
        url = '/forensics/case_management/cases'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class CaptureResource(ResourceBase):
    """Operations below ``/capture``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.recoveries: CaptureRecoveriesResource = CaptureRecoveriesResource(session)
        self.recovery_tasks: CaptureRecoveryTasksResource = CaptureRecoveryTasksResource(session)


class CaseManagementResource(ResourceBase):
    """Operations below ``/case_management``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.case_create_tasks: CaseManagementCaseCreateTasksResource = CaseManagementCaseCreateTasksResource(session)
        self.cases: CaseManagementCasesResource = CaseManagementCasesResource(session)


class ForensicsAPI(ResourceBase):
    """Resource-oriented client for the ``forensics`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.capture: CaptureResource = CaptureResource(session)
        self.case_management: CaseManagementResource = CaseManagementResource(session)

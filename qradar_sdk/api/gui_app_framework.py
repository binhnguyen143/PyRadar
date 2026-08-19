"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class ApplicationCreationTaskAuthResource(ResourceBase):
    """Operations below ``/gui_app_framework/application_creation_task/{application_id}/auth``."""

    def create(self, application_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Responds to an authorisation request for an application install.'
        url = f'/gui_app_framework/application_creation_task/{application_id}/auth'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, application_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an authorisation request for an application install.'
        url = f'/gui_app_framework/application_creation_task/{application_id}/auth'
        return self._s.get(url, fields=fields, **kwargs)


class ApplicationDefinitionsUserRoleIdResource(ResourceBase):
    """Operations below ``/gui_app_framework/application_definitions/{application_definition_id}/user_role_id``."""

    def delete(self, application_definition_id, user_role_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Call DELETE /gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def list(self, application_definition_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve all user roles associated with an application definition.'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}/user_role_id'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, application_definition_id, user_role_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Add a user role to the list associated with an application definition'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}'
        return self._s.post(url, fields=fields, **kwargs)


class ApplicationsHostTypeResource(ResourceBase):
    """Operations below ``/gui_app_framework/applications/{application_id}/host_type``."""

    def get(self, application_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve a host type.'
        url = f'/gui_app_framework/applications/{application_id}/host_type'
        return self._s.get(url, fields=fields, **kwargs)


class ApplicationCreationTaskResource(ResourceBase):
    """Operations below ``/gui_app_framework/application_creation_task``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.auth: ApplicationCreationTaskAuthResource = ApplicationCreationTaskAuthResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Installs a new application.'
        url = '/gui_app_framework/application_creation_task'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get(self, application_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the status of an application install.'
        url = f'/gui_app_framework/application_creation_task/{application_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the status of all application installs.'
        url = '/gui_app_framework/application_creation_task'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, application_id, status: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels an application install.'
        url = f'/gui_app_framework/application_creation_task/{application_id}'
        params = {'status': status}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class ApplicationDefinitionsResource(ResourceBase):
    """Operations below ``/gui_app_framework/application_definitions``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.user_role_id: ApplicationDefinitionsUserRoleIdResource = ApplicationDefinitionsUserRoleIdResource(session)

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Installs a new application definition.'
        url = '/gui_app_framework/application_definitions'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, application_definition_id, **kwargs: Any) -> Any:
        'Deletes an application definition and its associated instances.'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}'
        return self._s.delete(url, **kwargs)

    def get(self, application_definition_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an application definition.'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve list of application definitions.'
        url = '/gui_app_framework/application_definitions'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def replace(self, application_definition_id, body: Optional[Any]=None, include_stopped_application: Optional[Any]=None, use_local_zip: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Upgrades an application definition.'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}'
        headers = {'include_stopped_application': include_stopped_application, 'use_local_zip': use_local_zip, 'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)

    def update(self, application_definition_id, status: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Cancels the creation or upgrade of an application definition'
        url = f'/gui_app_framework/application_definitions/{application_definition_id}'
        params = {'status': status}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class ApplicationsResource(ResourceBase):
    """Operations below ``/gui_app_framework/applications``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.host_type: ApplicationsHostTypeResource = ApplicationsHostTypeResource(session)

    def create(self, application_definition_id: Optional[Any]=None, memory: Optional[Any]=None, security_profile_id: Optional[Any]=None, force_multitenancy_safe: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new application instance.'
        url = '/gui_app_framework/applications'
        params = {'application_definition_id': application_definition_id, 'memory': memory, 'security_profile_id': security_profile_id, 'force_multitenancy_safe': force_multitenancy_safe}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def delete(self, application_id, **kwargs: Any) -> Any:
        'Deletes an application instance.'
        url = f'/gui_app_framework/applications/{application_id}'
        return self._s.delete(url, **kwargs)

    def get(self, application_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve an installed application.'
        url = f'/gui_app_framework/applications/{application_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, fields: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve list of applications.'
        url = '/gui_app_framework/applications'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def replace(self, application_id, body: Optional[Any]=None, use_local_zip: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Upgrades an application.'
        url = f'/gui_app_framework/applications/{application_id}'
        headers = {'use_local_zip': use_local_zip, 'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)

    def update(self, application_id, status: Optional[Any]=None, memory: Optional[Any]=None, oauth_user_id: Optional[Any]=None, security_profile_id: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an application.'
        url = f'/gui_app_framework/applications/{application_id}'
        params = {'status': status, 'memory': memory, 'oauth_user_id': oauth_user_id, 'security_profile_id': security_profile_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)


class NamedServicesResource(ResourceBase):
    """Operations below ``/gui_app_framework/named_services``."""

    def get(self, uuid, **kwargs: Any) -> Any:
        'Retrieves a named service.'
        url = f'/gui_app_framework/named_services/{uuid}'
        return self._s.get(url, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        'Retrieves all named services.'
        url = '/gui_app_framework/named_services'
        return self._s.get(url, **kwargs)


class GuiAppFrameworkAPI(ResourceBase):
    """Resource-oriented client for the ``gui_app_framework`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.application_creation_task: ApplicationCreationTaskResource = ApplicationCreationTaskResource(session)
        self.application_definitions: ApplicationDefinitionsResource = ApplicationDefinitionsResource(session)
        self.applications: ApplicationsResource = ApplicationsResource(session)
        self.named_services: NamedServicesResource = NamedServicesResource(session)

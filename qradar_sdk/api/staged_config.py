"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class DeploymentHostsTunnelsResource(ResourceBase):
    """Operations below ``/staged_config/deployment/hosts/{id}/tunnels``."""

    def list(self, id, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of tunnels for the host.'
        url = f'/staged_config/deployment/hosts/{id}/tunnels'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, name, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a tunnel by host ID and tunnel name.  The update is in the staged configuration and a deployment is needed.\n\nThe only editable field is reverse_source. The default is false and can be set to true.'
        url = f'/staged_config/deployment/hosts/{id}/tunnels/{name}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class FlowApplicationsActiveApplicationsResource(ResourceBase):
    """Operations below ``/staged_config/flow/applications/active_applications``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a new active flow application in the staged configuration area.'
        url = '/staged_config/flow/applications/active_applications'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Removes the active flow application from the staged configuration area, as specified by the application ID.'
        url = f'/staged_config/flow/applications/active_applications/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets an individual active flow application that is in the staged configuration area, as specified by the application ID.\n\nActive applications are flow applications that are currently in-use by the system. Active applications that are in the staged configuration area are not yet deployed.\nChanges or modifications to a flow application should always be made to the active applications list. Do not update the default applications.\n\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = f'/staged_config/flow/applications/active_applications/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of active flow applications that are in the staged configuration area.'
        url = '/staged_config/flow/applications/active_applications'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an active flow application that is in the staged configuration area, as specified by the application ID.'
        url = f'/staged_config/flow/applications/active_applications/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AccessSecurityProfilesResource(ResourceBase):
    """Operations below ``/staged_config/access/security_profiles``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a staged security profile by ID.'
        url = f'/staged_config/access/security_profiles/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, tenant_id: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the list of staged security profiles available in the system.'
        url = '/staged_config/access/security_profiles'
        params = {'tenant_id': tenant_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class AccessUserDeleteTasksResource(ResourceBase):
    """Operations below ``/staged_config/access/user_delete_tasks/{task_id}``."""

    def get(self, task_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the delete user task status.'
        url = f'/staged_config/access/user_delete_tasks/{task_id}'
        return self._s.get(url, fields=fields, **kwargs)


class AccessUserRolesResource(ResourceBase):
    """Operations below ``/staged_config/access/user_roles``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get a staged user role by ID.'
        url = f'/staged_config/access/user_roles/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, contains: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Get the list of staged user roles available in the system.'
        url = '/staged_config/access/user_roles'
        params = {'contains': contains}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class AccessUsersResource(ResourceBase):
    """Operations below ``/staged_config/access/users``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Create a staged user.'
        url = '/staged_config/access/users'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Deletes a user from staging. To ensure safe deletion, dependencies are checked. This might take some time. An asynchronous task is started to do this check.'
        url = f'/staged_config/access/users/{id}'
        return self._s.delete(url, fields=fields, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a staged user.'
        url = f'/staged_config/access/users/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, sort: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all staged users.'
        url = '/staged_config/access/users'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a staged user.'
        url = f'/staged_config/access/users/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class BackupAndRestoreScheduledBackupConfigurationsResource(ResourceBase):
    """Operations below ``/staged_config/backup_and_restore/scheduled_backup_configurations``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a Staged Backup Configuration by ID.'
        url = f'/staged_config/backup_and_restore/scheduled_backup_configurations/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of the Staged Backup Configurations.'
        url = '/staged_config/backup_and_restore/scheduled_backup_configurations'
        return self._s.get(url, fields=fields, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates a Staged Backup Configuration.'
        url = f'/staged_config/backup_and_restore/scheduled_backup_configurations/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class CertificatesCertificateSigningRequestResource(ResourceBase):
    """Operations below ``/staged_config/certificates/certificate_signing_request``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new Certificate Signing Request (CSR) file. A private key is generated and used to create the CSR file. The private key is kept secure on the Console. Use the GET call to download the CSR file.\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = '/staged_config/certificates/certificate_signing_request'
        return self._s.post(url, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes the Certificate Signing Request (CSR) resource.'
        url = f'/staged_config/certificates/certificate_signing_request/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, **kwargs: Any) -> Any:
        'Download the generated Certificate Signing Request (CSR) file.'
        url = f'/staged_config/certificates/certificate_signing_request/{id}'
        return self._s.get(url, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        'List of Certificate Signing Request (CSR) metadata that is stored in the\ncertificate_signing_request database table.'
        url = '/staged_config/certificates/certificate_signing_request'
        return self._s.get(url, **kwargs)


class CertificatesEndCertificatesResource(ResourceBase):
    """Operations below ``/staged_config/certificates/end_certificates``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Use this endpoint to create a new certificate resource on the Console.\nThis endpoint creates a keystore file that contains the supplied security objects.\nYou must have System Administrator or Security Administrator permissions to use this endpoint. An administrator must deploy the configuration change.'
        url = '/staged_config/certificates/end_certificates'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        "Marks the certificate for deletion, but doesn't immediately remove it. After this\nrequest, the value of the certificate's Status field is change to DELETE_PENDING. To remove\nthe certificate from the console and managed hosts, you must deploy the change after invoking this\nAPI. You must have System Administrator or Security Administrator permissions to use this endpoint."
        url = f'/staged_config/certificates/end_certificates/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets information about a specific certificate, as specified by the certificate ID.\nYou must have System Administrator, Security Administrator, Manage Log Sources, or WinCollect permissions to use this endpoint.'
        url = f'/staged_config/certificates/end_certificates/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of uploaded certificates from the staged area.\nYou must have System Administrator, Security Administrator, Manage Log Sources, or WinCollect permissions to use this endpoint.'
        url = '/staged_config/certificates/end_certificates'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Use this endpoint to update an existing certificate resource.\nThe ID that is specified in the URL path indicates the target resource to be modified. The parameter to be modified on the target resource is included in the\n body as a JSON object, with the new data value. The endpoint updates only the specified parameters. Empty values or missing parameters are ignored.\nYou must have System Administrator or Security Administrator permissions to use this endpoint. After the certificate resource is updated, an administrator must deploy the updated Keystore file.'
        url = f'/staged_config/certificates/end_certificates/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class CertificatesRootCertificatesResource(ResourceBase):
    """Operations below ``/staged_config/certificates/root_certificates``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Uploads a new single root certificate to the staged configuration folder on the Console.  \nThis API enables the deployment of new root certificates to managed hosts, which enables the TLS handshake between a managed host and a destination device.\nThe following steps are required to push the root certificate to the managed host:'
        url = '/staged_config/certificates/root_certificates'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, id, **kwargs: Any) -> Any:
        'Deletes a certificate from the staged configuration folder on the Console, but does not\nremove the certificate from the managed host. To remove the certificate from managed hosts, invoke\nthis API and then deploy the configuration changes. You must have System Administrator permissions\nto use this endpoint.'
        url = f'/staged_config/certificates/root_certificates/{id}'
        return self._s.delete(url, **kwargs)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets details of an uploaded root certificate, as specified by the ID.\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = f'/staged_config/certificates/root_certificates/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the list of all of the root certificates that are uploaded.\nYou must have System Administrator or Security Administrator permissions to use this endpoint.'
        url = '/staged_config/certificates/root_certificates'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class DeploymentHostsResource(ResourceBase):
    """Operations below ``/staged_config/deployment/hosts``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.tunnels: DeploymentHostsTunnelsResource = DeploymentHostsTunnelsResource(session)

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a staged host by ID. The Host object has the following fields:'
        url = f'/staged_config/deployment/hosts/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, filter: Optional[Any]=None, range_header: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all staged hosts.'
        url = '/staged_config/deployment/hosts'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class FlowApplicationsResource(ResourceBase):
    """Operations below ``/flow/applications``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.active_applications: FlowApplicationsActiveApplicationsResource = FlowApplicationsActiveApplicationsResource(session)


class AccessResource(ResourceBase):
    """Operations below ``/access``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.security_profiles: AccessSecurityProfilesResource = AccessSecurityProfilesResource(session)
        self.user_delete_tasks: AccessUserDeleteTasksResource = AccessUserDeleteTasksResource(session)
        self.user_roles: AccessUserRolesResource = AccessUserRolesResource(session)
        self.users: AccessUsersResource = AccessUsersResource(session)


class BackupAndRestoreResource(ResourceBase):
    """Operations below ``/backup_and_restore``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.scheduled_backup_configurations: BackupAndRestoreScheduledBackupConfigurationsResource = BackupAndRestoreScheduledBackupConfigurationsResource(session)


class CertificatesResource(ResourceBase):
    """Operations below ``/certificates``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.certificate_signing_request: CertificatesCertificateSigningRequestResource = CertificatesCertificateSigningRequestResource(session)
        self.end_certificates: CertificatesEndCertificatesResource = CertificatesEndCertificatesResource(session)
        self.root_certificates: CertificatesRootCertificatesResource = CertificatesRootCertificatesResource(session)


class DeployStatusResource(ResourceBase):
    """Operations below ``/staged_config/deploy_status``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Executes a deploy.'
        url = '/staged_config/deploy_status'
        return self._s.post(url, json_body=body, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        'Retrieves the status of a deploy in progress.'
        url = '/staged_config/deploy_status'
        return self._s.get(url, **kwargs)


class DeploymentResource(ResourceBase):
    """Operations below ``/deployment``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.hosts: DeploymentHostsResource = DeploymentHostsResource(session)


class FlowResource(ResourceBase):
    """Operations below ``/flow``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.applications: FlowApplicationsResource = FlowApplicationsResource(session)


class RemoteNetworksResource(ResourceBase):
    """Operations below ``/staged_config/remote_networks``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds a new staged remote network.'
        url = '/staged_config/remote_networks'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, network_id, **kwargs: Any) -> Any:
        'Deletes an existing staged remote network.'
        url = f'/staged_config/remote_networks/{network_id}'
        return self._s.delete(url, **kwargs)

    def get(self, network_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a staged remote network by ID.'
        url = f'/staged_config/remote_networks/{network_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of staged remote networks.'
        url = '/staged_config/remote_networks'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, network_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing staged remote network.'
        url = f'/staged_config/remote_networks/{network_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class RemoteServicesResource(ResourceBase):
    """Operations below ``/staged_config/remote_services``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Adds a staged remote service.'
        url = '/staged_config/remote_services'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete(self, service_id, **kwargs: Any) -> Any:
        'Deletes an existing staged remote service.'
        url = f'/staged_config/remote_services/{service_id}'
        return self._s.delete(url, **kwargs)

    def get(self, service_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a staged remote service by ID.'
        url = f'/staged_config/remote_services/{service_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of staged remote services.'
        url = '/staged_config/remote_services'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, service_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing staged remote service.'
        url = f'/staged_config/remote_services/{service_id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class YaraRulesResource(ResourceBase):
    """Operations below ``/staged_config/yara_rules``."""

    def delete(self, **kwargs: Any) -> Any:
        'Deletes all Yara rules from the QRadar system.'
        url = '/staged_config/yara_rules'
        return self._s.delete(url, **kwargs)

    def replace(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Uploads the supplied Yara rule file to the QRadar system.\nIf the provided Yara file is empty - all rules are deleted from the system.'
        url = '/staged_config/yara_rules'
        return self._s.put(url, json_body=body, **kwargs)


class StagedConfigAPI(ResourceBase):
    """Resource-oriented client for the ``staged_config`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.access: AccessResource = AccessResource(session)
        self.backup_and_restore: BackupAndRestoreResource = BackupAndRestoreResource(session)
        self.certificates: CertificatesResource = CertificatesResource(session)
        self.deploy_status: DeployStatusResource = DeployStatusResource(session)
        self.deployment: DeploymentResource = DeploymentResource(session)
        self.flow: FlowResource = FlowResource(session)
        self.remote_networks: RemoteNetworksResource = RemoteNetworksResource(session)
        self.remote_services: RemoteServicesResource = RemoteServicesResource(session)
        self.yara_rules: YaraRulesResource = YaraRulesResource(session)

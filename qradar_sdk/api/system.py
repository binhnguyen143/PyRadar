"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class ServersNetworkInterfacesBondedResource(ResourceBase):
    """Operations below ``/system/servers/{server_id}/network_interfaces/bonded``."""

    def create(self, server_id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new bonded network interface.'
        url = f'/system/servers/{server_id}/network_interfaces/bonded'
        return self._s.post(url, json_body=body, **kwargs)

    def delete(self, server_id, device_name, **kwargs: Any) -> Any:
        'Removes a bonded network interface.'
        url = f'/system/servers/{server_id}/network_interfaces/bonded/{device_name}'
        return self._s.delete(url, **kwargs)

    def list(self, server_id, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of the bonded network interfaces based on the supplied server ID.'
        url = f'/system/servers/{server_id}/network_interfaces/bonded'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, server_id, device_name, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing bonded network interface.'
        url = f'/system/servers/{server_id}/network_interfaces/bonded/{device_name}'
        return self._s.post(url, json_body=body, **kwargs)


class ServersNetworkInterfacesEthernetResource(ResourceBase):
    """Operations below ``/system/servers/{server_id}/network_interfaces/ethernet``."""

    def list(self, server_id, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of the ethernet network interfaces based on the supplied server ID.'
        url = f'/system/servers/{server_id}/network_interfaces/ethernet'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, server_id, device_name, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an ethernet network interface based on the suppied server_Id and device_name.'
        url = f'/system/servers/{server_id}/network_interfaces/ethernet/{device_name}'
        return self._s.post(url, json_body=body, **kwargs)


class AuthorizationPasswordPoliciesResource(ResourceBase):
    """Operations below ``/system/authorization/password_policies``."""

    def get(self, id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a single Password Policies that exist on the system'
        url = f'/system/authorization/password_policies/{id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of Password Policies that exist on the system'
        url = '/system/authorization/password_policies'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Update a single Password Policies available on the system. This policy\ndefines the requirements for passwords that are stored locally, and that\nwill be enforced on login or while creating a new user, or while a user\nis updating their password.'
        url = f'/system/authorization/password_policies/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AuthorizationPasswordValidatorsResource(ResourceBase):
    """Operations below ``/system/authorization/password_validators``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new password validator for the provided password based\non the current Password Policy.'
        url = '/system/authorization/password_validators'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class AuthorizationSettingsResource(ResourceBase):
    """Operations below ``/system/authorization/settings``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates the Authentication Settings. Changes to these values take effect immediately, but are not retroactive. For example, a change to the inactivity_timeout setting will not change the inactivity timeout for currently logged in users.\n\nWhen setting the account_lockout and host_lockout fields simultaneously, consider how they will operate. e.g. if the account based lockout configuration is less restrictive than the host based lockout configuration, a single host will be able to attempt to log in with multiple accounts before the IP address of the caller is locked out. Also, if users of the system are behind a proxy, consider disabling the host based lockout and enabling the account based lockout.'
        url = '/system/authorization/settings'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def list(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Gets the Authentication Settings for the system. These settings apply to all methods of authentication with the following exceptions.'
        url = '/system/authorization/settings'
        return self._s.get(url, fields=fields, **kwargs)


class InformationEncodingsResource(ResourceBase):
    """Operations below ``/system/information/encodings``."""

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the list of encodings that are supported by the system for event data..'
        url = '/system/information/encodings'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)


class InformationLocalesResource(ResourceBase):
    """Operations below ``/system/information/locales``."""

    def list(self, sample_type: Optional[Any]=None, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, sort: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieve Locales.'
        url = '/system/information/locales'
        params = {'sample_type': sample_type}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)


class ServersFirewallRulesResource(ResourceBase):
    """Operations below ``/system/servers/{server_id}/firewall_rules``."""

    def list(self, server_id, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of access control firewall rules based on the supplied server ID.'
        url = f'/system/servers/{server_id}/firewall_rules'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def replace(self, server_id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Sets the access control firewall rules based on the supplied server ID.'
        url = f'/system/servers/{server_id}/firewall_rules'
        return self._s.put(url, json_body=body, **kwargs)


class ServersNetworkInterfacesResource(ResourceBase):
    """Operations below ``/servers/network_interfaces``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.bonded: ServersNetworkInterfacesBondedResource = ServersNetworkInterfacesBondedResource(session)
        self.ethernet: ServersNetworkInterfacesEthernetResource = ServersNetworkInterfacesEthernetResource(session)


class ServersSystemTimeSettingsResource(ResourceBase):
    """Operations below ``/system/servers/{server_id}/system_time_settings``."""

    def create(self, server_id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Sets the system time and time zone settings of to a server host. Services are restarted after the call and service interruptions will occur.'
        url = f'/system/servers/{server_id}/system_time_settings'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def list(self, server_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the system time and time zone settings of a server host based on the supplied server ID.'
        url = f'/system/servers/{server_id}/system_time_settings'
        return self._s.get(url, fields=fields, **kwargs)


class ServersTimezonesResource(ResourceBase):
    """Operations below ``/system/servers/{server_id}/timezones``."""

    def list(self, server_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves all the available time zones that can be set for a server.'
        url = f'/system/servers/{server_id}/timezones'
        return self._s.get(url, fields=fields, **kwargs)


class AboutResource(ResourceBase):
    """Operations below ``/system/about``."""

    def get(self, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the current system information'
        url = '/system/about'
        return self._s.get(url, fields=fields, **kwargs)


class AuthorizationResource(ResourceBase):
    """Operations below ``/authorization``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.password_policies: AuthorizationPasswordPoliciesResource = AuthorizationPasswordPoliciesResource(session)
        self.password_validators: AuthorizationPasswordValidatorsResource = AuthorizationPasswordValidatorsResource(session)
        self.settings: AuthorizationSettingsResource = AuthorizationSettingsResource(session)


class EmailServersResource(ResourceBase):
    """Operations below ``/system/email_servers``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new email server.'
        url = '/system/email_servers'
        return self._s.post(url, json_body=body, **kwargs)

    def delete(self, email_server_id, **kwargs: Any) -> Any:
        'Deletes an email server.'
        url = f'/system/email_servers/{email_server_id}'
        return self._s.delete(url, **kwargs)

    def get(self, email_server_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves an email server based on the supplied email server ID.'
        url = f'/system/email_servers/{email_server_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all email servers.'
        url = '/system/email_servers'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, email_server_id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing email server.'
        url = f'/system/email_servers/{email_server_id}'
        return self._s.post(url, json_body=body, **kwargs)


class EulaAcceptancesResource(ResourceBase):
    """Operations below ``/system/eula_acceptances``."""

    def get(self, id, **kwargs: Any) -> Any:
        'Retrieves an individual EULA Acceptance by id.'
        url = f'/system/eula_acceptances/{id}'
        return self._s.get(url, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        'Retrieves the list of EULA acceptance statuses that the caller has permission to see.'
        url = '/system/eula_acceptances'
        return self._s.get(url, **kwargs)

    def update(self, id, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an individual EULA acceptance.'
        url = f'/system/eula_acceptances/{id}'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class EulasResource(ResourceBase):
    """Operations below ``/system/eulas``."""

    def list(self, **kwargs: Any) -> Any:
        'Retrieves a list of EULAs.'
        url = '/system/eulas'
        return self._s.get(url, **kwargs)


class InformationResource(ResourceBase):
    """Operations below ``/information``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.encodings: InformationEncodingsResource = InformationEncodingsResource(session)
        self.locales: InformationLocalesResource = InformationLocalesResource(session)


class ServerConnectionValidatorResource(ResourceBase):
    """Operations below ``/system/server_connection_validator``."""

    def create(self, body: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a server connection validator for the provided hostname and port, based\non the provided host ids.'
        url = '/system/server_connection_validator'
        headers = {'fields': fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)


class ServersResource(ResourceBase):
    """Operations below ``/system/servers``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.firewall_rules: ServersFirewallRulesResource = ServersFirewallRulesResource(session)
        self.network_interfaces: ServersNetworkInterfacesResource = ServersNetworkInterfacesResource(session)
        self.system_time_settings: ServersSystemTimeSettingsResource = ServersSystemTimeSettingsResource(session)
        self.timezones: ServersTimezonesResource = ServersTimezonesResource(session)

    def get(self, server_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a server host based on the supplied server ID.'
        url = f'/system/servers/{server_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, fields: Optional[Any]=None, range_header: Optional[Any]=None, filter: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a list of all server hosts in the deployment.'
        url = '/system/servers'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, server_id, body: Optional[Any]=None, **kwargs: Any) -> Any:
        'Updates an existing server.'
        url = f'/system/servers/{server_id}'
        return self._s.post(url, json_body=body, **kwargs)


class SystemAPI(ResourceBase):
    """Resource-oriented client for the ``system`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.about: AboutResource = AboutResource(session)
        self.authorization: AuthorizationResource = AuthorizationResource(session)
        self.email_servers: EmailServersResource = EmailServersResource(session)
        self.eula_acceptances: EulaAcceptancesResource = EulaAcceptancesResource(session)
        self.eulas: EulasResource = EulasResource(session)
        self.information: InformationResource = InformationResource(session)
        self.server_connection_validator: ServerConnectionValidatorResource = ServerConnectionValidatorResource(session)
        self.servers: ServersResource = ServersResource(session)

"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class DigLookupsResource(ResourceBase):
    """Operations below ``/services/dig_lookups``."""

    def create(self, ip: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new DIG lookup. Lookup completes in the background.'
        url = '/services/dig_lookups'
        params = {'IP': ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get(self, dig_lookup_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the DIG lookup status. The result is included if the lookup completed.'
        url = f'/services/dig_lookups/{dig_lookup_id}'
        return self._s.get(url, fields=fields, **kwargs)


class DnsLookupsResource(ResourceBase):
    """Operations below ``/services/dns_lookups``."""

    def create(self, ip: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new DNS lookup. Lookup completes in the background.'
        url = '/services/dns_lookups'
        params = {'IP': ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get(self, dns_lookup_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the DNS lookup status. The result is included if the lookup completes.'
        url = f'/services/dns_lookups/{dns_lookup_id}'
        return self._s.get(url, fields=fields, **kwargs)


class GeolocationsResource(ResourceBase):
    """Operations below ``/services/geolocations``."""

    def list(self, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the MaxMind geoip data for the given IP address.'
        url = '/services/geolocations'
        return self._s.get(url, fields=fields, filter_expr=filter, **kwargs)


class PortScansResource(ResourceBase):
    """Operations below ``/services/port_scans``."""

    def create(self, ip: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new PortScans lookup. Port scan completes in the background.'
        url = '/services/port_scans'
        params = {'IP': ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get(self, port_scan_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the port scan status. The result is included if the port scan completes.'
        url = f'/services/port_scans/{port_scan_id}'
        return self._s.get(url, fields=fields, **kwargs)


class WhoisLookupsResource(ResourceBase):
    """Operations below ``/services/whois_lookups``."""

    def create(self, ip: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Creates a new WHOIS lookup. Lookup completes in the background.'
        url = '/services/whois_lookups'
        params = {'IP': ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get(self, whois_lookup_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves the WHOIS lookup status. The result is included if the lookup completes.'
        url = f'/services/whois_lookups/{whois_lookup_id}'
        return self._s.get(url, fields=fields, **kwargs)


class ServicesAPI(ResourceBase):
    """Resource-oriented client for the ``services`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.dig_lookups: DigLookupsResource = DigLookupsResource(session)
        self.dns_lookups: DnsLookupsResource = DnsLookupsResource(session)
        self.geolocations: GeolocationsResource = GeolocationsResource(session)
        self.port_scans: PortScansResource = PortScansResource(session)
        self.whois_lookups: WhoisLookupsResource = WhoisLookupsResource(session)

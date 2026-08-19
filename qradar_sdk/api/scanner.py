"""Resource-oriented public QRadar API."""

from __future__ import annotations

from typing import Any, Optional

from .._http import QRadarSession
from ._base import ResourceBase


class ScanprofilesRunsResultsResource(ResourceBase):
    """Operations below ``/scanner/scanprofiles/{profileid}/runs/{run_id}/results``."""

    def list(self, profileid, run_id, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Call GET /scanner/scanprofiles/{profileid}/runs/{run_id}/results'
        url = f'/scanner/scanprofiles/{profileid}/runs/{run_id}/results'
        return self._s.get(url, range_header=range_header, fields=fields, **kwargs)


class ProfilesCreateResource(ResourceBase):
    """Operations below ``/scanner/profiles/create``."""

    def create(self, body: Optional[Any]=None, **kwargs: Any) -> Any:
        "Initiates a request to create a new scanProfile. The request takes one parameter - createScanRequest, which is just a POJO.\n\nTo create the scan, you will need to build up a JSON object that contains the Scan Profile name and ips to scan e.g.\n{'name':'New Scan Profile', 'ips':['10.100.85.135']}\n\nNote: Only IP addresses and ranges are accepted. CIDR ranges are not supported."
        url = '/scanner/profiles/create'
        return self._s.post(url, json_body=body, **kwargs)


class ProfilesStartResource(ResourceBase):
    """Operations below ``/scanner/profiles/start``."""

    def create(self, scan_profile_id: Optional[Any]=None, **kwargs: Any) -> Any:
        "Initiates a request to start an already created scanProfile. The request takes one parameter - scanProfileId.\n\nTo get a list of scanProfileIds, simply get a list of the current scan profiles by initiating a 'profiles' request on the\nscanner endpoint. The scanProfileId will be validated and an appropriate message returned."
        url = '/scanner/profiles/start'
        params = {'scanProfileId': scan_profile_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, **kwargs)


class ScanprofilesRunsResource(ResourceBase):
    """Operations below ``/scanner/scanprofiles/{profileid}/runs``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.results: ScanprofilesRunsResultsResource = ScanprofilesRunsResultsResource(session)

    def get(self, profileid, run_id, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Call GET /scanner/scanprofiles/{profileid}/runs/{run_id}'
        url = f'/scanner/scanprofiles/{profileid}/runs/{run_id}'
        return self._s.get(url, fields=fields, **kwargs)

    def list(self, profileid, range_header: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Call GET /scanner/scanprofiles/{profileid}/runs'
        url = f'/scanner/scanprofiles/{profileid}/runs'
        return self._s.get(url, range_header=range_header, fields=fields, **kwargs)


class ScanprofilesStartResource(ResourceBase):
    """Operations below ``/scanner/scanprofiles/{profileid}/start``."""

    def create(self, profileid, body: Optional[Any]=None, **kwargs: Any) -> Any:
        "Initiates a request to start an already created scanProfile. The request takes one parameter - scanProfileId, and one optional parameter - ips.\n\nTo get a list of scanProfileIds, simply get a list of the current scan profiles by initiating a 'profiles' request on the\nscanner endpoint. The scanProfileId will be validated and an appropriate message returned."
        url = f'/scanner/scanprofiles/{profileid}/start'
        return self._s.post(url, json_body=body, **kwargs)


class ProfilesResource(ResourceBase):
    """Operations below ``/scanner/profiles``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.create: ProfilesCreateResource = ProfilesCreateResource(session)
        self.start: ProfilesStartResource = ProfilesStartResource(session)

    def list(self, **kwargs: Any) -> Any:
        'Retrieves all of the currently created scan profiles. No parameters are required and the following information \nshould be retrieved for each scan profile\n\n - scanProfileId\n - scanProfileName\n - description\n - scanType\n - scannerName'
        url = '/scanner/profiles'
        return self._s.get(url, **kwargs)


class ScanprofilesResource(ResourceBase):
    """Operations below ``/scanner/scanprofiles``."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.runs: ScanprofilesRunsResource = ScanprofilesRunsResource(session)
        self.start: ScanprofilesStartResource = ScanprofilesStartResource(session)

    def delete(self, profileid, **kwargs: Any) -> Any:
        'Initiates a request to delete a  scanProfile. The request takes one parameter - the Scan Profile ID.'
        url = f'/scanner/scanprofiles/{profileid}'
        return self._s.delete(url, **kwargs)

    def get(self, profileid, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves a scan profile for a given Scan Profile ID. The only parameter required is the Scan Profile ID. The following\ninformation about a scan profile will be returned  \n\n - scanProfileId\n - name\n - description\n - scanType\n - scannerName\n - schedule\n - status\n - progress\n - endTime\n - duration'
        url = f'/scanner/scanprofiles/{profileid}'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def list(self, range_header: Optional[Any]=None, filter: Optional[Any]=None, fields: Optional[Any]=None, **kwargs: Any) -> Any:
        'Retrieves all of the currently created scan profiles. No parameters are required and the following information \nshould be retrieved for each scan profile\n\n - scanProfileId\n - name\n - description\n - scanType\n - scannerName\n - schedule\n - status\n - progress\n - endTime\n - duration'
        url = '/scanner/scanprofiles'
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def update(self, profileid, body: Optional[Any]=None, **kwargs: Any) -> Any:
        "Update a scan profile. The Scan Profile ID is required.\nThe following information on a scan profile can be updated \n\n- name\n- description\n- ips\n    eg  {'name':'Updated Scan Profile', 'ips':['10.100.85.135']}"
        url = f'/scanner/scanprofiles/{profileid}'
        return self._s.post(url, json_body=body, **kwargs)


class ScannerAPI(ResourceBase):
    """Resource-oriented client for the ``scanner`` endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        super().__init__(session)
        self.profiles: ProfilesResource = ProfilesResource(session)
        self.scanprofiles: ScanprofilesResource = ScanprofilesResource(session)

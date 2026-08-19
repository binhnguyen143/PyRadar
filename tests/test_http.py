"""Tests for the shared HTTP transport used by every SDK endpoint."""

from unittest.mock import Mock

import pytest

from qradar_sdk import QRadarClient
from qradar_sdk.exceptions import QRadarAPIError


def response(status=200, payload=None):
    result = Mock()
    result.status_code = status
    result.ok = status < 400
    result.content = b"{}" if payload is not None else b""
    result.json.return_value = payload
    result.text = str(payload)
    return result


@pytest.fixture
def client():
    value = QRadarClient(
        host="https://qradar.example.com/",
        sec_token="test-token",
        verify_ssl=False,
        max_retries=0,
    )
    yield value
    value.close()


def test_endpoint_request_contains_api_version_auth_and_tls_settings(client):
    request = Mock(return_value=response(payload={"release_name": "test"}))
    client._session._session.request = request

    assert client.system.about.get() == {"release_name": "test"}

    call = request.call_args.kwargs
    assert call["method"] == "GET"
    assert call["url"] == "https://qradar.example.com/api/system/about"
    assert call["verify"] is False
    assert call["headers"] is None or "SEC" not in call["headers"]
    assert client._session._session.headers["SEC"] == "test-token"
    assert client._session._session.headers["Version"] == "26.0"


def test_endpoint_query_and_range_are_forwarded(client):
    request = Mock(return_value=response(payload=[]))
    client._session._session.request = request

    client.siem.offenses.list(
        filter="status=OPEN", fields="id,status", range_header="0-49", sort="id"
    )

    call = request.call_args.kwargs
    assert call["url"].endswith("/api/siem/offenses")
    assert call["params"] == {
        "fields": "id,status",
        "filter": "status=OPEN",
        "sort": "id",
    }
    assert call["headers"] == {"Range": "items=0-49"}


def test_endpoint_errors_are_converted_to_sdk_exception(client):
    request = Mock(return_value=response(status=403, payload={"message": "forbidden"}))
    client._session._session.request = request

    with pytest.raises(QRadarAPIError):
        client.system.about.get()

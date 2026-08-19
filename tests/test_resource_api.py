"""Regression tests for the resource-oriented API surface."""

import ast
import asyncio
from pathlib import Path
from unittest.mock import Mock

from qradar_sdk import AsyncQRadarClient, QRadarClient


def _response(payload):
    response = Mock()
    response.ok = True
    response.content = b"{}"
    response.json.return_value = payload
    return response


def test_get_offense_uses_resource_api_and_expected_request():
    client = QRadarClient(host="qradar.example.com", sec_token="token")
    request = Mock(return_value=_response({"id": 42}))
    client._session._session.request = request

    result = client.siem.offenses.get(42, fields="id,status")

    assert result == {"id": 42}
    assert not hasattr(client.siem, "get_siem_offenses_offense_id")
    request.assert_called_once()
    call = request.call_args.kwargs
    assert call["method"] == "GET"
    assert call["url"].endswith("/api/siem/offenses/42")
    assert call["params"] == {"fields": "id,status"}


def test_nested_notes_resource_preserves_query_parameters():
    client = QRadarClient(host="qradar.example.com", sec_token="token")
    request = Mock(return_value=_response({"id": 7, "note_text": "Investigating"}))
    client._session._session.request = request

    result = client.siem.offenses.notes.create(42, note_text="Investigating")

    assert result["id"] == 7
    call = request.call_args.kwargs
    assert call["method"] == "POST"
    assert call["url"].endswith("/api/siem/offenses/42/notes")
    assert call["params"] == {"note_text": "Investigating"}


def test_async_client_traverses_resource_tree():
    async def run():
        client = AsyncQRadarClient(host="qradar.example.com", sec_token="token")
        request = Mock(return_value=_response({"id": 42}))
        client._target._session._session.request = request
        try:
            result = await client.siem.offenses.get(42)
        finally:
            await client.close()
        return result, request

    result, request = asyncio.run(run())

    assert result == {"id": 42}
    assert request.call_args.kwargs["url"].endswith("/api/siem/offenses/42")


def test_all_public_operations_call_session_directly():
    api_dir = Path(__file__).parents[1] / "qradar_sdk" / "api"
    total = 0

    for path in api_dir.glob("*.py"):
        if path.stem in {"__init__", "_base"}:
            continue

        tree = compile(path.read_text(encoding="utf-8"), str(path), "exec", ast.PyCF_ONLY_AST)
        operations = [
            node
            for class_node in tree.body
            if isinstance(class_node, ast.ClassDef)
            for node in class_node.body
            if isinstance(node, ast.FunctionDef) and node.name != "__init__"
        ]
        assert operations, path.name
        assert all(
            any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Attribute)
                and isinstance(node.func.value.value, ast.Name)
                and node.func.value.value.id == "self"
                and node.func.value.attr == "_s"
                for node in ast.walk(operation)
            )
            for operation in operations
        ), path.name
        total += len(operations)

    assert total == 729

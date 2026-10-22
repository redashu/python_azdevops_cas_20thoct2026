import json
import requests
from unittest.mock import Mock

import main


# Test 1: API retrieval succeeds
def test_fetch_user_data_success(monkeypatch):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = [
        {
            "userId": 1,
            "id": 1,
            "title": " daily report ",
            "body": " sample body "
        }
    ]

    mock_get = Mock(return_value=fake_response)
    monkeypatch.setattr(requests, "get", mock_get)

    result = main.fetch_user_data(1)

    assert len(result) == 1
    assert result[0]["id"] == 1

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts/",
        params={"userId": 1},
        timeout=10
    )


# Test 2: HTTP error is raised
def test_fetch_user_data_http_error(monkeypatch):
    fake_response = Mock()
    fake_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("404 Not Found")
    )

    monkeypatch.setattr(
        requests,
        "get",
        Mock(return_value=fake_response)
    )

    try:
        main.fetch_user_data(1)
        assert False, "Expected HTTPError"
    except requests.exceptions.HTTPError:
        pass


# Test 3: Valid records are transformed
def test_process_data_valid_record():
    data = [
        {
            "id": 1,
            "userId": 2,
            "title": " daily report ",
            "body": " sample body "
        }
    ]

    result = main.process_data(data)

    assert result == [
        {
            "record_id": 1,
            "user_id": 2,
            "title": "Daily Report",
            "body": "sample body"
        }
    ]


# Test 4: Invalid records are rejected
def test_process_data_invalid_record():
    data = [
        {
            "id": "bad-id",
            "userId": 1,
            "title": "Daily report",
            "body": "Sample body"
        },
        {
            "id": 2,
            "userId": 1,
            "title": "   ",
            "body": "Sample body"
        }
    ]

    assert main.process_data(data) == []


# Test 5: Empty input returns an empty list
def test_process_data_empty_input():
    assert main.process_data([]) == []


# Test 6: JSON export creates the correct file
def test_export_json(tmp_path):
    data = [{"record_id": 1, "title": "Daily Report"}]
    file_path = tmp_path / "test_records.json"

    main.export_json(data, file_path)

    with open(file_path, encoding="utf-8") as f:
        saved_data = json.load(f)

    assert saved_data == data


# Test 7: Empty data does not create a file
def test_export_json_empty_data(tmp_path):
    file_path = tmp_path / "empty_records.json"

    main.export_json([], file_path)

    assert not file_path.exists()
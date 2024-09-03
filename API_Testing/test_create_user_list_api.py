import pytest
import requests
import json

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/user/createWithArray"

@pytest.fixture
def user_list():
    return [
        {
            "id": 111112,
            "username": "111112",
            "firstName": "111112",
            "lastName": "111112",
            "email": "1111122test.dd",
            "password": "111112",
            "phone": "111112",
            "userStatus": 0
        }
    ]

def test_create_user_list(api_url, user_list):
    # Convert user list to JSON string
    json_data = json.dumps(user_list)

    # Make the POST request with JSON data
    response = requests.post(api_url, headers={'Content-Type': 'application/json'}, data=json_data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert response_data["message"] == "ok"
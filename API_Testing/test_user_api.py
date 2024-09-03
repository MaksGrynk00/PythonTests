import pytest
import requests

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/user"

@pytest.fixture
def user_data():
    return {
        "id": 123,
        "username": "UI0000123",
        "firstName": "UI0000123",
        "lastName": "UI0000123",
        "email": "UI0000123@test.cc",
        "password": "UI0000123",
        "phone": "1234567890",
        "userStatus": 0
    }

def test_create_user(api_url, user_data):
    # Make the POST request with user data
    response = requests.post(api_url, json=user_data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert "message" in response_data
    assert response_data["message"] == "123"
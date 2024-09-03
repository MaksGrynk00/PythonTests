import pytest
import requests

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/user/login"

@pytest.fixture
def login_credentials():
    return {
        "username": "UI0000123",
        "password": "UI0000123"
    }

def test_login_user(api_url, login_credentials):
    # Build the request URL with query parameters
    url = f"{api_url}?username={login_credentials['username']}&password={login_credentials['password']}"

    # Make the GET request
    response = requests.get(url)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert "message" in response_data
    assert response_data["message"].startswith("logged in user session:")  # Check message starts with expected prefix
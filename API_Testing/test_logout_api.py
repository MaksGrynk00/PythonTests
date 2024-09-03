import pytest
import requests

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/user/logout"

def test_logout_user(api_url):
    # Make the GET request for logout
    response = requests.get(api_url)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert response_data["message"] == "ok"
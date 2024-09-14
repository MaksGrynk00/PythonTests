import pytest
import requests



def test_logout_user(api_url8):
    # Make the GET request for logout
    response = requests.get(api_url8)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert response_data["message"] == "ok"
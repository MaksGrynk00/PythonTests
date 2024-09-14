import pytest
import requests

""" Verify that allows creating a User """

def test_create_user(api_url2, user_data):
    # Make the POST request with user data
    response = requests.post(api_url2, json=user_data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert "message" in response_data
    assert response_data["message"] == "123"
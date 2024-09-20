import requests
import json
""" 	Verify that allows creating the list of Users """

def test_create_user_list(api_url_user_createWithArray, user_list):
    # Convert user list to JSON string
    json_data = json.dumps(user_list)

    # Make the POST request with JSON data
    response = requests.post(api_url_user_createWithArray, headers={'Content-Type': 'application/json'}, data=json_data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body
    response_data = response.json()
    assert response_data["code"] == 200
    assert response_data["message"] == "ok"
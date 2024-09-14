import pytest
import requests
import json
"""	Verify that allows adding a new Pet """

def test_add_pet(api_url3, new_pet_data):
    # Convert pet data to JSON string
    json_data = json.dumps(new_pet_data)

    # Make the POST request with JSON data
    response = requests.post(api_url3, headers={'Content-Type': 'application/json'}, data=json_data)

    # Assert successful status code (likely 201 Created)
    assert response.status_code in (200, 201)  # Adjust based on API documentation

    # Assert the response body contains the added pet data (optional)
    if response.status_code == 201:  # Check if response indicates creation
        response_data = response.json()
        # Assert pet data fields based on your API response structure
        assert response_data["id"] == new_pet_data["id"]
        assert response_data["name"] == new_pet_data["name"]
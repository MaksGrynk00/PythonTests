import pytest
import requests
import json

"""	Verify that allows updating Pet’s name and status """
def test_update_pet(api_url5, updated_pet_data):
    # Convert pet data to JSON string
    json_data = json.dumps(updated_pet_data)

    # Make the PUT request with JSON data
    response = requests.put(api_url5, headers={'Content-Type': 'application/json'}, data=json_data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert the entire response body matches the updated pet data
    assert response.json() == updated_pet_data
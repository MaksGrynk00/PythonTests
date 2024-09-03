import pytest
import requests
import json

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/pet"

@pytest.fixture
def updated_pet_data():
    return {
        "id": 444,
        "category": {
            "id": 555,
            "name": "cats"
        },
        "name": "Borys-Barbarys",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

def test_update_pet(api_url, updated_pet_data):
    # Convert pet data to JSON string
    json_data = json.dumps(updated_pet_data)

    # Make the PUT request with JSON data
    response = requests.put(api_url, headers={'Content-Type': 'application/json'}, data=json_data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert the entire response body matches the updated pet data
    assert response.json() == updated_pet_data
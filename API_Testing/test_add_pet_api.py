import pytest
import requests
import json

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/pet"

@pytest.fixture
def new_pet_data():
    return {
        "id": 444,
        "category": {
            "id": 555,
            "name": "cat"
        },
        "name": "Borys",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 110,
                "name": "love"
            }
        ],
        "status": "available"
    }

def test_add_pet(api_url, new_pet_data):
    # Convert pet data to JSON string
    json_data = json.dumps(new_pet_data)

    # Make the POST request with JSON data
    response = requests.post(api_url, headers={'Content-Type': 'application/json'}, data=json_data)

    # Assert successful status code (likely 201 Created)
    assert response.status_code in (200, 201)  # Adjust based on API documentation

    # Assert the response body contains the added pet data (optional)
    if response.status_code == 201:  # Check if response indicates creation
        response_data = response.json()
        # Assert pet data fields based on your API response structure
        assert response_data["id"] == new_pet_data["id"]
        assert response_data["name"] == new_pet_data["name"]
        # ... assert other fields as needed
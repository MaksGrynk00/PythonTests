import requests

"""	Verify that allows deleting Pet  """

def test_delete_pet(api_url_pet, pet_id):
    # Construct the deletion URL with the provided pet ID
    delete_url = f"{api_url_pet}/{pet_id}"

    # Make the DELETE request
    response = requests.delete(delete_url)

    # Assert successful status code (likely 200 or 204)
    assert response.status_code in (200, 204)  # Adjust based on API documentation

    # Optionally assert a specific response body (e.g., for 200)
    if response.status_code == 200:
        response_data = response.json()
        assert response_data["code"] == 200
        assert response_data["message"] == str(pet_id)  # Convert pet ID to string
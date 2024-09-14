import pytest
import httpx
"""	Verify that allows updating Pet’s image """

@pytest.mark.asyncio
async def test_update_pet_image(api_url6, image_path):
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Prepare the request data
    data = {
        "file": (image_path, image_data, "image/jpg")
    }
    # Use httpx to send the POST request with multipart/form-data
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url6, files=data)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body (optional)
    response_data = response.json()
    assert response_data["code"] == 200
    assert "message" in response_data
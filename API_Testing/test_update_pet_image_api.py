import pytest
import httpx

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2/pet/444/uploadImage"

@pytest.fixture
def image_path():
    return "borys.jpg"  # Replace with the actual image path

def test_update_pet_image(api_url, image_path):
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Prepare the request data
    data = {
        "file": (image_path, image_data, "image/jpeg")
    }

    # Use httpx to send the POST request with multipart/form-data
    async with httpx.AsyncClient() as client:
        async def send_request():
            response = await client.post(api_url, files=data)
            return response

        response = client.run_async(send_request)

    # Assert successful status code (200)
    assert response.status_code == 200

    # Assert expected response body (optional)
    response_data = response.json()
    assert response_data["code"] == 200
    assert "message" in response_data
    # You might need to adjust the response assertion based on your API's structure
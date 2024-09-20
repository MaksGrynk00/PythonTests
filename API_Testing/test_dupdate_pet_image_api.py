import os
import requests

"""Verify that allows updating Pet’s image """

def test_update_pet_image(api_url_uploadImage, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    data = {
        "file": (os.path.basename(image_path), image_data, 'image/jpg')
    }

    response = requests.post(api_url_uploadImage, files=data)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data['code'] == 200
    assert 'message' in response_data
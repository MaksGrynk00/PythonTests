import pytest
import os

# login User test
@pytest.fixture
def api_url_login():
    return "https://petstore.swagger.io/v2/user/login"

@pytest.fixture
def login_credentials():
    return {
        "username": "UI0000123",
        "password": "UI0000123"
    }
# create User api test
@pytest.fixture
def api_url_user():
    return "https://petstore.swagger.io/v2/user"

@pytest.fixture
def user_data():
    return {
        "id": 123,
        "username": "UI0000123",
        "firstName": "UI0000123",
        "lastName": "UI0000123",
        "email": "UI0000123@test.cc",
        "password": "UI0000123",
        "phone": "1234567890",
        "userStatus": 0
    }
# create pet test
@pytest.fixture
def api_url_pet():
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

# create user list test
@pytest.fixture
def api_url_user_createWithArray():
    return "https://petstore.swagger.io/v2/user/createWithArray"

@pytest.fixture
def user_list():
    return [
        {
            "id": 111112,
            "username": "111112",
            "firstName": "111112",
            "lastName": "111112",
            "email": "1111122test.dd",
            "password": "111112",
            "phone": "111112",
            "userStatus": 0
        }
    ]
# data to create new pet
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
# pet image test

@pytest.fixture
def api_url_uploadImage():
    return "https://petstore.swagger.io/v2/pet/444/uploadImage"


# Upload Image relative path to the project.
@pytest.fixture
def image_path():
    # Note: It only works if the test is run from the project directory.
    base_dir = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(base_dir, 'th.jpg')  # relative path to your image
    return image_path


@pytest.fixture
def pet_id():
    return 444  # Replace with the actual pet ID you want to delete

# User loguot test
@pytest.fixture
def api_url_logOut():
    return "https://petstore.swagger.io/v2/user/logout"

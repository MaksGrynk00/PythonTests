import pytest
import requests

# login User test
@pytest.fixture
def api_url1():
    return "https://petstore.swagger.io/v2/user/login"

@pytest.fixture
def login_credentials():
    return {
        "username": "UI0000123",
        "password": "UI0000123"
    }
# create User api test
@pytest.fixture
def api_url2():
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
def api_url3():
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
def api_url4():
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
# update pet test
@pytest.fixture
def api_url5():
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
# pet image test

@pytest.fixture
def api_url6():
    return "https://petstore.swagger.io/v2/pet/444/uploadImage"


@pytest.fixture
def image_path():
    return "C:\\Users\\Maksym_Grynkiv\\source\\repos\\MaksGrynk00\\PythonTest\\API_Testing\\th.jpg"  # the image path

# delete pet test
@pytest.fixture
def api_url7():
    return "https://petstore.swagger.io/v2/pet"

@pytest.fixture
def pet_id():
    return 444  # Replace with the actual pet ID you want to delete

# User loguot test

@pytest.fixture
def api_url8():
    return "https://petstore.swagger.io/v2/user/logout"

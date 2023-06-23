import pytest
from settings import valid_password, valid_email
from main import PetFriends
import os

@pytest.fixture()
def setup_key():
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    header["auth_key"] = pets_f.auth_key["key"]
    yield header

@pytest.fixture()
def setup_invalid_key():
    header = {}
    header["auth_key"] = "pets_f.auth_key"
    yield header


@pytest.fixture()
def setup_key_pet_id():
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    pet_id = []
    header["auth_key"] = pets_f.auth_key["key"]
    status, result = pets_f.get_list_of_pets("GET", "my_pets", header=header)

    if len(result["pets"]) > 0:
        for _ in result["pets"]:
            pet_id.append(_["id"])

    yield header, pet_id[0]


@pytest.fixture()
def setup_pet_id_and_photo():
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    pet_id = []
    pet_photo = "images/corgi.jpeg"
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    header["auth_key"] = pets_f.auth_key["key"]
    status, result = pets_f.get_list_of_pets("GET", "my_pets", header=header)
    for _ in result["pets"]:
        if len(result["pets"]) > 0 and _["pet_photo"] == "":
            pet_id.append(_["id"])

    yield header, pet_id[0], pet_photo

from main import PetFriends
from params import params_id_invalid
import pytest

pets = PetFriends()

"""Valid data"""
def test_update_pet_info_valid(setup_key_pet_id):
    header, pet_id = setup_key_pet_id
    name = "name"
    animal_type = "animal_type"
    age = 1
    status, result = pets.put_pet_info(header, pet_id, name, animal_type, age)
    assert status == 200
    status, result = pets.get_list_of_pets("GET", "my_pets", header=header)
    for _ in result["pets"]:
        if _["id"] == pet_id:
            assert _["name"] == name
            assert _["animal_type"] == animal_type
            assert _["age"] == str(age)
    print("\n", status)
    print(result)


"""invalid key, valid data"""
def test_update_pet_info_invalid_key(setup_key_pet_id):
    header, pet_id = setup_key_pet_id
    name = "name"
    animal_type = "animal_type"
    age = 1
    header["auth_key"] = ""
    status, result = pets.put_pet_info(header, pet_id, name, animal_type, age)
    assert status == 403
    print("\n", status)
    print(result)


"""Valid key, INvalid id"""
@pytest.mark.parametrize("id, expected", params_id_invalid)
def test_update_pet_invalid_id(setup_key_pet_id, id, expected):
    header, _ = setup_key_pet_id
    pet_id = id
    name = "name"
    animal_type = "animal_type"
    age = 1
    status, result = pets.put_pet_info(header, pet_id, name, animal_type, age)
    assert status == expected
    print("\n", status)
    print(result)


"""Valid key, None id"""
def test_update_pet_none_id(setup_key):
    header = setup_key
    pet_id = None
    name = "name"
    animal_type = "animal_type"
    age = 1
    status, result = pets.put_pet_info(header, pet_id, name, animal_type, age)
    assert status == 400
    print("\n", status)
    print(result)
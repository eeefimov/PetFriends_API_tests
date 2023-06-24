from main import PetFriends
from params import params_id_invalid
import pytest

pets = PetFriends()

"""valid data"""
def test_delete_pets(setup_key, setup_key_pet_id):
    header = setup_key
    _, pet_id = setup_key_pet_id
    _, result = pets.get_list_of_pets("GET", "my_pets", header)
    status = pets.delete_pet(header, pet_id)
    assert status == 200
    _, result_deleted = pets.get_list_of_pets("GET", "my_pets", header)
    assert len(result["pets"]) == len(result_deleted["pets"]) + 1


"""Invalid key"""
def test_delete_pets_invalid_key(setup_invalid_key, setup_key_pet_id):
    header = setup_invalid_key
    _, pet_id = setup_key_pet_id
    status  = pets.delete_pet(header, pet_id)
    assert status == 403


"""Invalid id"""
@pytest.mark.parametrize("id, expected", params_id_invalid)
def test_delete_pets_invalid_id(setup_invalid_key, id, expected):
    header = setup_invalid_key
    pet_id = id
    status = pets.delete_pet(header, pet_id)
    assert status == expected
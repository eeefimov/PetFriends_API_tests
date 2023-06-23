import pytest
from params import params_id_invalid, \
    params_add_pet_photo_valid, params_add_pet_invalid_photo
from main import PetFriends

pets = PetFriends()

"""valid"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_add_photo_valid(setup_key_pet_id, name, animal_type, age, pet_photo):
    header, pet_id = setup_key_pet_id
    pet_photo = pet_photo
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 200
    status, result = pets.get_list_of_pets("GET", "my_pets", header=header)
    for _ in result["pets"]:
        if _["id"] == pet_id:
            assert _["pet_photo"] != ""
    print(result)


"""invalid key, valid data"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_add_photo_invalid_key(setup_key_pet_id, name, animal_type, age, pet_photo):
    header, pet_id = setup_key_pet_id
    pet_photo = pet_photo
    header["auth_key"] = "qew"
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 403
    print(result)


'''None key'''
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_add_photo_none_key(setup_key_pet_id, name, animal_type, age, pet_photo):
    header, pet_id = setup_key_pet_id
    pet_photo = pet_photo
    header["auth_key"] = None
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 403
    print(result)


#BUG 500 with wrong id
"""valid key, invalid id"""
@pytest.mark.parametrize("id, expected", params_id_invalid)
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_add_photo_invalid_id(setup_key, name, animal_type, age, pet_photo, id, expected):
    header = setup_key
    pet_id = id
    pet_photo = pet_photo
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == expected
    print(result)

#deffect1: > 1s
#deffect2: add photo to exicting photo
"""Valid data, existing pet has pet"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_add_photo_exicting_photo(setup_key_pet_id, name, animal_type, age, pet_photo):
    header, pet_id = setup_key_pet_id
    pet_photo = pet_photo
    status, result = pets.get_list_of_pets("GET", "my_pets", header=header)
    for _ in result["pets"]:
        if _["pet_photo"] != "":
            pet_id == _["id"]
            break
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 200
    print(result)

#FAILD 500, img, txt, error photo
"""valid data, Invalid photo file"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_invalid_photo)
def test_add_photo_invalid_photo(setup_key_pet_id, name, animal_type, age, pet_photo):
    header, pet_id = setup_key_pet_id
    pet_photo = pet_photo
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 200
    status, result = pets.get_list_of_pets("GET", "my_pets", header=header)
    for _ in result["pets"]:
        if _["id"] == pet_id:
            assert _["pet_photo"] != ""
    print(status, result)


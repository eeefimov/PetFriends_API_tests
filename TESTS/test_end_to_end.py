from main import PetFriends
import pytest
from params import params_add_pet_nophoto_valid, params_add_pet_photo_valid


pets = PetFriends()

"""Creat pet without photo, update pet info, delete pet"""
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_nophoto_valid)
def test_Add_pet_simple_Update_info_Delete(setup_key, name, animal_type, age):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 200
    pet_id = result["id"]
    name = "new_name"
    animal_type = "new_type"
    age = 1
    status, result = pets.put_pet_info(header, pet_id, name, animal_type, age)
    assert status == 200
    assert result["id"] == pet_id
    assert result["name"] == name
    assert result["animal_type"] == animal_type
    assert result["age"] == str(age)
    print(status, result)
    status = pets.delete_pet(header, pet_id)
    assert status == 200
    print(status, "THIS is THE END")


"""create pet without photo, add photo, delete"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_Add_pet_simple_Update_info_Update_photo_Delete(setup_key, name, animal_type, age, pet_photo):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 200
    pet_id = result["id"]
    pet_photo = pet_photo
    photo_befor = result["pet_photo"]
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 200
    assert result["pet_photo"] != photo_befor
    print(status, result)
    status = pets.delete_pet(header, pet_id)
    assert status == 200
    print(status, "THIS is THE END")


"""create pet with photo, update info, update photo, delete"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_Add_pet_Update_info_Update_photo_Delete(setup_key, name, animal_type, age, pet_photo):
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, str(age), pet_photo)
    assert status == 200
    pet_id = result["id"]
    name = "new_name"
    animal_type = "new_type"
    age = 1
    status, result = pets.put_pet_info(header, pet_id, name, animal_type, age)
    assert status == 200
    status, result = pets.post_photo_pet(header, pet_id, pet_photo)
    assert status == 200
    status = pets.delete_pet(header, pet_id)
    assert status == 200
    print(status, "THIS is THE END")
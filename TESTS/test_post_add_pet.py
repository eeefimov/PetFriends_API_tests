import pytest
from params import params_add_pet_photo_valid, params_add_pet_invalid_photo,\
    params_add_pet_empty_fields
from main import PetFriends

"""OPTIONAL TESTS: big size photo, multimedia file, file with code or script"""

pets = PetFriends()


#BUG age int->str
"""Valid auth_key(email, pass), Valid data """
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_valid(setup_key, name, animal_type, age, pet_photo):
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, age, pet_photo)
    assert status == 200
    print(result)


"""Valid auth_key(email, pass), Valid data str(age)"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_valid(setup_key, name, animal_type, age, pet_photo):
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, str(age), pet_photo)
    assert status == 200
    print(result)


"""InValid auth_key(email, pass), Valid data str(age)"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_valid(setup_invalid_key, name, animal_type, age, pet_photo):
    header = setup_invalid_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, str(age), pet_photo)
    assert status == 403
    print(result)


#BUG png - no photo, creat pet with no photo using txt or jpeg file with error
"""Valid auth_key(email, pass), INValid photo file"""
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_invalid_photo,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_post_add_pet_valid(setup_key, name, animal_type, age, pet_photo):
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['pet_photo'] != ""
    print(result)


#BUG: create pet with photo and empty fields (requered)
"""Valid auth_key(email, pass), Empty fields"""
@pytest.mark.parametrize("name_n, animal_type_n, age_n", params_add_pet_empty_fields)
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_valid(setup_key, name, name_n, animal_type, animal_type_n, age, age_n, pet_photo):
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name_n, animal_type_n, str(age_n), pet_photo)
    assert status == 400
    print(result)
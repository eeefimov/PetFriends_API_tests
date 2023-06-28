import pytest
from params import params_add_pet_photo_valid, params_add_pet_photo_type,\
    params_add_pet_empty_fields
from main import PetFriends

"""OPTIONAL TESTS: big size photo, multimedia file, file with code or script"""

pets = PetFriends()


#BUG age int->str
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_valid_int(setup_key, name, animal_type, age, pet_photo):
    """Valid auth_key(email, pass), Valid data """
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, age, pet_photo)
    assert status == 200
    print(result)


@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_valid_str(setup_key, name, animal_type, age, pet_photo):
    """Valid auth_key(email, pass), Valid data str(age)"""
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, str(age), pet_photo)
    assert status == 200
    print(result)


@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_invalid_key(setup_invalid_key, name, animal_type, age, pet_photo):
    """InValid auth_key(email, pass), Valid data str(age)"""
    header = setup_invalid_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, str(age), pet_photo)
    assert status == 403
    print(result)


#BUG png - no photo, creat pet with no photo using txt or jpeg file with error
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_type,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_post_add_pet_photo_type(setup_key, name, animal_type, age, pet_photo):
    """Valid auth_key(email, pass), INValid photo file"""
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['pet_photo'] != ""
    print(result)


#BUG: create pet with photo and empty fields (requered)
@pytest.mark.parametrize("name_n, animal_type_n, age_n", params_add_pet_empty_fields)
@pytest.mark.parametrize("name, animal_type, age, pet_photo", params_add_pet_photo_valid)
def test_create_pet_empty_fields(setup_key, name, name_n, animal_type, animal_type_n, age, age_n, pet_photo):
    """Valid auth_key(email, pass), Empty fields"""
    header = setup_key
    status, result = pets.post_pet_with_photo(header, name_n, animal_type_n, str(age_n), pet_photo)
    assert status == 400
    print(result)
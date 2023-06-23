import pytest
from params import params_add_pet_nophoto_valid, params_add_pet_empty_fields\
    , params_add_pet_invalid_data_type, params_add_pet_check_string_fields_special, \
    params_add_pet_check_age_numbers
from main import PetFriends

pets = PetFriends()

#BUG time > 1 sec (flasky)
"""Valid data"""
@pytest.mark.positive
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_nophoto_valid)
def test_create_pet_simple_valid(setup_key, name, animal_type, age):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 200
    print(result)

#BUG <class 'str'> != <class 'int'> age
"""valid data. Check Json fields"""
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_nophoto_valid)
def test_create_pet_simple_check_json(setup_key, name, animal_type, age):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 200
    assert type(result["animal_type"]) == str
    assert type(result["created_at"]) == str
    assert type(result["id"]) == str
    assert type(result["name"]) == str
    assert type(result["pet_photo"]) == str
    assert type(result["age"]) == int


"""INvalid auth_key(email, pass), Valid data """
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_nophoto_valid)
def test_create_pet_simple_invalid_key(setup_invalid_key, name, animal_type, age):
    header = setup_invalid_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 403
    print("\n", result)


"""NO auth_key(email, pass), Valid data """
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_nophoto_valid)
def test_create_pet_simple_invalid_key(setup_invalid_key, name, animal_type, age):
    header = None
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 403
    print("\n", result)



"""Valid auth_key(email, pass), None data(all fields are required)"""
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_empty_fields)
def test_create_pet_simple_empty_fields(setup_key, name, animal_type, age):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 400
    print(result)


# BUG
"""Valid auth_key(email, pass), INvalid data type"""
@pytest.mark.parametrize("name, animal_type, age", params_add_pet_invalid_data_type)
def test_create_pet_simple_invalid_data(setup_key, name, animal_type, age):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == 400


#BUG Spechial char
"""Valid auth_key(email, pass), Check special chars"""
@pytest.mark.parametrize("name, animal_type, age, expected", params_add_pet_check_string_fields_special)
def test_create_pet_simple_special_chars(setup_key, name, animal_type, age, expected):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == expected


#BUG <0, 1000
"""Valid auth_key(email, pass), Check AGE"""
@pytest.mark.parametrize("name, animal_type, age, expected", params_add_pet_check_age_numbers)
def test_create_pet_simple_age(setup_key, name, animal_type, age, expected):
    header = setup_key
    status, result = pets.post_pet_without_photo(header, name, animal_type, age)
    assert status == expected

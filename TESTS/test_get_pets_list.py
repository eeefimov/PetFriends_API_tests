import pytest
from main import PetFriends
from params import params_filter_valid, \
    params_filter_invalid, params_filter_methods, \
    params_filter_json_fields

pets = PetFriends()


"""valid data(email, pass), 2 filters"""
@pytest.mark.positive
@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_valid(setup_key, filter):
    header = setup_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 200
    print("\n", status, result)


"""INvalid auth_key"""
@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_invalid_key(setup_invalid_key, filter):
    header = setup_invalid_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 403


"""NO auth_key"""
@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_no_key(setup_invalid_key, filter):
    header = None
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 403


#BUG str != int
"""Valid data. Check correct json fields"""
@pytest.mark.positive
@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
@pytest.mark.parametrize("json_key", params_filter_json_fields,
                        ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_valid_json_fields(setup_key, json_key, filter):
    header = setup_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 200
    for _ in range(0, len(result)):
        assert json_key in result["pets"][_]
        pet = result["pets"][_]
    print(pet)
    assert type(pet["animal_type"]) == str
    assert type(pet["created_at"]) == str
    assert type(pet["id"]) == str
    assert type(pet["name"]) == str
    assert type(pet["pet_photo"]) == str
    assert type(pet["age"]) == int


"""Valid data, Valid filter. Check INVALID Methods(PUT, DELETE, PATCH)"""
@pytest.mark.parametrize("filter, method", params_filter_methods,
                        ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_put_list_of_pets_methods(setup_key, filter, method):
    header = setup_key
    mtd = str(method)
    status, result = pets.get_list_of_pets(mtd, filter, header=header)
    if mtd == "PATCH":
        assert status == 400
    else:
        assert status == 405
    print("\n", result, "\n")

#BUG 500
"""valid data(email, pass), INVALID filters"""
@pytest.mark.parametrize("filter", params_filter_invalid,
                        ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_of_pets_invalid_filter(setup_key, filter):
    header = setup_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 200
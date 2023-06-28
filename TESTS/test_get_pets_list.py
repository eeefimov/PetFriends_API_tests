import pytest
from main import PetFriends
from params import params_filter_valid, \
    params_filter_invalid, params_filter_methods, \
    params_filter_json_fields

pets = PetFriends()


@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_valid(setup_key, filter):
    """valid data(email, pass), 2 filters"""
    header = setup_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 200
    print("\n", status, result)


@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_invalid_key(setup_invalid_key, filter):
    """INvalid auth_key"""
    header = setup_invalid_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 403


@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_no_key(setup_invalid_key, filter):
    """NO auth_key"""
    header = None
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 403


#BUG str != int
@pytest.mark.parametrize("filter", params_filter_valid,
                         ids=lambda val: f"{val} ({pytest.current_test_name()})")
@pytest.mark.parametrize("json_key", params_filter_json_fields,
                        ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_valid_json_fields(setup_key, json_key, filter):
    """Valid data. Check correct json fields"""
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


@pytest.mark.parametrize("filter, method", params_filter_methods,
                        ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_put_list_of_pets_methods(setup_key, filter, method):
    """Valid data, Valid filter. Check INVALID Methods(PUT, DELETE, PATCH)"""
    header = setup_key
    mtd = str(method)
    status, result = pets.get_list_of_pets(mtd, filter, header=header)
    if mtd == "PATCH":
        assert status == 400
    else:
        assert status == 405
    print("\n", result, "\n")


#BUG 500
@pytest.mark.parametrize("filter", params_filter_invalid,
                        ids=lambda val: f"{val} ({pytest.current_test_name()})")
def test_get_list_of_pets_invalid_filter(setup_key, filter):
    """valid data(email, pass), INVALID filters"""
    header = setup_key
    status, result = pets.get_list_of_pets("GET", filter, header=header)
    assert status == 200
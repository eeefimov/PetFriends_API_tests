from API_Logic.GetList import PetFriendsGetList
import pytest
import allure
from TESTS.params import params_filter_valid, params_filter_invalid, params_filter_methods

pf = PetFriendsGetList()


@allure.feature("Get Pet List")
@allure.suite("Get Pet List")
class TestGetPetList:

    @allure.title("Get Pet List with Valid Filter")
    @allure.description("""
    Get the list of pets with a valid filter as: my_pets.

    Precondition:
    - User has a valid API key.
    - The filter 'my_pets' is valid.

    Expected result:
    - Response returns HTTP status code 200.
    """)
    @pytest.mark.parametrize("fltr, expected", params_filter_valid,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_pet_list_valid(self, setup_key, fltr, expected):
        pf.get_pet_list_with_valid_filter(setup_key, fltr, expected)

    @allure.title("Get Pet List with Invalid API Key")
    @allure.description("""
    Get the list of pets with an invalid API key and a valid filter as: my_pets.

    Precondition:
    - User has an invalid API key.
    - The filter 'my_pets' is valid.

    Expected result:
    - Response returns HTTP status code 403.
    """)
    @pytest.mark.parametrize("fltr, expected", params_filter_valid,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_pet_list_invalid_key(self, setup_invalid_key, fltr, expected):
        expect = 403
        pf.get_pet_list_with_valid_filter(setup_invalid_key, fltr, expect)

    @allure.title("Get Pet List without API Key")
    @allure.description("""
    Get the list of pets without an API key and a valid filter as: my_pets.

    Precondition:
    - User does not provide an API key.
    - The filter 'my_pets' is valid.

    Expected result:
    - Response returns HTTP status code 403.
    """)
    @pytest.mark.parametrize("fltr, expected", params_filter_valid,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_pet_list_no_key(self, fltr, expected):
        expect = 403
        header = None
        pf.get_pet_list_with_valid_filter(header, fltr, expect)

    @allure.title("Get Pet List with Invalid Filter")
    @allure.description("""
    Get the list of pets with an invalid filter as: ' ' (empty string).

    Precondition:
    - User has a valid API key.
    - The filter is invalid (empty string).

    Expected result:
    - Response returns HTTP status code 422.
    """)
    @pytest.mark.parametrize("fltr, expected", params_filter_invalid,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_pet_list_invalid_filter(self, setup_key, fltr, expected):
        pf.get_pet_list_with_valid_filter(setup_key, fltr, expected)

    @allure.title("Get Pet List with Other HTTP Methods")
    @allure.description("""
    Get the list of pets using HTTP methods other than GET (e.g., PUT, POST, DELETE).

    Precondition:
    - User has a valid API key.
    - The filter 'my_pets' is valid.

    Expected result:
    - Response returns HTTP status code 405 for PUT and DELETE methods, and 400 for POST method.
    """)
    @pytest.mark.parametrize("fltr, expected, method", params_filter_methods,
                             ids=lambda val: f"{val} ({pytest.current_test_name()})")
    def test_get_pet_list_other_methods(self, setup_key, fltr, expected, method):
        pf.get_pet_list_with_other_methods(setup_key, fltr, expected, method)

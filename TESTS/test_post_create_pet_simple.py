import allure
import pytest
from API_Logic.CreatePetSimple import PetFriendsCreatePetSimple
from TESTS.params import params_add_pet_no_photo_valid, params_add_pet_empty_fields, params_add_pet_no_photo_invalid_key

pf = PetFriendsCreatePetSimple()


@allure.feature("Create Pet (Simple)")
@allure.suite("Create Pet (Simple)")
class TestCreatePetSimple:

    @allure.title("Create pet with valid information")
    @allure.description("""
    Create a pet with valid information and verify its presence in the list.

    Precondition:
    - User is authenticated and has a valid API key.

    Expected result:
    - A pet is successfully created, and its information is verified in the list.
    """)
    @pytest.mark.parametrize("name, animal_type, age, expected", params_add_pet_no_photo_valid)
    def test_create_pet_simple_valid(self, delete_pet_after, name, animal_type, age, expected):
        pf.create_pet_simple(delete_pet_after, name, animal_type, age, expected)

    @allure.title("Create pet with missing required fields")
    @allure.description("""
    Attempt to create a pet with missing required fields.

    Precondition:
    - User is authenticated and has a valid API key.

    Expected result:
    - The request returns a 400 error code.
    """)
    @pytest.mark.parametrize("name, animal_type, age, expected", params_add_pet_empty_fields)
    def test_create_pet_simple_check_empty_fields(self, delete_pet_after, name, animal_type, age, expected):
        pf.create_pet_simple(delete_pet_after, name, animal_type, age, expected)

    @allure.title("Create pet with invalid API key")
    @allure.description("""
    Attempt to create a pet with an invalid API key.

    Precondition:
    - User is not authenticated (invalid API key is provided).

    Expected result:
    - The request returns a 403 error code.
    """)
    @pytest.mark.parametrize("name, animal_type, age, expected", params_add_pet_no_photo_invalid_key)
    def test_create_pet_simple_invalid_key(self, setup_invalid_key, name, animal_type, age, expected):
        pf.create_pet_invalid_key(setup_invalid_key, name, animal_type, age, expected)

import pytest
import allure
from API_Logic.CreatePetWithPhoto import PetFriendCreatePetWithPhoto
from TESTS.params import params_add_pet_with_photo_valid, params_add_pet_photo_type, params_add_pet_photo_empty_fields

pf = PetFriendCreatePetWithPhoto()


@allure.feature("Create Pet with Photo")
@allure.suite("Create Pet")
class TestCreatePet:

    @allure.title("Create Pet with Photo - Valid Data")
    @allure.description("""
    Create a pet with a photo using valid data.

    Precondition:
    - User has a valid API key.
    - Pet data is valid.

    Expected result:
    - Pet is successfully created, and the response returns HTTP status code 200.
    """)
    @pytest.mark.parametrize("name, animal_type, age, photo, expected", params_add_pet_with_photo_valid)
    def test_create_pet_with_photo_valid(self, setup_key, name, animal_type, age, photo, expected):
        pf.create_pet(setup_key, name, animal_type, age, photo, expected)


    @allure.title("Create Pet with Photo - Invalid API Key")
    @allure.description("""
    Attempt to create a pet with a photo using an invalid API key.

    Precondition:
    - User has an invalid API key.
    - Pet data is valid.

    Expected result:
    - Pet creation is denied, and the response returns HTTP status code 403.
    """)
    @pytest.mark.parametrize("name, animal_type, age, photo, expected", params_add_pet_with_photo_valid)
    def test_create_pet_with_photo_invalid_key(self, setup_invalid_key, name, animal_type, age, photo, expected):
        expected = 403
        pf.create_pet(setup_invalid_key, name, animal_type, age, photo, expected)

    @allure.title("Create Pet with Photo - Empty Fields")
    @allure.description("""
    Attempt to create a pet with a photo with empty fields.

    Precondition:
    - User has a valid API key.
    - Pet data contains empty fields.

    Expected result:
    - Pet creation is denied, and the response returns HTTP status code 400.
    """)
    @pytest.mark.parametrize("name, animal_type, age, photo, expected", params_add_pet_photo_empty_fields)
    def test_create_pet_empty_fields(self, setup_key, name, animal_type, age, photo, expected):
        pf.create_pet(setup_key, name, animal_type, age, photo, expected)

    @allure.title("Create Pet with Photo - Different Photo Types")
    @allure.description("""
    Attempt to create a pet with a photo using different photo types (e.g., PNG).

    Precondition:
    - User has a valid API key.
    - Pet data is valid, but the photo type is different.

    Expected result:
    - Pet creation is successful, and the response returns HTTP status code 200.
    """)
    @pytest.mark.parametrize("name, animal_type, age, photo, expected", params_add_pet_photo_type)
    def test_create_pet_with_photo_different_type(self, setup_key, name, animal_type, age, photo, expected):
        pf.create_pet(setup_key, name, animal_type, age, photo, expected)


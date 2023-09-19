import pytest
from API_Logic.PutUpdateInfo import PetFriendUpdatePet
from TESTS.params import randomize_number, randomize_string, randomize_id
import allure

pf = PetFriendUpdatePet()
pet_number = randomize_number(10)


@allure.feature("Update Pet Information")
@allure.suite("Update Pet Information")
class TestUpdatePetInfo:

    @allure.title("Update Pet Information with Valid Data")
    @allure.description("""
    Update a pet's information with valid data.

    Precondition:
    - User is authenticated and has a valid API key.
    - There is at least one pet in the list.

    Expected result:
    - The pet's information is successfully updated.
    """)
    @pytest.mark.usefixtures("capture_console_output")
    def test_update_pet_info(self, setup_key):
        pf.update_pet_info(setup_key, 0, 200)

    @allure.title("Update Pet Information with Random Pet Number")
    @allure.description("""
    Update a pet's information with a random pet number.

    Precondition:
    - User is authenticated and has a valid API key.

    Expected result:
    - The pet's information is successfully updated.
    """)
    @pytest.mark.usefixtures("capture_console_output")
    def test_update_pet_info_random(self, setup_key):
        pf.update_pet_info(setup_key, pet_number, 200)

    @allure.title("Update Pet Information with Invalid Key")
    @allure.description("""
    Attempt to update a pet's information with an invalid API key.

    Precondition:
    - User is not authenticated.

    Expected result:
    - The request returns a 403 error code, and the pet's information is not updated.
    """)
    @pytest.mark.usefixtures("capture_console_output")
    def test_update_pet_info_invalid_key(self, setup_key, setup_invalid_key):
        pf.update_pet_info_invalid_key(setup_key, setup_invalid_key, 0, 403)

    @allure.title("Update Pet Information with Invalid Pet ID")
    @allure.description("""
    Attempt to update a pet's information with an invalid pet ID.

    Precondition:
    - User is authenticated and has a valid API key.

    Expected result:
    - The request returns a 400 error code, and the pet's information is not updated.
    """)
    @pytest.mark.usefixtures("capture_console_output")
    def test_update_pet_info_invalid_id(self, setup_key):
        status, result = pf.put_pet_info(
            setup_key, randomize_id(), randomize_string(5), randomize_string(5), randomize_number(5)
        )
        assert status == 400
        print(result)

    @allure.title("Update Pet Information with None Pet ID")
    @allure.description("""
    Attempt to update a pet's information with a None pet ID.

    Precondition:
    - User is authenticated and has a valid API key.

    Expected result:
    - The request returns a 400 error code, and the pet's information is not updated.
    """)
    @pytest.mark.usefixtures("capture_console_output")
    def test_update_pet_info_none_id(self, setup_key):
        status, result = pf.put_pet_info(
            setup_key, None, randomize_string(5), randomize_string(5), randomize_number(5)
        )
        assert status == 400
        print(result)

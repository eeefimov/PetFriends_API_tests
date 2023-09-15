from API_Logic.DeletePet_upd import PetFriendsDeletePet
import allure
import pytest

pf = PetFriendsDeletePet()


@allure.feature("Delete Pet")
@allure.suite("Delete Pet")
class TestDeletePet:

    @allure.title("Delete first valid pet")
    @allure.description("""
    Delete the first valid pet in the list of my_pets.

    Precondition:
    - User is authenticated and has a valid API key.
    - There is at least one pet in the list.

    Expected result:
    - The pet is successfully deleted, and the total number of pets is reduced by one.
    """)
    def test_delete_first_valid_pet(self, setup_key):
        pf.delete_first_valid_pet(setup_key, None)

    @allure.title("Delete random valid pet")
    @allure.description("""
    Delete a random valid pet in the list of my_pets.

    Precondition:
    - User is authenticated and has a valid API key.
    - There is at least one pet in the list.

    Expected result:
    - A random pet is successfully deleted, and the total number of pets is reduced by one.
    """)
    def test_delete_random_valid_pet(self, setup_key):
        pf.delete_random_valid_pet(setup_key)
        allure.attach("Test Status", "Test passed successfully", allure.attachment_type.TEXT)

    @allure.title("Delete pet with invalid ID")
    @allure.description("""
    Attempt to delete a pet with an invalid ID.

    Precondition:
    - User is authenticated and has a valid API key.
    - Provide an invalid pet ID.

    Expected result:
    - The request returns a 403 error code, and the pet is not deleted.
    """)
    def test_delete_pet_invalid_id(self, setup_key, setup_invalid_id):
        pf.delete_pet_invalid_id(setup_key, setup_invalid_id)

    @allure.title("Delete pet with invalid key")
    @allure.description("""
    Attempt to delete a pet with an invalid API key.

    Precondition:
    - User is not authenticated (invalid API key is provided).

    Expected result:
    - The request returns a 403 error code, and the pet is not deleted.
    """)
    def test_delete_pet_invalid_key(self, setup_invalid_key):
        pf.delete_pet_invalid_id(setup_invalid_key, None)


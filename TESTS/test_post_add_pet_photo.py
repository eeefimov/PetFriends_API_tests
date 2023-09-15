import pytest
from API_Logic.AddPetPhoto import PetFriendsAddPhoto
import allure
from TESTS.params import valid_pet_photo, invalid_pet_photo_txt

pf = PetFriendsAddPhoto()

ph = valid_pet_photo
ph_invalid = invalid_pet_photo_txt


@allure.feature("Add Photo to Pet")
@allure.suite("Add Photo to Pet")
class TestAddPhotoToPet:

    @allure.title("Add Photo to Pet with Valid Photo")
    @allure.description("""
    Add a valid photo to an existing pet.

    Precondition:
    - User is authenticated and has a valid API key.
    - There is at least one pet in the list.

    Expected result:
    - The photo is successfully added to the pet.
    """)
    def test_add_pet_photo_valid(self, delete_pet_after):
        pf.add_pet_photo(delete_pet_after, 0, ph, "no", 200)

    @allure.title("Add Photo to Pet with Existing Photo")
    @allure.description("""
    Attempt to add a photo to a pet that already has a photo.

    Precondition:
    - User is authenticated and has a valid API key.
    - There is at least one pet in the list.
    - The pet already has a photo.

    Expected result:
    - The request returns a 400 error code, and the photo is not added.
    """)
    def test_add_pet_photo_existing_photo(self, delete_pet_after):
        pf.add_pet_photo(delete_pet_after, 0, ph, "yes", 400)

    @allure.title("Add Photo to Pet with Invalid Pet ID")
    @allure.description("""
    Attempt to add a photo to a non-existing pet.

    Precondition:
    - User is authenticated and has a valid API key.

    Expected result:
    - The request returns a 400 error code, and the photo is not added.
    """)
    def test_add_pet_photo_invalid_pet_id(self, setup_key):
        pf.add_pet_photo(setup_key, 0, ph, "invalid_id", 400)

    @allure.title("Add Photo with Invalid Photo Type")
    @allure.description("""
    Attempt to add a photo with an invalid photo type to an existing pet.

    Precondition:
    - User is authenticated and has a valid API key.
    - There is at least one pet in the list.

    Expected result:
    - The request returns a 400 error code, and the photo is not added.
    """)
    def test_add_pet_photo_invalid_photo_type(self, setup_key):
        pf.add_pet_photo(setup_key, 0, ph_invalid, "no", 400)

    @allure.title("Add Photo with Invalid Key")
    @allure.description("""
    Attempt to add a photo to a pet with an invalid API key.

    Precondition:
    - User is not authenticated.

    Expected result:
    - The request returns a 403 error code, and the photo is not added.
    """)
    def test_add_pet_photo_invalid_key(self):
        pf.add_pet_photo_invalid_key(0, ph, 403)

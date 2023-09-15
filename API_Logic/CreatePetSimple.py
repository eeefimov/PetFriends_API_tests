import json
from API_Logic.GetList import PetFriendsGetList


class PetFriendsCreatePetSimple(PetFriendsGetList):
    def __init__(self):
        super().__init__()

    def create_pet_simple(self, setup_key, name, animal_type, age, expected):
        """
        Create a pet with simple information.

        Precondition:
        - User is authenticated and has a valid API key.

        :param setup_key: Authentication key.
        :param name: Pet's name.
        :param animal_type: Pet's animal type.
        :param age: Pet's age.
        :param expected: Expected HTTP status code.
        """
        status, result = self.post_pet_without_photo(setup_key, name, animal_type, age)
        self.assert_and_print(status, result, expected)

        status, result = self.get_list_of_pets("GET", "my_pets", setup_key)

        print("New pet is in the list:", self.check_pet_is_in_the_list(result, name, age, animal_type))
        # return status, result

    def create_pet_invalid_key(self, setup_key, name, animal_type, age, expected):
        """
        Attempt to create a pet with an invalid API key.

        Precondition:
        - User is not authenticated (invalid API key is provided).

        :param setup_key: Invalid authentication key.
        :param name: Pet's name.
        :param animal_type: Pet's animal type.
        :param age: Pet's age.
        :param expected: Expected HTTP status code.
        """
        status, result = self.post_pet_without_photo(setup_key, name, animal_type, age)

        self.assert_and_print(status, result, expected)

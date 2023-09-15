import json

from API_Logic.GetList import PetFriendsGetList


class PetFriendsCreatePetSimple(PetFriendsGetList):
    def __init__(self):
        super().__init__()

    def create_pet_simple(self, setup_key, name, animal_type, age, expected):
        status, result = self.post_pet_without_photo(setup_key, name, animal_type, age)
        self.assert_and_print(status, result, expected)

        status, result = self.get_list_of_pets("GET", "my_pets", setup_key)

        print("New pet is in the list:", self.check_pet_is_in_the_list(result, name, age, animal_type))

    def create_pet_invalid_key(self, setup_key, name, animal_type, age, expected):
        status, result = self.post_pet_without_photo(setup_key, name, animal_type, age)

        self.assert_and_print(status, result, expected)

    def create_pet_check_json_fields_type(self, setup_key, name, animal_type, age, expected):
        self.create_pet_simple(setup_key, name, animal_type, age, expected)
        _, result = self.get_list_of_pets("GET", "my_pets", setup_key)
        print(type(result["animal_type"]))
        # assert type(result["created_at"]) == str
        # assert type(result["id"]) == str
        # assert type(result["name"]) == str
        # assert type(result["pet_photo"]) == str
        # assert type(result["age"]) == int









from API_Logic.CreatePetSimple import PetFriendsCreatePetSimple


class PetFriendCreatePetWithPhoto(PetFriendsCreatePetSimple):
    def __init__(self):
        super().__init__()

    def create_pet(self, setup_key, name, animal_type, age, photo, expected):
        status, result = self.post_pet_with_photo(setup_key, name, animal_type, age, photo)
        self.assert_and_print(status, result, expected)

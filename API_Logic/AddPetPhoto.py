from PetFriendsV3.API_Logic.GetList import PetFriendsGetList
from PetFriendsV3.TESTS.params import randomize_id


class PetFriendsAddPhoto(PetFriendsGetList):
    def __init__(self):
        super().__init__()

    def get_my_pet_id(self, key, i: int, condition: str):
        status, result = self.get_list_of_pets("GET", "my_pets", key)
        pet_id_no_photo = []
        pet_id_with_photo = []
        if len(result["pets"]) > 0:
            for _ in result["pets"]:
                if _["pet_photo"] == "" or None :
                    pet_id_no_photo.append(_["id"])
                else:
                    pet_id_with_photo.append(_["id"])
        else:
            print("There are no pets in the list")

        if condition == "no":
            print(pet_id_no_photo[i])
            return pet_id_no_photo[i]

        elif condition == "yes":
            print(pet_id_with_photo[i])
            return pet_id_with_photo[i]

        elif condition == "invalid_id":
            pet_id = randomize_id()
            return pet_id

    def add_pet_photo(self, key, i, ph, condition, expected):
        pet_id = self.get_my_pet_id(key, i, condition)
        status, result = self.post_photo_pet(key, pet_id, ph)
        self.assert_and_print(status, result, expected)

    def add_pet_photo_invalid_key(self, pet_id, photo_path, expected):
        header = {}
        header["auth_key"] = "invalid_key_here"
        status, result = self.post_photo_pet(header, pet_id, photo_path)
        self.assert_and_print(status, result, expected)
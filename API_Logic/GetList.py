from API_Logic.PetFriends import PetFriends


class PetFriendsGetList(PetFriends):
    def __init__(self):
        super().__init__()

    def get_pet_list_with_valid_filter(self, header, fltr, expected):
        status, result = self.get_list_of_pets("GET", fltr, header=header)
        self.assert_and_print(status, result, expected)

    def get_pet_list_with_invalid_key(self, header, fltr, expected):
        status, result = self.get_list_of_pets("GET", fltr, header=header)
        self.assert_and_print(status, result, expected)

    def get_pet_list_with_no_key(self, fltr, expected):
        header = None
        status, result = self.get_list_of_pets("GET", fltr, header=header)
        self.assert_and_print(status, result, expected)

    def get_pet_list_with_invalid_filter(self, header, fltr, expected):
        status, result = self.get_list_of_pets("GET", fltr, header=header)
        self.assert_and_print(status, result, expected)

    def get_pet_list_with_other_methods(self, header, fltr, expected, method):
        mtd = str(method)
        status, result = self.get_list_of_pets(mtd, fltr, header=header)
        self.assert_and_print(status, result, expected)

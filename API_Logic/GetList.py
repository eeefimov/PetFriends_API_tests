from API_Logic.PetFriends import PetFriends


class PetFriendsGetList(PetFriends):
    def __init__(self):
        super().__init__()

    def get_list_validation(self, setup_key, filter, expected):
        status, result = self.get_list_of_pets("GET", filter, header=setup_key)

        self.assert_and_print(status, result, expected)

    def get_list_other_methods(self, setup_key, filter, expected, method):
        mtd = str(method)
        status, result = self.get_list_of_pets(mtd, filter, header=setup_key)

        self.assert_and_print(status, result, expected)

    def get_list_invalid_filter(self, setup_key, filter, expected):
        status, result = self.get_list_of_pets("GET", filter, header=setup_key)

        self.assert_and_print(status, result, expected)





from PetFriendsV3.API_Logic.PetFriends import PetFriends


class PetFriendsGetList(PetFriends):
    def __init__(self):
        super().__init__()

    def get_pet_list_with_valid_filter(self, header, filter, expected):
        status, result = self.get_list_of_pets("GET", filter, header=header)
        self.assert_and_print(status, result, expected)
        # return status, result

    #
    # def get_pet_list_with_valid_filter(self, setup_key, filter, expected):
    #     """
    #     Get the list of pets with a valid filter and validate the response.
    #
    #     Args:
    #         setup_key (dict): The API key for authentication.
    #         filter (str): The filter to be applied.
    #         expected (int): The expected HTTP status code.
    #
    #     Returns:
    #         None
    #     """
    #     status, result = self.get_list_of_pets("GET", filter, header=setup_key)
    #     self.assert_and_print(status, result, expected)

    def get_pet_list_with_invalid_key(self, header, filter, expected):
        status, result = self.get_list_of_pets("GET", filter, header=header)
        self.assert_and_print(status, result, expected)
        # return status, result
    # def get_pet_list_with_invalid_filter(self, setup_key, filter, expected):
    #     """
    #     Get the list of pets with an invalid filter and validate the response.
    #
    #     Args:
    #         setup_key (dict): The API key for authentication.
    #         filter (str): The filter to be applied.
    #         expected (int): The expected HTTP status code.
    #
    #     Returns:
    #         None
    #     """
    #     status, result = self.get_list_of_pets("GET", filter, header=setup_key)
    #     self.assert_and_print(status, result, expected)
    def get_pet_list_with_no_key(self, filter, expected):
        header = None
        status, result = self.get_list_of_pets("GET", filter, header=header)
        self.assert_and_print(status, result, expected)
        # return status, result

    def get_pet_list_with_invalid_filter(self, header, filter, expected):
        status, result = self.get_list_of_pets("GET", filter, header=header)
        self.assert_and_print(status, result, expected)
        # return status, result

    def get_pet_list_with_other_methods(self, header, filter, expected, method):
        mtd = str(method)
        status, result = self.get_list_of_pets(mtd, filter, header=header)
        self.assert_and_print(status, result, expected)
        # return status, result
    #
    # def get_pet_list_with_other_methods(self, setup_key, filter, expected, method):
    #     """
    #     Get the list of pets using HTTP methods other than GET and validate the response.
    #
    #     Args:
    #         setup_key (dict): The API key for authentication.
    #         filter (str): The filter to be applied.
    #         expected (int): The expected HTTP status code.
    #         method (str): The HTTP method to use (e.g., "PUT", "POST", "DELETE").
    #
    #     Returns:
    #         None
    #     """
    #     mtd = str(method)
    #     status, result = self.get_list_of_pets(mtd, filter, header=setup_key)
    #     self.assert_and_print(status, result, expected)
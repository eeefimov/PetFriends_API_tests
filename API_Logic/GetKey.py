from PetFriendsV3.API_Logic.PetFriends import PetFriends


class PetFriendsGetKey(PetFriends):
    def __init__(self):
        super().__init__()

    def get_api_key_validation(self, email, password, expect):
        status, result = self.get_api_key(email, password)
        assert status == expect
        if status == 200:
            assert "key" in self.auth_key
        print("\n", self.header)
        print(self.auth_key)
        print(status)
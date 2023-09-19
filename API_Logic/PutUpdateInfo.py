from API_Logic.PetFriends import PetFriends
from TESTS.params import randomize_number, randomize_string


class PetFriendUpdatePet(PetFriends):
    def __init__(self):
        super().__init__()

    def get_pet_id(self, header, pet_num: int):
        num = pet_num
        status, result = self.get_list_of_pets("GET", "my_pets", header)
        pet_data = result.get('pets')
        if num is None:
            pet = self.check_pet_is_in_the_list(result, pet_data[0]['name'],
                                                pet_data[0]['age'], pet_data[0]['animal_type'])
        else:
            pet = self.check_pet_is_in_the_list(result, pet_data[num]['name'],
                                                pet_data[num]['age'], pet_data[num]['animal_type'])

        return pet['id'], pet

    def update_pet_info(self, header, pet_num: int, expected):
        pet_id, old_pet_info = self.get_pet_id(header, pet_num)
        name = randomize_string(10)
        animal_type = randomize_string(10)
        age = randomize_number(10)
        status, result = self.put_pet_info(header, pet_id, name, animal_type, age)
        self.assert_and_print(status, result, expected)

        _, new_pet_info = self.get_pet_id(header, pet_num)
        print(old_pet_info)
        print(new_pet_info)

    def update_pet_info_invalid_key(self, header_valid, header_invalid, pet_num, expected):
        self.get_pet_id(header_valid, pet_num)

        status, result = self.put_pet_info(header_invalid, id, randomize_string(5),
                                           randomize_string(5), randomize_number(10))
        self.assert_and_print(status, result, expected)

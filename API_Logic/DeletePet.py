from API_Logic.GetList import PetFriendsGetList
from TESTS.params import randomize_number


class PetFriendsDeletePet(PetFriendsGetList):
    def __init__(self):
        super().__init__()

    def delete_first_valid_pet(self, setup_key, pet_num: int):
        num = pet_num
        status, result = self.get_list_of_pets("GET", "my_pets", setup_key)
        pet_data = result.get('pets')
        num_pets_was = len(pet_data)

        print(f"\nNumber of my pets was:{num_pets_was}")

        if num == None:
            pet = self.check_pet_is_in_the_list(result, pet_data[0]['name'], pet_data[0]['age'], pet_data[0]['animal_type'])
        else:
            pet = self.check_pet_is_in_the_list(result, pet_data[num]['name'], pet_data[num]['age'],
                                                pet_data[num]['animal_type'])
        print("\n", pet)
        print("\n", pet['id'])

        status = self.delete_pet(setup_key, pet['id'])

        print(status)

        _, result = self.get_list_of_pets("GET", "my_pets", setup_key)
        num_pets_is = len(result.get('pets'))

        print(f"Number of my pets is:{num_pets_is}")
        assert num_pets_was == num_pets_is + 1

    def delete_randome_valid_pet(self, setup_key):
        status, result = self.get_list_of_pets("GET", "my_pets", setup_key)
        pet_data = result.get('pets')
        num = randomize_number(len(pet_data))
        if num != 0:
            self.delete_first_valid_pet(setup_key, num)
        else:
            print("\nThere is no pet in the list")

    def delete_pet_invalid_id(self, setup_key, setup_id):
        status = self.delete_pet(setup_key, setup_id)

        print("\n", status)
        print(setup_id)
        assert status == 403


PTD = PetFriendsDeletePet()
dl = PTD.delete_first_valid_pet


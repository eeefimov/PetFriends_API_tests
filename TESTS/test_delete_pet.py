from main import PetFriends

pets = PetFriends()

"""valid data"""
def test_delete_pets(setup_key_pet_id):
    header, pet_id = setup_key_pet_id
    _, result = pets.get_list_of_pets("GET", "my_pets", header)
    status, _ = pets.delete_pet(header, pet_id)
    assert status == 200
    _, result_deleted = pets.get_list_of_pets("GET", "my_pets", header)
    assert len(result["pets"]) == len(result_deleted["pets"]) + 1

"""Invalid key"""
def test_delete_pets(setup_key, setup_key_pet_id):
    header = setup_key
    _, pet_id = setup_key_pet_id
    _, result = pets.get_list_of_pets("GET", "my_pets", header)
    status, _ = pets.delete_pet(header, pet_id)
    assert status == 200
    _, result_deleted = pets.get_list_of_pets("GET", "my_pets", header)
    assert len(result["pets"]) == len(result_deleted["pets"]) + 1
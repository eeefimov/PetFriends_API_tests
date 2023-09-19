from typing import Union, Any

import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.main_url = "https://petfriends.skillfactory.ru/"
        self.email = None,
        self.password = None
        self.header = {}
        self.auth_key = None

    def get_api_key(self, email, password):
        api_url = self.main_url + str("api/key")

        self.header["password"] = password
        self.header["email"] = email
        self.header["Content-Type"] = "application/json"

        req = requests.get(api_url, headers=self.header)
        status = req.status_code
        try:
            result = req.json()
            self.auth_key = result
        except json.decoder.JSONDecodeError:
            result = req.text

        return status, result

    @staticmethod
    def assert_and_print(status, result, expected):
        assert status == expected
        print("\n", result, "\n")
        print(status)

    def get_list_of_pets(self, method, fltr, header) -> tuple[int, Union[str, Any]]:
        fltr = {"filter": fltr}
        api_url = self.main_url + str("api/pets")
        req = None
        if method == "GET":
            req = requests.get(api_url, headers=header, params=fltr)
        elif method == "PUT":
            req = requests.put(api_url, headers=self.header, params=fltr)
        elif method == "POST":
            req = requests.post(api_url, headers=self.header, params=fltr)
        status = req.status_code
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text

        return status, result

    @staticmethod
    def check_pet_is_in_the_list(result, name, age, animal_type):
        pet_data = result.get('pets')
        if pet_data:
            for i in range(len(pet_data)):
                if(
                    pet_data[i]['name'] == name and
                    pet_data[i]['age'] == str(age) and
                    pet_data[i]['animal_type'] == animal_type
                ):
                    print("\nPet is in the list")
                    assert True
                    break
        else:
            print("Pet is not in the list")

        return pet_data[0]

    def delete_pet(self, setup_key, pet_id):
        api_url = self.main_url + str("api/pets/") + str(pet_id)
        res = requests.delete(api_url, headers=setup_key)
        status = res.status_code
        return status

    def post_pet_without_photo(self, hd, nm, at, ag):
        api_url = self.main_url + str("api/create_pet_simple")
        data = {"name": nm, "animal_type": at, "age": ag}
        req = requests.post(api_url, headers=hd, data=data)
        status = req.status_code
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def post_pet_with_photo(self, setup_key, nm, at, ag, ph):
        api_url = self.main_url + str("api/pets")
        fields = {"name": nm,
                  "animal_type": at,
                  "age": ag,
                  "pet_photo": (ph, open(ph, 'rb'), 'Images/*')
                  }
        data = MultipartEncoder(fields=fields)
        hdd = setup_key["auth_key"]
        headers = {'auth_key': hdd, 'Content-Type': data.content_type}
        req = requests.post(api_url, headers=headers, data=data)
        status = req.status_code
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def post_photo_pet(self, key, pet_id, ph):
        api_url = self.main_url + f"api/pets/set_photo/{pet_id}"
        fields = {"pet_photo": (ph, open(ph, 'rb'), 'image/*')}
        data = MultipartEncoder(fields=fields)
        hdd = key["auth_key"]
        headers = {'auth_key': hdd, 'Content-Type': data.content_type}
        req = requests.post(api_url, headers=headers, data=data)
        status = req.status_code
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def put_pet_info(self, auth_key, pet_id, nm, at, ag):
        api_url = self.main_url + str("api/pets/") + str(pet_id)
        print(api_url)
        data = {"name": nm, "animal_type": at, "age": ag}

        headers = {'auth_key': auth_key["auth_key"]}
        res = requests.put(api_url, headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

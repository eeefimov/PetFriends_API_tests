import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os

'''api SWAGGER DOC url: https://petfriends.skillfactory.ru/apidocs/#/

list of default api: 

POST /api/create_pet_simple
Add information about new pet without photo

GET /api/key
Get API key

GET /api/pets
Get list of pets

POST /api/pets
Add information about new pet

POST /api/pets/set_photo/{pet_id}
Add photo of pet

DELETE /api/pets/{pet_id}
Delete pet from database

PUT /api/pets/{pet_id}
Update information about pet
'''


class PetFriends:
    def __init__(self):
        self.main_url = "https://petfriends.skillfactory.ru/"
        self.email = None,
        self.password = None
        self.header = {}
        self.auth_key = None

    def get_api_key(self, em, ps):
        api_url = self.main_url + str("api/key")
        self.header["password"] = ps
        self.header["email"] = em
        self.header["Content-Type"] = "application/json"
        req = requests.get(api_url, headers=self.header)
        status = req.status_code
        try:
            result = req.json()
            self.auth_key = result
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def get_list_of_pets(self, method, filter, header) -> str:
        filter = {"filter": filter}
        api_url = self.main_url + str("api/pets")
        req = None
        if method == "GET":
            req = requests.get(api_url, headers=header, params=filter)
        elif method == "PUT":
            req = requests.put(api_url, headers=self.header, params=filter)
        elif method == "PATCH":
            req = requests.post(api_url, headers=self.header, params=filter)
        elif method == "DELETE":
            req = requests.delete(api_url, headers=self.header, params=filter)
        status = req.status_code
        result = None
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def post_pet_without_photo(self, hd, nm, at, ag):
        api_url = self.main_url + str("api/create_pet_simple")
        data = {"name": nm, "animal_type": at, "age": ag}
        req = requests.post(api_url, headers=hd, data=data)
        status = req.status_code
        result = None
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def post_pet_with_photo(self, auth_key: json, nm, at, ag, ph):
        api_url = self.main_url + str("api/pets")
        fields={"name": nm,
                "animal_type": at,
                "age": ag,
                "pet_photo": (ph, open(ph, 'rb'), 'image/*')
                }
        data = MultipartEncoder(fields=fields)
        headers = {'auth_key': auth_key["auth_key"], 'Content-Type': data.content_type}
        req = requests.post(api_url, headers=headers, data=data)
        status = req.status_code
        result = None
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text
        return status, result

    def post_photo_pet(self, auth_key, pet_id, ph):
        api_url = self.main_url + str("api/pets/set_photo/") + str(pet_id)
        fields = {"pet_photo": (ph, open(ph, 'rb'), 'image/*')}
        data = MultipartEncoder(fields=fields)
        headers = {'auth_key': auth_key["auth_key"], 'Content-Type': data.content_type}
        res = requests.post(api_url, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_pet_info(self, auth_key, pet_id, nm, at, ag):
        api_url = self.main_url + str("api/pets/") + str(pet_id)
        print(api_url)
        data = {"name": nm, "animal_type": at, "age": ag}

        headers = {'auth_key': auth_key["auth_key"]}
        res = requests.put(api_url, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pet(self, hd, pet_id):
        api_url = self.main_url + str("api/pets/") + str(pet_id)
        res = requests.delete(api_url, headers=hd)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status
# PetFriends
requirements.txt file is included. (Libs for all tests)

TESTS Folder

Automate tests for https://petfriends.skillfactory.ru/ API site. API documentation provided via Flasgger https://petfriends.skillfactory.ru/apidocs/ LIST of default api:

POST /api/create_pet_simple Add information about new pet without photo

GET /api/key Get API key

GET /api/pets Get list of pets

POST /api/pets Add information about new pet

POST /api/pets/set_photo/{pet_id} Add photo of pet

DELETE /api/pets/{pet_id} Delete pet from database

PUT /api/pets/{pet_id} Update information about pet

TESTS_Selenium folder:

Check Login

Check Numbers of "my_pets" items

Check pages title
import pytest
import os
from TESTS.settings import valid_password, valid_email
from API_Logic.PetFriends import PetFriends
import random
import string
import uuid

#pets = PetFriends()


def randomize_string(number: int):
    symbols = string.ascii_letters
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_id():
    random_id = "qweweq"#str(uuid.uuid4())
    return random_id


def randomize_number(n):
    random_number = random.randint(0, n)
    return random_number


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def latin_chars():
    return 'qazxswedcvfrtgbnhyujmkiolp'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

# Authentication Positive Test Parameters
params_auth_positive = [
    pytest.param(valid_email, valid_password, 200, id="Valid email and pass")
]

# Authentication Negative Test Parameters
params_auth_negative = [
    pytest.param(randomize_string(10), randomize_string(10), 403, id="Invalid email and pass"),
    pytest.param("", "", 403, id="Empty fields"),
    pytest.param(valid_email, "", 403, id="Empty pass"),
    pytest.param(valid_email, randomize_string(10), 403, id="Empty pass")
]

# Filter Valid Test Parameters
params_filter_valid = [
    pytest.param("my_pets", 200, id="Valid filter: my_pets"),
    pytest.param(None, 200, id="Valid filter: empty (list of all pets)")
]

# Filter Methods Test Parameters
params_filter_methods = [
    pytest.param("my_pets", 405, "PUT", id="Valid filter: PUT"),
    pytest.param("my_pets", 405, "DELETE", id="Valid filter: DELETE"),
    pytest.param("my_pets", 400, "POST", id="Valid filter: POST")
]

# Filter Invalid Test Parameters
params_filter_invalid = [
    pytest.param(" ", 422, id="Valid filter: empty (list of all pets) "),
    pytest.param(latin_chars(), 422, id="Invalid filter: Latin"),
    pytest.param(russian_chars(), 422, id="Invalid filter: Cyrillic"),
    pytest.param(chinese_chars(), 422, id="Invalid filter: Chinese"),
    pytest.param(special_chars(), 422, id="Invalid filter: Special chars"),
    pytest.param(randomize_string(1), 422, id="Invalid filter: Short string"),
    pytest.param(randomize_string(255), 422, id="Invalid filter: 255 string"),
    pytest.param(randomize_string(1000), 422, id="Invalid filter: 1000 string"),
    pytest.param(randomize_number(10), 422, id="Invalid filter: Number")
]

# Add Pet No Photo Valid Test Parameters
params_add_pet_nophoto_valid = [
    pytest.param(randomize_string(10), randomize_string(10), (randomize_number(10)), 200, id="Valid values")
]

# Add Pet No Photo Invalid Key Test Parameters
params_add_pet_nophoto_invalid_key = [
    pytest.param(randomize_string(10), randomize_string(10), (randomize_number(10)), 403, id="Valid values")
]

# Add Pet Check String Fields Special Test Parameters
params_add_pet_check_string_fields_special = [
    pytest.param(russian_chars(), russian_chars(), russian_chars(), 200, id="Cyrillic abs"),
    pytest.param(chinese_chars(), chinese_chars(), chinese_chars(), 200, id="Chines abs"),
    pytest.param(special_chars(), special_chars(), special_chars(), 400, id="Special chars")
]

# Add Pet Check Age Numbers Test Parameters
params_add_pet_check_age_numbers = [
    pytest.param(randomize_string(5), randomize_string(5), -10, 400, id="Valid strings; {age} < 0 "),
    pytest.param(randomize_string(5), randomize_string(5), 0, 200, id="Valid strings; {age} = 0 "),
    pytest.param(randomize_string(5), randomize_string(5), 10.6, 200, id="Valid strings; {age} float"),
    pytest.param(randomize_string(5), randomize_string(5), randomize_number(1000), 400, id="Valid strings; {age} 1000"),
]

# ID Invalid Test Parameters
params_id_invalid = [
    pytest.param(randomize_id(), 403, id="Invalid ID")
]

current_dir = os.path.dirname(__file__)
valid_pet_photo = os.path.join(current_dir, "Images", "corgi.jpeg")
valid_pet_photo_png = os.path.join(current_dir, "Images", "img.png")
invalid_pet_photo_txt = os.path.join(current_dir, "Images", "requirements.txt")
invalid_pet_photo_broken_jpeg = os.path.join(current_dir, "Images", "requirements.jpeg")

# Add Pet With Photo Valid Test Parameters
params_add_pet_with_photo_valid = [
    pytest.param(randomize_string(10),
                 randomize_string(10),
                 str(randomize_number(10)),
                 valid_pet_photo,
                 200,
                 id="Valid values")
]

# Add Pet Photo Valid Test Parameters
params_add_pet_photo_valid = [
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), valid_pet_photo, 200, id="Valid data")
]
params_add_pet_empty_fields = [
    pytest.param(randomize_string(10), randomize_string(10), None, 400, id="None age"),
    pytest.param(randomize_string(10), None, str(randomize_number(10)), 400, id="None animal_type"),
    pytest.param(None, randomize_string(10), str(randomize_number(10)), 400, id="None name"),
    pytest.param(None, None, None, 400, id="None name, animal_type, age"),
]

# Add Pet Photo Empty Fields Test Parameters
params_add_pet_photo_empty_fields = [
    pytest.param(randomize_string(10), randomize_string(10), None, valid_pet_photo, 400, id="None age"),
    pytest.param(randomize_string(10), None, str(randomize_number(10)), valid_pet_photo, 400, id="None animal_type"),
    pytest.param(None, randomize_string(10), str(randomize_number(10)), valid_pet_photo, 400, id="None name"),
    pytest.param(None, None, None, valid_pet_photo, 400, id="None name, animal_type, age")
]

# Add Pet Photo Type Test Parameters
params_add_pet_photo_type = [
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), invalid_pet_photo_txt, 400, id="Photo = txt"),
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), invalid_pet_photo_broken_jpeg, 400, id="Photo = broken jpeg"),
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), valid_pet_photo_png, 200, id="Photo = png")
]

params_add_pet_check_string_fields = [
    pytest.param(randomize_string(1), randomize_string(1), randomize_number(10), id="1 char strings; Valid {age} "),
    pytest.param(randomize_string(255), randomize_string(255), randomize_number(10), id="255 char strings; Valid {age} "),
    pytest.param(randomize_string(1000), randomize_string(1000), randomize_number(10), id="1000 char strings; Valid {age} ")
]

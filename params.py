import pytest
from settings import valid_password, valid_email
from main import PetFriends
import random
import string
import uuid

pets = PetFriends()

def randomize_string(number: int):
    symbols = string.ascii_letters
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_id():
    random_id = str(uuid.uuid4())
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


params_auth_positive = [
    pytest.param(valid_email, valid_password, 200, id="Valid email and pass")
]
params_auth_negative = [
    pytest.param(randomize_string(10), randomize_string(10), 403, id="Invalid email and pass"),
    pytest.param("", "", 403, id="Empty fields"),
    pytest.param(valid_email, "", 403, id="Empty pass"),
]
params_filter_valid = [
    pytest.param("my_pets", id="Valid filter: my_pets"),
    pytest.param(None, id="Valid filter: empty (list of all pets) ")
]
params_filter_json_fields = [
    pytest.param("age", id="json age"),
    pytest.param("animal_type", id="json animal type"),
    pytest.param("created_at", id="json created at"),
    pytest.param("id", id="json pet id"),
    pytest.param("name", id="json pet name"),
    pytest.param("pet_photo", id="json pet photo")
]
params_filter_methods = [
    pytest.param("my_pets", "PUT", id="Valid filter: PUT"),
    pytest.param("my_pets", "DELETE", id="Valid filter: DELETE"),
    pytest.param("my_pets", "PATCH", id="Valid filter: PATCH")
]
params_filter_invalid = [
    pytest.param(" ", id="Valid filter: empty (list of all pets) "),
    pytest.param(latin_chars(), id="INvalid filter: Latin"),
    pytest.param(russian_chars(), id="INvalid filter: Cyrillic"),
    pytest.param(chinese_chars(), id="INvalid filter: Chinese"),
    pytest.param(special_chars(), id="INvalid filter: Special chars"),
    pytest.param(randomize_string(1), id="INvalid filter: Short string"),
    pytest.param(randomize_string(255), id="INvalid filter: 255 string"),
    pytest.param(randomize_string(1000), id="INvalid filter: 1000 string"),
    pytest.param(randomize_number(10), id="INvalid filter: Number")
]

#BUG1: age(Number) -> get string
params_add_pet_nophoto_valid = [
    pytest.param(randomize_string(10), randomize_string(10), (randomize_number(10)), id="Valid values")
]

#BUG6: add pet with photo, without requered field(s)
params_add_pet_empty_fields = [
    pytest.param(randomize_string(10), randomize_string(10), None, id="Valid strings; None age"),
    pytest.param(randomize_string(10), None, None, id="Valid Name; None {animal type} and {age}"),
    pytest.param(None, None, None, id="All fields are None"),
    pytest.param(None, randomize_string(10), None, id="None Name; Valid {animal type} and None {age}"),
    pytest.param(None, randomize_string(10), str(randomize_number(10)), id="None Name; Valid {animal type} and Valid {age}"),
    pytest.param(None, None, str(randomize_number(10)), id="None strings; {age} valid"),
]

#BUG2: name(String), animal_type(String) -> get numbers
params_add_pet_invalid_data_type = [
    pytest.param(randomize_string(5), randomize_string(5), randomize_string(5), id="Valid strings; INvalid {age} "),
    pytest.param(randomize_number(10), randomize_number(10), randomize_string(5), id="INValid strings; INvalid {age}"),
]

#BUG3: string fields have no limit in length (new pet without and with photo)
params_add_pet_check_string_fields = [
    pytest.param(randomize_string(1), randomize_string(1), randomize_number(10), id="1 char strings; Valid {age} "),
    pytest.param(randomize_string(255), randomize_string(255), randomize_number(10), id="255 char strings; Valid {age} "),
    pytest.param(randomize_string(1000), randomize_string(1000), randomize_number(10), id="1000 char strings; Valid {age} ")
]

#BUG4: string fields have no limit in chars
params_add_pet_check_string_fields_special = [
    pytest.param(russian_chars(), russian_chars(), russian_chars(), 200, id="Cyrillic abs"),
    pytest.param(chinese_chars(), chinese_chars(), chinese_chars(), 200, id="Chines abs"),
    pytest.param(special_chars(), special_chars(), special_chars(), 400, id="Special chars")
]

#BUG5: age field accept <0, floats and more lage numbers
params_add_pet_check_age_numbers = [
    pytest.param(randomize_string(5), randomize_string(5), -10, 400, id="Valid strings; {age} < 0 "),
    pytest.param(randomize_string(5), randomize_string(5), 0, 200, id="Valid strings; {age} = 0 "),
    pytest.param(randomize_string(5), randomize_string(5), 10.6, 200, id="Valid strings; {age} float"),
    pytest.param(randomize_string(5), randomize_string(5), randomize_number(1000), 400, id="Valid strings; {age} 1000"),
]

params_id_invalid = [
    pytest.param(randomize_id(), 400, id="Invalid ID"),
    pytest.param("", 404, id="Empty ID")
]

#BUG1.1: age(Number) -> get string
params_add_pet_photo_valid = [
    pytest.param(randomize_string(10), randomize_string(10), randomize_number(10), "images/corgi.jpeg", id="Valid data")
]

#BUGx: add pet with invalid photo file, with no photo file.
params_add_pet_invalid_photo = [
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), "images/img.png", id="img_Png photo"),
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), "images/corgi.jpg", id="corgi_jpg photo"),
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), "images/requirements.jpeg", id="Error photo"),
    pytest.param(randomize_string(10), randomize_string(10), str(randomize_number(10)), "images/requirements.txt", id="TXT photo"),
]

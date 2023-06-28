import pytest
from settings import valid_password, valid_email
from main import PetFriends
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def setup_key():
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    header["auth_key"] = pets_f.auth_key["key"]
    yield header

@pytest.fixture()
def setup_invalid_key():
    header = {}
    header["auth_key"] = "pets_f.auth_key"
    yield header


@pytest.fixture()
def setup_key_pet_id():
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    pet_id = []
    header["auth_key"] = pets_f.auth_key["key"]
    status, result = pets_f.get_list_of_pets("GET", "my_pets", header=header)

    if len(result["pets"]) > 0:
        for _ in result["pets"]:
            pet_id.append(_["id"])

    yield header, pet_id[0]


@pytest.fixture()
def setup_pet_id_and_photo():
    pets_f = PetFriends()
    pets_f.get_api_key(valid_email, valid_password)
    header = {}
    pet_id = []
    pet_photo = "images/corgi.jpeg"
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    header["auth_key"] = pets_f.auth_key["key"]
    status, result = pets_f.get_list_of_pets("GET", "my_pets", header=header)
    for _ in result["pets"]:
        if len(result["pets"]) > 0 and _["pet_photo"] == "":
            pet_id.append(_["id"])

    yield header, pet_id[0], pet_photo


@pytest.fixture(scope="session")
def setup():
    service = ChromeService(executable_path=ChromeDriverManager().download_and_install())
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.get('http://petfriends.skillfactory.ru')
    driver.find_element(By.CLASS_NAME, 'btn-success').click()

    WDW(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form > div:nth-of-type(4) > a')))
    driver.find_element(By.CSS_SELECTOR, 'form > div:nth-of-type(4) > a').click()
    WDW(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#email')))
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(valid_email)
    driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys(valid_password)
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > button").click()

    yield driver

    driver.quit()



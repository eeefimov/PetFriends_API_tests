import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

def test_login_and_auth(setup):
    """
    Precondition: registered user
    Valid user(email, password). Login and check ALL pets cards.
    """
    setup.get('http://petfriends.skillfactory.ru')
    setup.find_element(By.CLASS_NAME, 'btn-success').click()

    WDW(setup, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form > div:nth-of-type(4) > a')))
    setup.find_element(By.CSS_SELECTOR, 'form > div:nth-of-type(4) > a').click()
    WDW(setup, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#email')))
    setup.find_element(By.CSS_SELECTOR, "input#email").send_keys(valid_email)
    setup.find_element(By.CSS_SELECTOR, "input#pass").send_keys(valid_password)
    setup.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > button").click()

    WDW(setup, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'card-deck')))

    assert setup.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    assert setup.find_element(By.CLASS_NAME, 'card-deck').is_displayed()

    setup.save_screenshot("Pets_card_desk.png")
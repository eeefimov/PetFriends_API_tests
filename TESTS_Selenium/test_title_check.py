from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password


def test_pages_title(setup):
    """
    Check titles on the pages
    """
    main_title = "PetFriends"
    new_user_title = "PetFriends: New User"
    login_title = "PetFriends: Login"
    all_pets_title = "PetFriends: All Pets"

    setup.get('http://petfriends.skillfactory.ru')
    assert setup.title == main_title
    setup.find_element(By.CLASS_NAME, 'btn-success').click()

    wait = WDW(setup, 2)
    wait.until(EC.title_is(new_user_title))
    
    assert setup.title == new_user_title
    setup.find_element(By.LINK_TEXT, "У меня уже есть аккаунт").click()

    wait = WDW(setup, 2)
    wait.until(EC.title_is(login_title))

    assert login_title == setup.title
    setup.find_element(By.CSS_SELECTOR, "input#email").send_keys(valid_email)
    setup.find_element(By.CSS_SELECTOR, "input#pass").send_keys(valid_password)
    setup.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > button").click()

    setup.implicitly_wait(10)
    assert setup.title == all_pets_title

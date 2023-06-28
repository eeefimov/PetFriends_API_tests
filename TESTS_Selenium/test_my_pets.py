from settings import user_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

def test_login_check_my_pets(browser):
    """
      Valid user(email, password). Login and check My_pets cards.
      """
    browser.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    WDW(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.\.col-sm-4.left > h2')))
    name = browser.find_element(By.CSS_SELECTOR, 'div.\.col-sm-4.left > h2').text
    assert name == user_name
    assert browser.find_element(By.CLASS_NAME, 'table-hover').is_displayed()
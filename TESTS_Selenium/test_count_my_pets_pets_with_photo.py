from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_count_my_pets(browser):
    """
      Valid user(email, password). Count all pets cards.
      """
    browser.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    WDW(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'table-hover')))

    pets_number = browser.find_element(By.CSS_SELECTOR, ".\\.col-sm-4").text
    start_pos = pets_number.index(": ") + 2
    end_pos = pets_number.index("Д")
    num = int(pets_number[start_pos:end_pos])

    img = 0
    num2 = 0
    """
    because pets info could be empty, we search list line in the frame. 
    + 1 line for titles.
    
    check more than half pets have photo
    """
    for n in browser.find_elements(By.TAG_NAME, "tr"):
        num2 = num2 + 1
    assert num == num2 - 1
    print(num)
    print(num2)

    for i in browser.find_elements(By.XPATH, "//img"):
        if i.get_attribute("src").startswith("data:image"):
            img = img + 1

    assert (num / 2) < img
    print(img)

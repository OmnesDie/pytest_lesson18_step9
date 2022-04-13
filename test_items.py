from selenium.webdriver.common.by import By
import pytest
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.ID, "add_to_basket_form"), "кнопка отсутствует"


if __name__ == "__main__":
    pytest.main()
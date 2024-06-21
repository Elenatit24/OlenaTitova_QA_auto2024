import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.mark.ui
def test_check_incorrect_username():
    # створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login 
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(ChromeDriverManager.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адрІесу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
    time.sleep(3)

    

    # Закриваємо браузер
    driver.close()

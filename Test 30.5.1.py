import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC


chromedriver_autoinstaller.install()


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    driver.maximize_window()
    yield driver

    driver.quit()

def test_show_my_pets(driver):
    wdw(driver, 5).until(EC.presence_of_element_located((By.ID,'email')))
    driver.find_element(By.ID, 'email').send_keys('123454545@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что зашли на главную страницу
    assert driver.find_element(By.TAG_NAME, 'h1').text != 'PetFriends'
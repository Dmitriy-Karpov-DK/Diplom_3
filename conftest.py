import pytest
import requests
import allure

from selenium import webdriver
from constants import Constants


@allure.step('Инициализируем браузер и после действий удаляем')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Constants.URL_BASE)
        yield driver
        driver.quit()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Constants.URL_BASE)
        yield driver
        driver.quit()
    else:
        pass


@allure.step('Создаем пользователя и после действий удаляем')
@pytest.fixture()
def create_user():
    payload = {
        "email": Constants.TEST_USER_EMAIL,
        "password": Constants.TEST_USER_PASSWORD,
        "name": Constants.TEST_USER_NAME
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
    acc_token = response.json()["accessToken"]

    yield response

    headers = {"Authorization": acc_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

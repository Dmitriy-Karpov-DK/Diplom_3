import allure

from pages.page_personal_account import LoginPage
from locators.base_pages_locators import LocatorBasePages
from constants import Constants


class TestPersonalAccount:

    @allure.title('Проверим переход по клику на Личный кабинет')
    def test_click_personal_account_goto_successful(self, driver):
        test_page = LoginPage(driver)
        test_page.go_to_url(Constants.URL_BASE)
        test_page.click_on_personal_account()
        test_page.expectation(LocatorBasePages.NAME_ENTER_IN_PERSONAL_ACCOUNT)
        assert test_page.get_url() == Constants.URL_LOGIN

    @allure.title('Проверим переход в раздел История заказов')
    def test_click_order_history_goto_successful(self, driver, create_user):

        test_page = LoginPage(driver)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.set_email(Constants.TEST_USER_EMAIL)
        test_page.set_password(Constants.TEST_USER_PASSWORD)
        test_page.click_on_enter()
        test_page.expectation(LocatorBasePages.COUNTER_ANY_INGREDIENT)
        test_page.click_on_personal_account()
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDER_HISTORY)
        test_page.click_on_order_history()
        assert test_page.get_url() == Constants.URL_ACCOUNT_ORDER_HISTORY

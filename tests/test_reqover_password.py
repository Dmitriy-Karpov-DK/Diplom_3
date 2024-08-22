import allure

from pages.page_personal_account import LoginPage
from locators.base_pages_locators import LocatorBasePages
from constants import Constants


class TestRecoverPassword:

    @allure.title('Проверяем переход по кнопке Восстановить пароль')
    def test_click_button_restore_pass_go_to_page_recover_pass_successful(self, driver):
        test_page = LoginPage(driver)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.wait_clickable(LocatorBasePages.BUTTON_RECOVER_PASSWORD)
        test_page.click_on_recover_password()
        test_page.expectation(LocatorBasePages.FIELD_INPUT_EMAIL)
        assert test_page.get_answer_text(
            LocatorBasePages.NAME_RECOVER_PASSWORD) == Constants.TEXT_NAME_RECOVER_PASSWORD

    @allure.title('Проверяем ввод почты')
    def test_input_email_successful(self, driver):
        test_page = LoginPage(driver)
        test_page.go_to_url(Constants.URL_FORGOT_PASSWORD)
        test_page.expectation(LocatorBasePages.FIELD_INPUT_EMAIL)
        test_page.set_email("Fake@qw.qw")
        assert test_page.get_attribute_text(
            LocatorBasePages.FIELD_INPUT_EMAIL, "value") == "Fake@qw.qw"

    @allure.title('Проверяем клик по кнопке Восстановить')
    def test_input_email_click_button_restore_successful(self, driver):
        test_page = LoginPage(driver)
        test_page.go_to_url(Constants.URL_FORGOT_PASSWORD)
        test_page.expectation(LocatorBasePages.FIELD_INPUT_EMAIL)
        test_page.click_on_recovery()
        test_page.expectation(LocatorBasePages.BUTTON_SAVE_IN_RECOVER_PASSWORD)
        assert test_page.get_url() == Constants.URL_RESET_PASSWORD

    @allure.title('Проверяем клик по кнопке показать-скрыть пароль')
    def test_click_button_show_hide_password_makes_field_active_highlights(self, driver):
        test_page = LoginPage(driver)
        test_page.go_to_url(Constants.URL_FORGOT_PASSWORD)
        test_page.click_on_recovery()
        test_page.wait_clickable(LocatorBasePages.BUTTON_SHOW_PASSWORD)
        test_page.click_on_show_hide_password()
        assert "input__placeholder-focused" in test_page.get_attribute_text(
            LocatorBasePages.FIELD_INPUT_PASSWORD_IS_ACTIVE, "class")

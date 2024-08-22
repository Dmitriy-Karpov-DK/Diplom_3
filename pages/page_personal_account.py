import allure
from pages.base_pages_stellar_burger import BasePagesSB
from locators.base_pages_locators import LocatorBasePages


class LoginPage(BasePagesSB):

    @allure.step('Вводим Email')
    def set_email(self, email):
        self.send_keys_method(LocatorBasePages.FIELD_INPUT_EMAIL, email)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.send_keys_method(LocatorBasePages.FIELD_INPUT_PASSWORD, password)

    @allure.step('Клик по кнопке Восстановить пароль')
    def click_on_recover_password(self):
        self.click_method(LocatorBasePages.BUTTON_RECOVER_PASSWORD)

    @allure.step('Клик по кнопке Восстановить')
    def click_on_recovery(self):
        self.click_method(LocatorBasePages.BUTTON_RECOVER)

    @allure.step('Клик по кнопке скрыть/показать пароль')
    def click_on_show_hide_password(self):
        self.click_method(LocatorBasePages.BUTTON_SHOW_PASSWORD)

    @allure.step('Клик по Личный кабинет')
    def click_on_personal_account(self):
        self.click_method(LocatorBasePages.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке Войти в личном кабинете')
    def click_on_enter(self):
        self.click_method(LocatorBasePages.BUTTON_ENTER_PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке История заказов')
    def click_on_order_history(self):
        self.click_method(LocatorBasePages.BUTTON_ORDER_HISTORY)

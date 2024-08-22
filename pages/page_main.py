import allure

from pages.page_personal_account import LoginPage
from locators.base_pages_locators import LocatorBasePages


class MainPage(LoginPage):

    @allure.step('Клик по Конструктор')
    def click_on_designer(self):
        self.click_method(LocatorBasePages.BUTTON_DESIGNER)

    @allure.step('Клик по Лента заказов')
    def click_on_orders_feed(self):
        self.click_method(LocatorBasePages.BUTTON_ORDERS_FEED)

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.click_method(LocatorBasePages.BUTTON_ANY_INGREDIENT)

    @allure.step('Клик по крестику всплывающего окна ингредиентов')
    def click_on_pop_up_close_button(self):
        self.click_method(LocatorBasePages.BUTTON_CLOSE_INFO_INGREDIENT)

    @allure.step('Перетащим ингредиент в конструкторе в набор')
    def drag_and_drop_ingredient_to_order(self):
        self.drag_and_drop_method(LocatorBasePages.ANY_INGREDIENT, LocatorBasePages.FIELD_BURGER_CONSTRUCTOR)

    @allure.step('клик по кнопке Оформить заказ')
    def click_on_button_place_order(self):
        self.click_method(LocatorBasePages.BUTTON_PLACE_ORDER)

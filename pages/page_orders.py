import allure

from pages.page_main import MainPage
from locators.base_pages_locators import LocatorBasePages


class OrderPage(MainPage):

    @allure.step('Клик на Заказ в ленте заказов')
    def click_order_in_order_feed(self):
        self.click_method(LocatorBasePages.ANY_ORDER_HISTORY)

    @allure.step('Закрыть окно с деталями заказа')
    def click_close_window_order_details(self):
        self.click_method(LocatorBasePages.BUTTON_CLOSE_INFO_INGREDIENT)

import allure

from pages.page_main import MainPage
from locators.base_pages_locators import LocatorBasePages
from constants import Constants


class TestPageMain:

    @allure.title('Проверим переход по клику на Конструктор')
    def test_go_to_designer_successful(self, driver):
        test_page = MainPage(driver)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.click_on_designer()
        assert test_page.get_url() == Constants.URL_BASE

    @allure.title('Проверим переход по клику на Лента заказов')
    def test_go_to_order_feed_successful(self, driver):
        test_page = MainPage(driver)
        test_page.click_on_orders_feed()
        assert test_page.get_url() == Constants.URL_ORDER_FEED

    @allure.title('Проверим клик на ингредиент с всплывающим окном деталей')
    def test_click_on_ingredient_show_pop_up_window(self, driver):
        test_page = MainPage(driver)
        test_page.click_on_ingredient()
        assert test_page.expectation(LocatorBasePages.POP_UP_WINDOW_ORDER_DETAILS)

    @allure.title('Проверим увеличение счетчика при добавлении ингредиента')
    def test_add_ingredient_show_up_count_ingredients(self, driver):
        test_page = MainPage(driver)
        test_page.drag_and_drop_ingredient_to_order()

        assert test_page.get_answer_text(LocatorBasePages.COUNTER_ANY_INGREDIENT) == '2'

    @allure.title('Проверим оформление заказа авторизованным ползователем')
    def test_create_order_auth_user_successful(self, driver, create_user):
        test_page = MainPage(driver)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.set_email(Constants.TEST_USER_EMAIL)
        test_page.set_password(Constants.TEST_USER_PASSWORD)
        test_page.click_on_enter()
        test_page.expectation(LocatorBasePages.COUNTER_ANY_INGREDIENT)
        test_page.drag_and_drop_ingredient_to_order()
        test_page.click_on_button_place_order()
        assert test_page.expectation(LocatorBasePages.NAME_ID_ORDER)

import allure

from pages.page_orders import OrderPage
from locators.base_pages_locators import LocatorBasePages
from constants import Constants


class TestOrderFeed:

    @allure.title('Проверим клик по заказу с открытием всплывающего окна с деталями заказа')
    def test_click_on_order_show_pop_up_window_details(self, driver):
        test_page = OrderPage(driver)
        test_page.go_to_url(Constants.URL_ORDER_FEED)
        test_page.wait_clickable(LocatorBasePages.ANY_ORDER_HISTORY)
        test_page.click_order_in_order_feed()
        assert test_page.expectation(LocatorBasePages.POP_UP_WINDOW_ORDER_NUMBER)

    @allure.title('Проверим отображение заказа из раздела История заказов в Ленте заказов')
    def test_order_display_from_order_history_in_order_feed(self, driver, create_user):
        test_page = OrderPage(driver)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.set_email(Constants.TEST_USER_EMAIL)
        test_page.set_password(Constants.TEST_USER_PASSWORD)
        test_page.click_on_enter()
        test_page.expectation(LocatorBasePages.COUNTER_ANY_INGREDIENT)
        test_page.drag_and_drop_ingredient_to_order()
        test_page.click_on_button_place_order()
        test_page.expectation(LocatorBasePages.DISPLAYING_CHECKMARK)
        while test_page.get_answer_text(LocatorBasePages.NUMBER_ORDER) == '9999':
            pass
        number_order = test_page.get_answer_text(LocatorBasePages.NUMBER_ORDER)
        test_page.go_to_url(Constants.URL_BASE)
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDERS_FEED)
        test_page.click_on_orders_feed()
        test_page.expectation(LocatorBasePages.NUMBER_ORDER_IN_ORDER_FEED)
        assert f"#0{number_order}" == test_page.get_answer_text(LocatorBasePages.NUMBER_ORDER_IN_ORDER_FEED)

    @allure.title('Проверим увеличение счетчика заказов Выполнено за все время')
    def test_increase_count_orders_for_all_time(self, driver, create_user):
        test_page = OrderPage(driver)
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDERS_FEED)
        test_page.click_on_orders_feed()
        test_page.expectation(LocatorBasePages.COUNTER_ORDERS_ALL_TIME)
        before = test_page.get_answer_text(LocatorBasePages.COUNTER_ORDERS_ALL_TIME)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.expectation(LocatorBasePages.FIELD_INPUT_EMAIL)
        test_page.set_email(Constants.TEST_USER_EMAIL)
        test_page.set_password(Constants.TEST_USER_PASSWORD)
        test_page.click_on_enter()
        test_page.expectation(LocatorBasePages.COUNTER_ANY_INGREDIENT)
        test_page.drag_and_drop_ingredient_to_order()
        test_page.click_on_button_place_order()
        test_page.expectation(LocatorBasePages.DISPLAYING_CHECKMARK)
        test_page.go_to_url(Constants.URL_BASE)
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDERS_FEED)
        test_page.click_on_orders_feed()
        test_page.expectation(LocatorBasePages.COUNTER_ORDERS_ALL_TIME)
        after = test_page.get_answer_text(LocatorBasePages.COUNTER_ORDERS_ALL_TIME)
        assert int(before) < int(after)

    @allure.title('Проверим увеличение счетчика заказов Выполнено за все сегодня')
    def test_increase_count_orders_for_today_time(self, driver, create_user):
        test_page = OrderPage(driver)
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDERS_FEED)
        test_page.click_on_orders_feed()
        test_page.expectation(LocatorBasePages.COUNTER_ORDERS_FOR_TODAY)
        before = test_page.get_answer_text(LocatorBasePages.COUNTER_ORDERS_FOR_TODAY)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.expectation(LocatorBasePages.FIELD_INPUT_EMAIL)
        test_page.set_email(Constants.TEST_USER_EMAIL)
        test_page.set_password(Constants.TEST_USER_PASSWORD)
        test_page.click_on_enter()
        test_page.expectation(LocatorBasePages.COUNTER_ANY_INGREDIENT)
        test_page.drag_and_drop_ingredient_to_order()
        test_page.click_on_button_place_order()
        test_page.expectation(LocatorBasePages.DISPLAYING_CHECKMARK)
        test_page.go_to_url(Constants.URL_BASE)
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDERS_FEED)
        test_page.click_on_orders_feed()
        test_page.expectation(LocatorBasePages.COUNTER_ORDERS_FOR_TODAY)
        after = test_page.get_answer_text(LocatorBasePages.COUNTER_ORDERS_FOR_TODAY)
        assert int(before) < int(after)

    @allure.title('Проверим что заказ появляется после оформления в разделе В работе')
    def test_create_order_check_in_progress(self, driver, create_user):
        test_page = OrderPage(driver)
        test_page.go_to_url(Constants.URL_LOGIN)
        test_page.expectation(LocatorBasePages.FIELD_INPUT_EMAIL)
        test_page.set_email(Constants.TEST_USER_EMAIL)
        test_page.set_password(Constants.TEST_USER_PASSWORD)
        test_page.click_on_enter()
        test_page.expectation(LocatorBasePages.COUNTER_ANY_INGREDIENT)
        test_page.drag_and_drop_ingredient_to_order()
        test_page.click_on_button_place_order()
        test_page.expectation(LocatorBasePages.DISPLAYING_CHECKMARK)
        while test_page.get_answer_text(LocatorBasePages.NUMBER_ORDER) == '9999':
            pass
        number_order = test_page.get_answer_text(LocatorBasePages.NUMBER_ORDER)
        test_page.go_to_url(Constants.URL_BASE)
        test_page.wait_clickable(LocatorBasePages.BUTTON_ORDERS_FEED)
        test_page.click_on_orders_feed()
        test_page.expectation(LocatorBasePages.NUMBER_IN_WORK)
        while test_page.get_answer_text(LocatorBasePages.NUMBER_IN_WORK) == 'Все текущие заказы готовы!':
            pass
        in_work = test_page.get_answer_text(LocatorBasePages.NUMBER_IN_WORK)
        assert int(number_order) == int(in_work)

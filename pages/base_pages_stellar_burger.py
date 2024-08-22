from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePagesSB:

    def __init__(self, driver):
        self.driver = driver

    def click_method(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_method(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def drag_and_drop_method(self, locator_element, locator_target):
        action = ActionChains(self.driver)
        drag = self.driver.find_element(*locator_element)
        drop = self.driver.find_element(*locator_target)
        action.drag_and_drop(drag, drop).perform()

    def get_url(self):
        get_url = self.driver.current_url
        return get_url

    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_attribute_text(self, locator, attribute):
        attrib = self.driver.find_element(*locator)
        return attrib.get_attribute(attribute)

    def expectation(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    def go_to_url(self, url):
        self.driver.get(url)

from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTSAL(BasePage):

    def is_title_matches(self):
        return "Says a Lot - Code and Theory" in self.driver.title

    def scrolling_down_page(self):
        self.driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(5)

    def click_on_sal_card(self):
        salcard = self.driver.find_element(*SaysaLotLocators.SALCARD)
        salcard.click()
        time.sleep(5)

    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    def submit_invalid_email(self):
        email = self.driver.find_element(*SaysaLotLocators.EMAIL)
        email.send_keys(" ")
        submit = self.driver.find_element(*SaysaLotLocators.SUBMIT)
        submit.click()
        time.sleep(2)
        error = self.driver.find_element(*SaysaLotLocators.ERROR)
        assert error is not None, "Error message is not present"

    def submit_valid_email(self):
        email = self.driver.find_element(*SaysaLotLocators.EMAIL)
        email.send_keys("test124@test.com")
        submit = self.driver.find_element(*SaysaLotLocators.SUBMIT)
        submit.click()
        time.sleep(5)







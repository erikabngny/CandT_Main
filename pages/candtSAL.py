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
        time.sleep(10)

    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    def submit_invalid_email(self):
        email = self.driver.find_element(*SaysaLotLocators.EMAIL)
        email.send_keys("test113@test")
        submit = self.driver.find_element(*SaysaLotLocators.SUBMIT)
        submit.click()
        time.sleep(2)
        validation = self.driver.find_element(*SaysaLotLocators.VALIDATION)
        validation_text = validation.text
        success_msg = "Success! Thanks for signing up."

        if validation_text == success_msg:
            print("Test Result Incorrect: Email is valid")
        else:
            print("Test Result Correct: Email is invalid")


    def clear_email_field(self):
        self.driver.find_element(*SaysaLotLocators.EMAIL).clear()


    def submit_valid_email(self):
        email = self.driver.find_element(*SaysaLotLocators.EMAIL)
        email.send_keys("test221@test.com")
        submit = self.driver.find_element(*SaysaLotLocators.SUBMIT)
        submit.click()
        time.sleep(5)

    def click_see_more_button(self):
        seemore = self.driver.find_element(*SaysaLotLocators.SEEMORE)
        seemore.click()
        time.sleep(5)







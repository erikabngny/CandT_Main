from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTCONTACT(BasePage):

    def is_title_matches(self):
        return "Code and Theory" in self.driver.title

    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    # Click email address

    def click_email_add(self):
        email1 = self.driver.find_element(*ContactLocators.EMAIL1)
        email1.click()
        time.sleep(3)

    # Test Valid/Invalid email on Newsletter

    def invalid_newsletter_email(self):
        email = self.driver.find_element(*ContactLocators.NEWSLETTER)
        email.send_keys(" ")
        submit = self.driver.find_element(*ContactLocators.SUBMIT)
        submit.click()
        time.sleep(3)

    def valid_newsletter_email(self):
        email = self.driver.find_element(*ContactLocators.NEWSLETTER)
        email.send_keys("test122@test.com")
        submit = self.driver.find_element(*ContactLocators.SUBMIT)
        submit.click()
        time.sleep(3)

    # Click Legal links

    def click_term_of_use(self):
        term = self.driver.find_element(*ContactLocators.TERMOFUSE)
        term.click()
        time.sleep(5)

    def click_privacy_policy(self):
        privacy = self.driver.find_element(*ContactLocators.PRIVACY)
        privacy.click()
        time.sleep(5)

    def click_supply_chain_statement(self):
        supply = self.driver.find_element(*ContactLocators.SUPPLYCHAIN)
        supply.click()
        time.sleep(5)
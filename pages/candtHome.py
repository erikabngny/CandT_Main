from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNT(BasePage):

    # def is_title_matches(self):
    #     return "My Store" in self.driver.title

    def navigate_to_whywemake_page(self):
        wwm_link = self.driver.find_element(*HomepageLocators.WHYWEMAKE)
        wwm_link.click()
        time.sleep(5)

    def navigate_to_thingswemake_page(self):
        twm_link = self.driver.find_element(*HomepageLocators.THINGSWEMAKE)
        twm_link.click()
        time.sleep(5)

    def navigate_to_saysalot_page(self):
        sal_link = self.driver.find_element(*HomepageLocators.SAYSALOT)
        sal_link.click()
        time.sleep(5)

    def navigate_to_aboutus_page(self):
        about_link = self.driver.find_element(*HomepageLocators.ABOUT_US)
        about_link.click()
        time.sleep(5)

    def navigate_to_career_page(self):
        career_link = self.driver.find_element(*HomepageLocators.CAREERS)
        career_link.click()
        time.sleep(5)

    def navigate_to_contact_page(self):
        contact_link = self.driver.find_element(*HomepageLocators.CONTACT)
        contact_link.click()
        time.sleep(5)

    def navigate_to_search_page(self):
        search_link = self.driver.find_element(*HomepageLocators.SEARCH)
        search_link.click()
        time.sleep(5)

    def click_contact_close_button(self):
        contact_close = self.driver.find_element(*HomepageLocators.CONTACT_CLOSE)
        contact_close.click()
        time.sleep(5)

    def click_search_close_button(self):
        search_close = self.driver.find_element(*HomepageLocators.SEARCH_CLOSE)
        search_close.click()
        time.sleep(5)



    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)











from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNT(BasePage):

    # def is_title_matches(self):
    #     return "My Store" in self.driver.title

    def navigate_to_about_us_page(self):

        about_us_link = self.driver.find_element(*AboutUsLocators.ABOUT_US)
        about_us_link.click()
        time.sleep(5)
        # nav_logo = self.driver.find_element(*NavLocators.CANDT_LOGO)
        # nav_logo.click()
        # time.sleep(2)

    # def click_navigation_logo(self):
    #     nav_logo = self.driver.find_element(*NavLocators.CANDT_LOGO)
    #     nav_logo.click()
    #     time.sleep(2)












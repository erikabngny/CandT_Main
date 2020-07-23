from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTWWM(BasePage):

    def is_title_matches(self):
        return "Why We Make" in self.driver.title

    def scrolling_down_page(self):
        self.driver.execute_script("window.scrollBy(0, 3000)")
        time.sleep(5)

    def scrolling_up_page(self):
        self.driver.execute_script("window.scrollBy(0, -3000)")
        time.sleep(5)










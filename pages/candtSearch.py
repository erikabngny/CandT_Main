from locators.page_elements import *
from utils import environment as env
from extensions.commands import *
from selenium.common.exceptions import NoSuchElementException



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTSEARCH(BasePage):

    def is_title_matches(self):
        return "Code and Theory" in self.driver.title

    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    # Valid Search

    def valid_search(self):
        search_input = self.driver.find_element(*SearchLocators.SEARCHINPUT)
        search_input.send_keys("pgim")
        time.sleep(5)
        result_count = self.driver.find_element(*SearchLocators.RESULTCOUNT)
        card1 = self.driver.find_element(*SearchLocators.FIRSTCARD)
        # assert result_count is not None, "No result count element"
        if result_count is not None:
            print(result_count.text)
            card1.click()
            time.sleep(5)


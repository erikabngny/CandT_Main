from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTTWM(BasePage):

    def is_title_matches(self):
        return "Things We Make" in self.driver.title

    def scrolling_down_page(self):
        self.driver.execute_script("window.scrollBy(0, 5000)")
        time.sleep(5)

    def scrolling_up_page(self):
        self.driver.execute_script("window.scrollBy(0, -5000)")
        time.sleep(5)

    def hover_on_carousel_slide_1(self):
        hero1 = self.driver.find_element(*ThingsWeMakeLocators.SLIDECONTENT1)
        actions = ActionChains(self.driver)
        actions.move_to_element(hero1).perform()
        time.sleep(3)

    def hover_on_carousel_slide_2(self):
        hero2 = self.driver.find_element(*ThingsWeMakeLocators.SLIDECONTENT2)
        actions = ActionChains(self.driver)
        actions.move_to_element(hero2).perform()
        time.sleep(3)

    def hover_on_carousel_slide_3(self):
        hero3 = self.driver.find_element(*ThingsWeMakeLocators.SLIDECONTENT3)
        actions = ActionChains(self.driver)
        actions.move_to_element(hero3).perform()
        time.sleep(3)

    def click_on_carousel_slide_3(self):
        hero1 = self.driver.find_element(*ThingsWeMakeLocators.SLIDECONTENT3)
        hero1.click()
        time.sleep(5)







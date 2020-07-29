from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTCAREER(BasePage):

    def is_title_matches(self):
        return "Careers - Code and Theory" in self.driver.title

    # def scrolling_up_page(self):
    #     header = self.driver.find_element(*AbutUsLocators.HEADER)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
    #     time.sleep(5)

    def scrolling_down_page(self):
        self.driver.execute_script("window.scrollBy(0, 700)")
        time.sleep(5)

    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    # Clicking Location tab

    def click_location_tab_ny(self):
        loc_ny = self.driver.find_element(*CareerLocators.LocationNY)
        loc_ny.click()
        time.sleep(3)

    def click_location_tab_sf(self):
        loc_sf = self.driver.find_element(*CareerLocators.LocationSF)
        loc_sf.click()
        time.sleep(3)

    def click_location_tab_london(self):
        loc_lon = self.driver.find_element(*CareerLocators.LocationLONDON)
        loc_lon.click()
        time.sleep(3)

    def click_location_tab_remote(self):
        loc_rem = self.driver.find_element(*CareerLocators.LocationREMOTE)
        loc_rem.click()
        time.sleep(3)

    # Clicking Career Job Post

    def click_job_post(self):
        careerjob = self.driver.find_element(*CareerLocators.CAREERJOB1)
        careerjob.click()
        time.sleep(5)

    def click_apply_now(self):
        apply = self.driver.find_element(*CareerLocators.APPLYNOW)
        apply.click()
        time.sleep(5)

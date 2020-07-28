from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class TestCNTABOUT(BasePage):

    def is_title_matches(self):
        return "About Us - Code and Theory" in self.driver.title

    def scrolling_up_page(self):
        header = self.driver.find_element(*AbutUsLocators.HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        time.sleep(5)

    def scrolling_down_page(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        time.sleep(5)

    def go_back_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    # CLicking Sub Nav

    def click_what_we_do(self):
        whatwedo = self.driver.find_element(*AbutUsLocators.WHATWEDO)
        whatwedo.click()
        time.sleep(5)

    def click_our_services(self):
        services = self.driver.find_element(*AbutUsLocators.OURSERVICES)
        services.click()
        time.sleep(5)

    def click_our_offices(self):
        offices = self.driver.find_element(*AbutUsLocators.OUROFFICES)
        offices.click()
        time.sleep(5)

    def click_join_our_team(self):
        team = self.driver.find_element(*AbutUsLocators.JOINOURTEAM)
        team.click()
        time.sleep(5)

    # Clicking Locations

    def click_new_york(self):
        ny = self.driver.find_element(*AbutUsLocators.NEWYORK)
        ny.click()
        time.sleep(5)

    def click_san_francisco(self):
        sf = self.driver.find_element(*AbutUsLocators.SF)
        sf.click()
        time.sleep(5)

    def click_london(self):
        london = self.driver.find_element(*AbutUsLocators.LONDON)
        london.click()
        time.sleep(5)

    def click_manila(self):
        manila = self.driver.find_element(*AbutUsLocators.MANILA)
        manila.click()
        time.sleep(5)

    #  Clicking Job Post

    def click_job1(self):
        job1 = self.driver.find_element(*AbutUsLocators.JOB1)
        job1.click()
        time.sleep(5)

    #  Contact Module

    def click_email_address(self):
        email = self.driver.find_element(*AbutUsLocators.EMAIL)
        email.click()
        time.sleep(5)

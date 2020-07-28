""" PYTEST PAGE ELEMENT IDENTIFIERS GO HERE """

from selenium.webdriver.common.by import By


class HomepageLocators(object):
    WHYWEMAKE = (By.XPATH, '//*[@id="page-home"]//a[@title="Why We Make - Our Philosophy"]')
    THINGSWEMAKE = (By.XPATH, '//*[@id="page-home"]//a[@title="The Things We Make - Our Work"]')
    SAYSALOT = (By.XPATH, '//*[@id="page-home"]//a[@title="Says a Lot - Media & Mentions"]')
    ABOUT_US = (By.XPATH, '//*[@id="page-home"]//a[@title="About Us - Everything Else"]')
    CAREERS = (By.XPATH, '//*[@id="page-home"]//a[@href="/careers"]')
    CONTACT = (By.XPATH, '//*[@id="page-home"]//li[2]/button')
    SEARCH = (By.XPATH, '//*[@id="page-home"]//li[3]/button')

    CONTACT_CLOSE = (By.XPATH, '//div[@id="overlay-portal"]//button[@class="src-sites-candt-components-ContactOverlay-contactOverlay__close"]')
    SEARCH_CLOSE = (By.XPATH, '//div[@id="overlay-portal"]//button[@class="src-sites-candt-components-SearchOverlay-searchOverlay__close"]')

class ThingsWeMakeLocators(object):
    SLIDECONTENT1 = (By.XPATH, '//*[@id="page-thingsWeMake"]//section/div[@id="gsap-slide-0"]//div[@id="gsap-content-0"]/a')
    SLIDECONTENT2 = (By.XPATH, '//*[@id="page-thingsWeMake"]//section/div[@id="gsap-slide-1"]//div[@id="gsap-content-1"]/a')
    SLIDECONTENT3 = (By.XPATH, '//*[@id="page-thingsWeMake"]//section/div[@id="gsap-slide-2"]//div[@id="gsap-content-2"]/a')


class SaysaLotLocators(object):
    SALCARD = (By.XPATH, '//*[@id="page-saysALot"]//section[1]/a[3]')
    EMAIL = (By.XPATH, '//input[@id="newsletter_card"]')
    SUBMIT = (By.XPATH, '//button[@type="submit"]')
    ERROR = (By.XPATH, '//*[@id="page-saysALot"]//div[@class="src-sites-candt-components-Newsletter-newsletter__validations"]')


class NavLocators(object):
    CANDT_LOGO = (By.XPATH, '//div[@class="src-sites-candt-components-MainNavigation-header__main"]')


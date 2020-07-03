""" PYTEST PAGE ELEMENT IDENTIFIERS GO HERE """

from selenium.webdriver.common.by import By


class AboutUsLocators(object):
    ABOUT_US = (By.XPATH, '//section[@id="page-home"]//div/section/nav[2]/ul/li[4]')

class NavLocators(object):
    CANDT_LOGO = (By.XPATH, '//div[@class="src-sites-candt-components-MainNavigation-header__main"]')


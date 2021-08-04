""" PYTEST PAGE ELEMENT IDENTIFIERS GO HERE """

from selenium.webdriver.common.by import By


class HomepageLocators(object):
    WHYWEMAKE = (By.XPATH, '//*[@id="page-home"]//a[@title="Why We Make - Our Philosophy"]')
    THINGSWEMAKE = (By.XPATH, '//*[@id="page-home"]//a[@title="The Things We Make - Our Work"]')
    SAYSALOT = (By.XPATH, '//*[@id="page-home"]//a[@title="Says a Lot - Media & Mentions"]')
    ABOUT_US = (By.XPATH, '//*[@id="page-home"]//a[@title="About Us - Everything Else"]')
    CAREERS = (By.XPATH, '//*[@id="main-content"]//ul[3]//a[@href="/careers"]')
    CONTACT = (By.XPATH, '//*[@id="main-content"]//li[2]/button')
    SEARCH = (By.XPATH, '//*[@id="main-content"]//li[3]/button')

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
    VALIDATION = (By.XPATH, '//*[@id="page-saysALot"]//div[@class="src-sites-candt-components-Newsletter-newsletter__validations"]/span')
    SEEMORE = (By.XPATH, '//article[@id="page-saysALot"]//button[@type="button"]')


class AbutUsLocators(object):
    HEADER = (By.XPATH, '//article[@id="page-aboutUs"]//div[@class="src-sites-candt-components-AboutUsHeader-about-us-header__title-container"]')
    WHATWEDO = (By.XPATH, '//article[@id="page-aboutUs"]//nav[@class="src-sites-candt-components-AboutUsSubNavigation-sub-navigation__list"]/button[1]')
    OURSERVICES = (By.XPATH, '//article[@id="page-aboutUs"]//nav[@class="src-sites-candt-components-AboutUsSubNavigation-sub-navigation__list"]/button[2]')
    OUROFFICES = (By.XPATH, '//article[@id="page-aboutUs"]//nav[@class="src-sites-candt-components-AboutUsSubNavigation-sub-navigation__list"]/button[3]')
    JOINOURTEAM = (By.XPATH, '//article[@id="page-aboutUs"]//nav[@class="src-sites-candt-components-AboutUsSubNavigation-sub-navigation__list"]/button[4]')

#       Location
    NEWYORK = (By.XPATH, '//article[@id="page-aboutUs"]/section[@class="src-sites-candt-components-OfficeGrid-container"]/ul//a[@href="/location/new-york"]')
    SF = (By.XPATH, '//article[@id="page-aboutUs"]/section[@class="src-sites-candt-components-OfficeGrid-container"]/ul//a[@href="/location/san-francisco"]')
    LONDON = (By.XPATH, '//article[@id="page-aboutUs"]/section[@class="src-sites-candt-components-OfficeGrid-container"]/ul//a[@href="/location/london"]')
    MANILA = (By.XPATH, '//article[@id="page-aboutUs"]/section[@class="src-sites-candt-components-OfficeGrid-container"]/ul//a[@href="/location/manila"]')

#       Job Post

    JOB1 = (By.XPATH, '//article[@id="page-aboutUs"]/section[@class="component src-sites-candt-components-JoinOurTeam-join-our-team"]//ul/li[1]')

#       Contact Module
    EMAIL = (By.XPATH, '//article[@id="page-aboutUs"]//ul[@class="contact__columns src-sites-candt-components-Contact-contact__columns--general"]/li[2]/span/span')


class CareerLocators(object):
    LocationNY = (By.XPATH, '//article[@id="page-careers"]/section[@class="src-sites-candt-components-CareersJobList-CareersJobList"]//ul/li[1]/button')
    LocationSF = (By.XPATH, '//article[@id="page-careers"]/section[@class="src-sites-candt-components-CareersJobList-CareersJobList"]//ul/li[2]/button')
    LocationLONDON = (By.XPATH, '//article[@id="page-careers"]/section[@class="src-sites-candt-components-CareersJobList-CareersJobList"]//ul/li[3]/button')
    LocationREMOTE = (By.XPATH, '//article[@id="page-careers"]/section[@class="src-sites-candt-components-CareersJobList-CareersJobList"]//ul/li[4]/button')

    CAREERJOB1 = (By.XPATH, '//*[@id="page-careers"]/section/div/section[1]/article[1]/a')
    APPLYNOW = (By.XPATH, '//*[@id="page-jobDetail"]/section/section/div[1]/button')

class ContactLocators(object):
    EMAIL1 = (By.XPATH, '//div[@id="overlay-portal"]/section[@role="dialog"]//ul//span[.="newbiz@codeandtheory.com"]')
    NEWSLETTER = (By.XPATH, '//*[@id="newsletter_contact"]')
    SUBMIT = (By.XPATH, '//*[@type="submit"]')

    TERMOFUSE = (By.XPATH, '//a[@href="/terms-of-use"]')
    PRIVACY = (By.XPATH, '//a[@href="/privacy-policy"]')
    SUPPLYCHAIN = (By.XPATH, '//a[@href="/supply-chain-statement"]')

class SearchLocators(object):
    SEARCHINPUT = (By.XPATH, '//*[@id="search"]')
    # RESULTCOUNT = (By.XPATH, '//*[@id="searchOverlay"]/div/div[2]/div[2]/p')
    RESULTCOUNT = (By.CLASS_NAME, 'src-sites-candt-components-SearchOverlay-searchOverlay__resultCount')
    FIRSTCARD = (By.XPATH, '//*[@id="searchOverlay"]/div/div[3]/a[1]')
    NORESULT = (By.XPATH, '//*[@id="searchOverlay"]/div/p')



class NavLocators(object):
    CANDT_LOGO = (By.XPATH, '//div[@class="src-sites-candt-components-MainNavigation-header__main"]')


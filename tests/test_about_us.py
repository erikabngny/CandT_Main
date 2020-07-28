import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_about(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_aboutus_page(self)
        # Clicking Sub Nav items
        on.ABOUT.click_what_we_do(self)
        on.ABOUT.scrolling_up_page(self)
        on.ABOUT.click_our_services(self)
        on.ABOUT.scrolling_up_page(self)
        on.ABOUT.click_our_offices(self)
        on.ABOUT.scrolling_up_page(self)
        on.ABOUT.click_join_our_team(self)
        on.ABOUT.scrolling_up_page(self)
        # Clicking Locations
        on.ABOUT.click_our_offices(self)
        on.ABOUT.click_new_york(self)
        on.ABOUT.go_back_to_previous_page(self)
        on.ABOUT.click_san_francisco(self)
        on.ABOUT.go_back_to_previous_page(self)
        on.ABOUT.click_london(self)
        on.ABOUT.go_back_to_previous_page(self)
        on.ABOUT.click_manila(self)
        on.ABOUT.go_back_to_previous_page(self)
        # Clicking Job Post
        on.ABOUT.scrolling_up_page(self)
        on.ABOUT.click_join_our_team(self)
        on.ABOUT.click_job1(self)
        on.ABOUT.go_back_to_previous_page(self)
        # Clicking Email address on Contact Module
        on.ABOUT.scrolling_down_page(self)
        on.ABOUT.click_email_address(self)







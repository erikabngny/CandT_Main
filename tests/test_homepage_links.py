import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_homepage_links(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_whywemake_page(self)
        on.Home.go_back_to_previous_page(self)
        on.Home.navigate_to_thingswemake_page(self)
        on.Home.go_back_to_previous_page(self)
        on.Home.navigate_to_saysalot_page(self)
        on.Home.go_back_to_previous_page(self)
        on.Home.navigate_to_aboutus_page(self)
        on.Home.go_back_to_previous_page(self)
        on.Home.navigate_to_career_page(self)
        on.Home.go_back_to_previous_page(self)
        on.Home.navigate_to_contact_page(self)
        on.Home.click_contact_close_button(self)
        on.Home.navigate_to_search_page(self)
        on.Home.click_search_close_button(self)



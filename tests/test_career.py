import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_career(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_career_page(self)
        on.CAREER.scrolling_down_page(self)
        # Clicking Location Tab
        on.CAREER.click_location_tab_sf(self)
        on.CAREER.click_location_tab_london(self)
        on.CAREER.click_location_tab_remote(self)
        on.CAREER.click_location_tab_ny(self)
        # Clicking Job Post
        on.CAREER.click_job_post(self)
        on.CAREER.click_apply_now(self)
        




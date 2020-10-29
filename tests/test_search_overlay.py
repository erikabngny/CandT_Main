import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_search_overlay(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_search_page(self)
        on.SEARCH.valid_search(self)


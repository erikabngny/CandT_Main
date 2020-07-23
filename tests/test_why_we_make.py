import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_wwm(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_whywemake_page(self)
        on.WWM.scrolling_down_page(self)
        on.WWM.scrolling_up_page(self)





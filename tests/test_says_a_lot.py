import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_sal(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_saysalot_page(self)
        on.SAL.scrolling_down_page(self)
        on.SAL.click_on_sal_card(self)
        on.SAL.scrolling_down_page(self)
        on.SAL.go_back_to_previous_page(self)
        on.SAL.submit_invalid_email(self)
        on.SAL.submit_valid_email(self)






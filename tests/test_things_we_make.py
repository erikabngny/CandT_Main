import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_twm(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_thingswemake_page(self)
        on.TWM.scrolling_down_page(self)
        on.TWM.scrolling_up_page(self)
        on.TWM.hover_on_carousel_slide_2(self)
        on.TWM.hover_on_carousel_slide_3(self)
        on.TWM.hover_on_carousel_slide_1(self)
        on.TWM.click_on_carousel_slide_1(self)






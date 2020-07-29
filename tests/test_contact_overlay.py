import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_contact_overlay(self):
        self.driver.get(env.page_url)

        on.Home.navigate_to_contact_page(self)
        on.CONTACT.click_email_add(self)
        # Test Newsletter
        on.CONTACT.invalid_newsletter_email(self)
        on.CONTACT.valid_newsletter_email(self)
        # Click Legal Links
        on.CONTACT.click_term_of_use(self)
        on.CONTACT.go_back_to_previous_page(self)
        on.CONTACT.click_privacy_policy(self)
        on.CONTACT.go_back_to_previous_page(self)
        on.CONTACT.click_supply_chain_statement(self)


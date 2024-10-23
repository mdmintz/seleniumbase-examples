# Test the user-agent with UC Mode (Verify "Headless" is NOT in it)
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--uc")


class HeadlessUCTests(BaseCase):
    def test_verify_user_agent_of_headless_uc_mode(self):
        if not self.undetectable or not self.headless:
            self.get_new_driver(undetectable=True)
        self.open("data:,")
        user_agent = self.get_user_agent()
        print('\nUser Agent = "%s"' % user_agent)
        print('\nUser Agent (lower) = "%s"' % user_agent.lower())
        self.assert_true("headless" not in user_agent.lower())

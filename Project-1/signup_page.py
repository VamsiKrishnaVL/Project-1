from pages.base_page import BasePage

class SignupPage(BasePage):
    def get_signup_url(self):
        return self.get_url()

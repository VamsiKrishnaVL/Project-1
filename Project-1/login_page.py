from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-btn")
    ERROR_MSG = (By.CLASS_NAME, "error-message")

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.click(self.SUBMIT)

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text

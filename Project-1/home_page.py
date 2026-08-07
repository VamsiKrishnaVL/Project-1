from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_BTN = (By.XPATH, "//a[text()='Login']")
    SIGNUP_BTN = (By.XPATH, "//a[text()='Sign Up']")
    COURSES = (By.XPATH, "//a[text()='Courses']")
    LIVE_CLASSES = (By.XPATH, "//a[text()='LIVE Classes']")
    PRACTICE = (By.XPATH, "//a[text()='Practice']")
    DOBBY_ASSISTANT = (By.ID, "dobby-assistant")

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_signup(self):
        self.click(self.SIGNUP_BTN)

    def menu_items_visible(self):
        return all([
            self.is_visible(self.COURSES),
            self.is_visible(self.LIVE_CLASSES),
            self.is_visible(self.PRACTICE)
        ])

    def is_dobby_present(self):
        return self.is_visible(self.DOBBY_ASSISTANT)

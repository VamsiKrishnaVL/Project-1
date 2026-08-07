from selenium import webdriver

class DriverFactory:
    def get_driver(self, browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            raise Exception("Browser not supported")
        driver.maximize_window()
        return driver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

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

from pages.base_page import BasePage

class SignupPage(BasePage):
    def get_signup_url(self):
        return self.get_url()

"""
GUVI Selenium + Pytest - Single File Automation Test Suite

Run:
    pip install selenium pytest
    pytest -v guvi_automation_single.py

Note:
    Replace the placeholder valid login credentials in test_tc6_valid_login
    and test_tc10_logout with a real GUVI test account if required.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


class SignupPage(BasePage):
    def get_signup_url(self):
        return self.get_url()


@pytest.fixture
def driver():
    driver = DriverFactory().get_driver("chrome")
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()


# =========================
# HOME PAGE TESTS
# =========================

def test_tc1_url_valid(driver):
    assert "guvi.in" in driver.current_url


def test_tc2_title(driver):
    assert driver.title == "GUVI | Learn to code in your native language"


def test_tc3_login_button(driver):
    home = HomePage(driver)
    assert home.is_visible(HomePage.LOGIN_BTN)
    home.click_login()
    assert "login" in driver.current_url


def test_tc4_signup_button(driver):
    home = HomePage(driver)
    assert home.is_visible(HomePage.SIGNUP_BTN)
    home.click_signup()
    assert "register" in driver.current_url


def test_tc8_menu_items(driver):
    home = HomePage(driver)
    assert home.menu_items_visible()


def test_tc9_dobby_assistant(driver):
    home = HomePage(driver)
    assert home.is_dobby_present()


# =========================
# SIGNUP TEST
# =========================

def test_tc5_signup_navigation(driver):
    home = HomePage(driver)
    home.click_signup()
    signup = SignupPage(driver)
    assert signup.get_signup_url() == "https://www.guvi.in/register/"


# =========================
# LOGIN TESTS
# =========================

def test_tc6_valid_login(driver):
    home = HomePage(driver)
    home.click_login()
    login = LoginPage(driver)

    # Replace these with a real test account.
    login.login("vamsikrishna9686@gmail.com", "vamsi123@")

    assert "dashboard" in driver.current_url


def test_tc7_invalid_login(driver):
    home = HomePage(driver)
    home.click_login()
    login = LoginPage(driver)
    login.login("wrong@example.com", "wrongpass")
    assert "Invalid" in login.get_error_message()


def test_tc10_logout(driver):
    home = HomePage(driver)
    home.click_login()
    login = LoginPage(driver)

   


    # find_element_by_xpath API.
    driver.find_element(By.XPATH, "//a[text()='Logout']").click()

    assert "login" in driver.current_url or "guvi.in" in driver.current_url

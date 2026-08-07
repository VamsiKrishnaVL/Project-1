import pytest
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = DriverFactory().get_driver("chrome")
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()

def test_tc6_valid_login(driver):
    home = HomePage(driver)
    home.click_login()
    login = LoginPage(driver)
    login.login("valid_email@example.com", "valid_password")
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
    login.login("valid_email@example.com", "valid_password")
    driver.find_element_by_xpath("//a[text()='Logout']").click()
    assert "login" in driver.current_url or "guvi.in" in driver.current_url

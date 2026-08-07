import pytest
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = DriverFactory().get_driver("chrome")
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()

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

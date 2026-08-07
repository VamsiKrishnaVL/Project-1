import pytest
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.signup_page import SignupPage

@pytest.fixture
def driver():
    driver = DriverFactory().get_driver("chrome")
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()

def test_tc5_signup_navigation(driver):
    home = HomePage(driver)
    home.click_signup()
    signup = SignupPage(driver)
    assert signup.get_signup_url() == "https://www.guvi.in/register/"

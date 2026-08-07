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

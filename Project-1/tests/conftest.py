import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    d=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield d
    d.quit()

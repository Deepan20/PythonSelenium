from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def driver():
    # options = Options()
    # options.add_argument("--headless=new")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")

    driver = webdriver.Chrome()
    driver.get("https://www.leafground.com/")

    yield driver
    driver.quit()
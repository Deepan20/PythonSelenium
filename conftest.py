from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.leafground.com/select.xhtml")
    yield driver
    driver.close()
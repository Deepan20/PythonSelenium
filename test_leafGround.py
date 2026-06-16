from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestLeafGround:
    def test_windowHandle(self,driver):
        parent=driver.current_window_handle
        driver.find_element(By.XPATH,"//span[text()='Open']/parent::button[@id='j_idt88:new']").click()
        windows = driver.window_handles
        for window in windows:
            if window != parent:
                driver.switch_to.window(window)
                title= driver.title
                assert title , "Dashboard"


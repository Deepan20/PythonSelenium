from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.select import Select

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

    @pytest.mark.smoke
    def test_dropdown(self,driver):
        ele=driver.find_element(By.CSS_SELECTOR,"select.ui-selectonemenu")
        dropdown=Select(ele)
        dropdown.select_by_visible_text("Cypress")
        driver.save_screenshot("dropdown.png")



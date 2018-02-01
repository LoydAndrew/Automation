from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

class Slider():

    def sliding(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/slider/")
        sleep(2)
        driver.implicitly_wait(1)
        driver.switch_to.frame(0)

        locator_span = '[tabindex="0"]'
        element = driver.find_element(By.CSS_SELECTOR, locator_span)
        sleep(1)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 500, 0 ).perform()
            print("Slide.....")
            sleep(1)
        finally:
            driver.quit()

CH = Slider()
CH.sliding()
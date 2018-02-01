from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Constants import kodeit_practise_url
from time import sleep

class MouseHover():

    def test_mouse_hover(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_practise_url)
        driver.execute_script("window.scrollBy(0,800);")
        sleep(2)
        driver.implicitly_wait(5)

        element = driver.find_element(By.ID, "mousehover")
        item_to_click_locator = '[href="\#top"]'

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print ("Mouse hover")
            sleep(2)
            top_link = driver.find_element(By.CSS_SELECTOR, item_to_click_locator)
            actions.move_to_element(top_link).click().perform()
            print("item_click")
            sleep(2)
        finally:
            driver.quit()


CH = MouseHover()
CH.test_mouse_hover()

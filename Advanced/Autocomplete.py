from selenium import webdriver
from selenium.webdriver.common.by import By
#from HandyWrapper import Explicitly_Wait
from time import sleep

class Autocomplete():

    def test_suggestion(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.prom.ua")
        driver.implicitly_wait(5)
        #explicit_wait = Explicitly_Wait(driver)

        try:
            """search_box = explicit_wait.wait_for_element(
                "//input[@data-qaid='search_input']",
                "xpath")"""
            search_box = driver.find_element(By.CSS_SELECTOR, "[type='text']")
            search_box.click()
            search_box.send_keys("мобильные телефоны")
            sleep(2)
            suggestion = driver.find_element(
                By.XPATH,
                "//span[@class='x-autocomplete__highlight-text'][contains(text(),'Мобильные телефоны, смартфоны')]")
            suggestion.click()
            sleep(3)
        finally:
            driver.quit()


CH = Autocomplete()
CH.test_suggestion()

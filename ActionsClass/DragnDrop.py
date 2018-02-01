from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

class DragnDrop():

    def drah_n_drop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        sleep(2)
        driver.implicitly_wait(1)
        driver.switch_to.frame(0)
        try:
            actions = ActionChains(driver)
            drag_element = driver.find_element(By.ID, "draggable")
            drop_element = driver.find_element(By.ID, "droppable")
            actions.drag_and_drop(drag_element,drop_element).perform()
            print("Drag_and_dropped")

            sleep(2)
        finally:
            driver.quit()


    def accurate_drah_n_drop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        sleep(2)
        driver.implicitly_wait(1)
        driver.switch_to.frame(0)
        try:
            actions = ActionChains(driver)
            drag_element = driver.find_element(By.ID, "draggable")
            drop_element = driver.find_element(By.ID, "droppable")
            actions.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
            print("Drag_and_dropped")

            sleep(2)
        finally:
            driver.quit()


CH = DragnDrop()
CH.drah_n_drop()
CH.accurate_drah_n_drop()

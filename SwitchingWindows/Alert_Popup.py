from selenium import webdriver
from selenium.webdriver.common.by import By
from HandyWrapper import screenshot
from Constants import kodeit_practise_url
from time import sleep

class Iframe():

    def test_iframe(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_practise_url)
        driver.execute_script("window.scrollBy(0, 800);")
        driver.implicitly_wait(5)

        try:
            driver.find_element(By.ID, "name").send_keys("Ojega")
            driver.find_element(By.ID, "alertbtn").click()
            sleep(2)
            alert1 = driver.switch_to.alert
            alert1.accept()
            sleep(2)
            driver.find_element(By.ID, "confirmbtn").click()
            sleep(2)
            alert2 = driver.switch_to.alert
            alert2.dismiss()

        finally:
            driver.quit()

CH = Iframe()
CH. test_iframe()
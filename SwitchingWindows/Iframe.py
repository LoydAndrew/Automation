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
            #Switch to Frame using id
            driver.switch_to.frame("courses-iframe")
            #Switch to Frame using name
            #driver.switch_to.frame("iframe-name")
            #Switch to Frame using numbers
            #driver.switch_to.frame(0)

            #Search courses
            search_box = driver.find_element(By.ID, "search-courses")
            search_box.send_keys("python")
            sleep(2)

            #Switch back to the parent frame
            driver.switch_to.default_content()
            driver.execute_script("window.scrollBy(0,-1000);")
            sleep(3)
            driver.find_element(By.ID, "name").send_keys("success")
            sleep(2)
        finally:
            driver.quit()

CH= Iframe()
CH.test_iframe()
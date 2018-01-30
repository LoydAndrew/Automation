from selenium import webdriver
from selenium.webdriver.common.by import By
from HandyWrapper import screenshot
from Constants import kodeit_practise_url
from time import sleep

class Js_script():

    def js_execution(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get(kodeit_main_url)
        driver.execute_script("window.location='https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(5)

        try:
            #driver.find_element(By.ID, "name").send_keys("test")
            element = driver.execute_script("return document.getElementById('name');")
            element.send_keys("test")
            sleep(2)
        finally:
            driver.quit()

    def size_of_window(self):
        driver = webdriver.Chrome()
        #driver.maximize_window()
        # driver.get(kodeit_main_url)
        driver.execute_script("window.location='https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(5)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth")
        print ("Size of height: %s. Size of width: %s " % (height,width))
        driver.quit()

    def scrolling(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_practise_url)
        driver.execute_script("window.location='https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(5)

        #Scroll Down
        driver.execute_script("window.scrollBy(0,800);")
        sleep(3)
        #Scroll Up
        driver.execute_script("window.scrollBy(0,-800);")
        sleep(3)
        #Scroll Element IntoView
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(3)
        driver.execute_script("window.scrollBy(0,-100);")
        #Selenium Scroll
        sleep(2)
        driver.execute_script("window.scrollBy(0,800);")
        location = element.location_once_scrolled_into_view
        print ("Location is:"  + str(location))
        sleep(3)
        driver.execute_script("window.scrollBy(0,-100);")
        sleep(2)
        driver.quit()


CH = Js_script()
# CH.js_execution()
# CH.size_of_window()
CH.scrolling()


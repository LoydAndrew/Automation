from selenium import webdriver
from time import sleep
class ElementState():

    def isEnabled(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        baseUrl = "http://www.google.com"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_id("gs_taif0")
        #e1.send_keys("letskodeit")
        e1state=e1.is_enabled()
        print (str(e1state) + " is a state of e1state")

        e2 = driver.find_element_by_id("lst-ib")
        e2.send_keys("letskodeit")
        e2state = e2.is_enabled()
        print(str(e2state) + " is a state of e2state")
        sleep(3)
        driver.quit()


FF = ElementState()
FF.isEnabled()

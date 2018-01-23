from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from Constants import kodeit_practise_url
from HandyWrapper import HandyWrapper



class WrapperUsage(object):

    def testWrapper(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_practise_url)
        driver.implicitly_wait(2)
        hw = HandyWrapper(driver)

        text_field = hw.get_element("name")
        sleep(2)
        text_field.send_keys("Test")
        sleep(1)
        text_field2 = hw.get_element("//input[@id='name']","xpath")
        sleep(1)
        text_field2.clear()
        sleep(1)
        driver.quit()

CH = WrapperUsage()
CH.testWrapper()
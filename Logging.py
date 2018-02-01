from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from time import strftime
import logging
"""class ():

    def (self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/slider/")
        sleep(2)
        driver.implicitly_wait(1)
        driver.switch_to.frame(0)
"""
"""
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning('warning')
logging.error("error")
logging.info("info")
"""
"""Basic Logging"""
logging.basicConfig(format='%(asctime)s, %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
logging.warning('warning')
logging.error("error")
logging.info("info")




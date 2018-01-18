from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ClickAndSend():

    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com"
        driver.maximize_window()
        driver.get(baseUrl)
        login_link = driver.find_element(By.XPATH, "//a[@href='/sign_in']")
        login_link.click()
        driver.implicitly_wait(10)  # waiting 10 seconds, then another until finding

        email = driver.find_element(By.ID, "user_email")
        email.send_keys('test')
        sleep(3)
        email.clear()

        password = driver.find_element(By.ID,'user_password')
        password.send_keys('test')
        sleep(3)
        password.clear()
        driver.quit()

FF = ClickAndSend()
FF.test()


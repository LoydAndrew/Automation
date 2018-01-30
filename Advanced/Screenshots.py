from selenium import webdriver
from selenium.webdriver.common.by import By
from HandyWrapper import screenshot
from Constants import kodeit_main_url
from time import sleep

class ScreenShot():

    def test_screenshot(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_main_url)
        driver.implicitly_wait(5)
        #explicit_wait = Explicitly_Wait(driver)

        try:
            driver.find_element(By.LINK_TEXT, "Login").click()
            driver.find_element(By.ID, "user_email").send_keys('asdfasdf.com')
            driver.find_element(By.ID, "user_password").send_keys('fasdj234123')
            driver.find_element(By.NAME,"commit").click()
            sleep(2)
            screenshot(driver)


            """try:
                driver.save_screenshot(destination)
                print("Screenshot was saved to: " + destination)
            except NotADirectoryError:
                print("Directory error")"""



        finally:
            driver.quit()

CH = ScreenShot()
CH.test_screenshot()




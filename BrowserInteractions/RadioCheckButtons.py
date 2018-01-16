from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class RadioCheck(object):

    def test(self):
        driver = webdriver.Chrome()
        BaseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        radio1 = driver.find_element(By.ID, "bmwradio")
        radio1.click()
        sleep(1)

        radio2 = driver.find_element(By.ID, "benzradio")
        radio2.click()
        sleep(1)

        radio3 = driver.find_element(By.ID, "hondaradio")
        radio3.click()
        sleep(1)

        check1 = driver.find_element(By.ID, "bmwcheck")
        check1.click()
        sleep(1)

        check2 = driver.find_element(By.ID, "benzcheck")
        check2.click()
        sleep(1)

        check3 = driver.find_element(By.ID, "hondacheck")
        check3.click()
        sleep(2)

        print("Honda radio button is selected: ", str(radio3.is_selected()))
        print("Benz radio button is selected: ", str(radio2.is_selected()))
        print("Honda check is selected: ", str(check3.is_selected()))

        sleep(2)
        driver.quit()

CH = RadioCheck()
CH.test()

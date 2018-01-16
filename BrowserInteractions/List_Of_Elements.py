from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ListOfElements(object):

    def test(self):
        driver = webdriver.Chrome()
        BaseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        listOfRadio = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name, 'cars')]")
        size = len(listOfRadio)
        print("Size of list is: " + str(size))

        for item in listOfRadio:
            isSelected = item.is_selected()
            print(str(isSelected))
            if not isSelected:
                item.click()
                sleep(1)

        sleep(2)
        driver.quit()

CC = ListOfElements()
CC.test()

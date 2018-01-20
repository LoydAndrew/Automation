from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropdownSelect(object):

    def test(self):
        driver = webdriver.Chrome()
        BaseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(BaseUrl)
        driver.maximize_window()
        #driver.implicitly_wait(5)
        element = driver.find_element_by_id("carselect")

        select_element = Select(element)
        select_element.select_by_value("benz")
        print ("Benz was selected by value")
        sleep(3)

        select_element.select_by_index("2")
        print("Honda was selected by index")
        sleep(3)

        select_element.select_by_visible_text("BMW")
        print ("Bmw was selected by visible text")
        sleep(3)

        select_element.select_by_index("2")
        print("Honda was selected by index")
        sleep(2)

        driver.quit()

CH = DropdownSelect()
CH.test()


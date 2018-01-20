from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HideShow(object):

    def testKodeit(self):
        driver = webdriver.Chrome()
        BaseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.get(BaseUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)

        text_box_element = driver.find_element_by_id("displayed-text")
        driver.execute_script("arguments[0].scrollIntoView(false);", text_box_element)
        print("Finding textboxelement by id")
        text_state = text_box_element.is_displayed()
        print ("The enabled state is " + str(text_state))
        sleep(2)

        driver.find_element_by_id("hide-textbox").click()
        sleep(2)
        text_state = text_box_element.is_displayed()
        print("The enabled state is " + str(text_state))
        sleep(2)

        driver.find_element_by_id("show-textbox").click()
        text_state = text_box_element.is_displayed()
        print("The enabled state is " +str(text_state))
        sleep(2)
        driver.close()

    def testExpedia(self):
        driver = webdriver.Chrome()
        NewUrl = "https://www.expedia.com"
        driver.get(NewUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)

        driver.find_element_by_id('tab-flight-tab-hp').click()
        elementChildren = driver.find_element_by_id('flight-children-hp-flight')
        sleep(1)
        Select(elementChildren).select_by_index("2")
        print("One Children selected in dropdown")
        child_age_dd = driver.find_element_by_id("flight-age-select-1-hp-flight")
        print (child_age_dd.text)
        sleep(2)
        driver.quit()


CH = HideShow()
CH.testKodeit()
CH.testExpedia()
from selenium import webdriver
from time import sleep
from Constants import expedia_url

class GetAttribute(object):

    def test(self):
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(expedia_url)
        #driver.implicitly_wait(5)

        element = driver.find_element_by_id("tab-hotel-tab-hp")
        element_attribute = element.get_attribute('type')
        print ("The name of attribute: %s" % element_attribute)
        sleep(1)
        driver.quit()


CH = GetAttribute()
CH.test()

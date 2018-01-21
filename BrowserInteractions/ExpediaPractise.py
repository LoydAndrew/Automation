from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class ExpediaTest(object):

    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.expedia.com")
        driver.maximize_window()
        #driver.implicitly_wait(5)

        try:
            driver.find_element_by_id("tab-hotel-tab-hp").click()#finding hotels tab
            sleep(2)
            input_element = driver.find_element_by_id("hotel-destination-hp-hotel")
            input_element.send_keys("Kiev")

            driver.find_element_by_id('hotel-checkin-hp-hotel').send_keys(
                '01/22/2018')
            sleep(1)

            checkout = driver.find_element_by_id('hotel-checkout-hp-hotel')
            checkout.clear()
            checkout.send_keys('01/28/2018')
            sleep(2)

            select_guests = Select(driver.find_element_by_css_selector(
                "select[data-gcw-guests-toggled-field-on-value='99']"))
            select_guests.select_by_value("1")
            sleep(1)

            driver.find_element_by_id('hotel-add-car-checkbox-hp-hotel').click()
            #sleep(1)
            driver.find_element_by_css_selector(
                '#gcw-hotel-form-hp-hotel [type="submit"]').click()


        finally:
            driver.quit()

CH = ExpediaTest()
CH.test()
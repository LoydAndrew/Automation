from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class ExpediaTest(object):

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.expedia.com")
        #driver.implicitly_wait(5)

        try:
            driver.find_element_by_id("tab-hotel-tab-hp").click()#finding hotels tab
            sleep(2)
            search_element = driver.find_element_by_id("hotel-destination-hp-hotel")
            search_element.send_keys("Kiev")

            #choosing checkin and checkout dates
            driver.find_element_by_id('hotel-checkin-hp-hotel').send_keys(
                '01/22/2018')
            sleep(1)

            checkout = driver.find_element_by_id('hotel-checkout-hp-hotel')
            checkout.clear()
            checkout.send_keys('01/28/2018')
            sleep(1)
            #clicking on dropdown and choosing number of guests
            guests_element = driver.find_element_by_css_selector(
                "select[data-gcw-guests-toggled-field-on-value='99']")
            guests_element.click()
            select_guests = Select(guests_element).select_by_value('1')
            sleep(1)
            #choosing car option
            car_selected = driver.find_element_by_id('hotel-add-car-checkbox-hp-hotel')
            car_selected.click()
            print("Car option is selected: " + str(car_selected.is_enabled()))
            #sleep(1)
            #submiting all that was selected
            driver.find_element_by_css_selector(
                '#gcw-hotel-form-hp-hotel [type="submit"]').click()


        finally:
            driver.quit()

CH = ExpediaTest()
CH.test()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from Constants import expedia_url
from time import sleep


class ExplicitWait(object):

    # noinspection PyMethodMayBeStatic
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(expedia_url)
        #driver.implicitly_wait(0.5)

        try:
            driver.find_element_by_id("tab-flight-tab-hp").click()
            driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
            driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
            driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("01/28/2018")
            return_date = driver.find_element_by_id("flight-returning-hp-flight")
            return_date.clear()
            return_date.send_keys("03/30/2018")
            driver.find_element_by_css_selector(
                "#gcw-flights-form-hp-flight .search-btn-col").click()
            driver.find_element_by_id("stopFilter_stops-1").click()

            wait = WebDriverWait(
                driver,
                10,
                poll_frequency=1,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotSelectableException,
                    ElementNotVisibleException])

            element = wait.until(ec.element_to_be_clickable((
                By.XPATH, "//button[@data-test-id='select-button']"))
                       )

            element.click()
            sleep(3)
        finally:
            driver.quit()


CH = ExplicitWait()
CH.test()

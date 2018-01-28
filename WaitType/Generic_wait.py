from selenium import webdriver
from selenium.webdriver.common.by import By
from Constants import expedia_url
from HandyWrapper import Explicitly_Wait
from time import sleep


class ExplicitWait2(object):

    # noinspection PyMethodMayBeStatic
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(expedia_url)
        explicit_wait = Explicitly_Wait(driver)

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
            check_box = explicit_wait.wait_for_element(
                "stopFilter_stops-1",timeout=10)
            check_box.click()

            element = explicit_wait.wait_for_element(
                "//button[@data-test-id='select-button']",
                "xpath")

            element.click()
            sleep(3)
        finally:
            driver.quit()


CH = ExplicitWait2()
CH.test()

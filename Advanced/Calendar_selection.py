from selenium import webdriver
from selenium.webdriver.common.by import By
from Constants import expedia_url
from time import sleep

class Calendar():

    def test_day(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(expedia_url)
        driver.implicitly_wait(3)

        try:
            driver.find_element_by_id("tab-flight-tab-hp").click()
            driver.find_element(By.ID, "flight-departing-hp-flight").click()
            select_date = driver.find_element(By.XPATH,"//button[@data-day='31']")
            driver.execute_script("arguments[0].scrollIntoView(false);", select_date)
            sleep(3)
            select_date.click()
            sleep(3)
        finally:
            driver.quit()

    def test_month(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(expedia_url)
        driver.implicitly_wait(3)

        try:
            driver.find_element_by_id("tab-flight-tab-hp").click()
            driver.find_element(By.ID, "flight-departing-hp-flight").click()
            select_date = driver.find_element(By.XPATH,
                                              "//div[@class='datepicker-cal-month'][position()=1]//tr[position()=5]")
            valid_dates = select_date.find_elements(By.TAG_NAME, "td")

            for date in valid_dates:
                if date.text == "29":
                    date.click()
                    break
            sleep(3)
        finally:
            driver.quit()


CH = Calendar()
#CH.test_day()
CH.test_month()

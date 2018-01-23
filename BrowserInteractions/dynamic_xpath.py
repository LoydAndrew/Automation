from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class DynamicXpath(object):
    def test_dynamic(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/courses")
        driver.implicitly_wait(3)

        search_box = driver.find_element(By.ID, 'search-courses')
        search_box.send_keys("Java")
        search_box.submit()
        try:
            course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
            course_text = course.format("JavaScript for beginners")
            find_course = driver.find_element(By.XPATH, course_text)
            sleep(1)
            find_course.click()
        finally:
            driver.quit()


CH = DynamicXpath()
CH.test_dynamic()

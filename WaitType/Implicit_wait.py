from selenium import webdriver
from selenium.webdriver.common.by import By
from Constants import kodeit_courses
from time import sleep



class ImplicitWait(object):

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_courses)
        #driver.implicitly_wait(3)# will wait for every element for 3 seconds

        element = driver.find_element_by_xpath("//a[@href='/sign_in']")
        element.click()

        element2 = driver.find_element(By.CSS_SELECTOR,"user_email")
        element2.send_keys("Hello")# will fail without implicitly_wait(3)

        sleep(2)
        driver.quit()

CH = ImplicitWait()
CH.test()

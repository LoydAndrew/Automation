
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByClassTag(object):
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        # driver.maximize_window()
        driver.get(baseUrl)
        elementByid = driver.find_element(By.ID, "name")
        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        elementByCss = driver.find_element(By.CSS_SELECTOR,"#openwindow")
        elementByCss.click()
        elementbylinktext = driver.find_element(By.LINK_TEXT, "Login")
        elementByTag = driver.find_element(By.TAG_NAME, 'header')

        if elementByXpath is not None:
            print("The 'Hide-show' element was found by class-name on Letskodeit")
        if elementByid is not None:
            print("The 'Practise' element was found by tag Letskodeit ")
        if elementbylinktext is not None:
            print("The Login was found By.Link_Text")
        if elementByCss is not None:
            print("The openwindow was found By.CSS_Selector")
        if elementByTag is not None:
            print("Header was found By.Tag_NAME")


FF = FindByClassTag()
FF.test()

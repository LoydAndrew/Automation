from selenium import webdriver
from selenium.webdriver.common.by import By


class FindLists(object):
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseUrl)

        elements_by_class = driver.find_elements_by_class_name('inputs')
        length_of_inputs = len(elements_by_class)

        if elements_by_class is not None:
            print("Found list of inputs with a length of " + str(length_of_inputs))

        elements_by_tag = driver.find_elements(By.TAG_NAME, "th")
        length_of_tag = len(elements_by_tag)

        if elements_by_tag is not None:
            print("Found list of 'th' with a length of " + str(length_of_tag))


FF = FindLists()
FF.test()


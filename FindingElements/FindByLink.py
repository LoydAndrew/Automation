from  selenium import webdriver


class FindByXpathCss(object):
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByLink = driver.find_element_by_link_text("Login")
        elementByPartialLink = driver.find_element_by_partial_link_text("Pract")
        if elementByLink is not None:
            print ("The 'Login' element was found by link on Letskodeit")
        if elementByPartialLink is not None:
            print ("The 'Practise' element was found by partial Letskodeit")




FF = FindByXpathCss()
FF.test()









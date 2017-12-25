from  selenium import webdriver


class FindByXpathCss(object):
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        elementByCss = driver.find_element_by_css_selector('#displayed-text')
        if elementByXpath is not None:
            print ("The 'name' element was found by xpath on Letskodeit")
        if elementByCss is not None:
            print ("The 'show-hide' element was found by css Letskodeit")

        driver = webdriver.Chrome()
        driver.maximize_window()
        promUrl = 'https://prom.ua'
        driver.get(promUrl)
        elementByNameProm = driver.find_element_by_css_selector("#search_form")
        elementByNameProm.send_keys("мобильные телефоны")
        if elementByNameProm is not None:
            print ("The 'search_term' element was found by css on Prom")


FF = FindByXpathCss()
FF.test()









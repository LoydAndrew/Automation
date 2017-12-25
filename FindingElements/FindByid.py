from  selenium import webdriver

class Findbyid(object):
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        elementByName = driver.find_element_by_name("show-hide")
        if elementById is not None:
            print ("The 'name' element was found by id on Letskodeit")
        if elementByName is not None:
            print ("The 'show-hide' element was found by name Letskodeit")

        driver = webdriver.Chrome()
        driver.maximize_window()
        promUrl = 'https://prom.ua'
        driver.get(promUrl)
        elementByNameProm = driver.find_element_by_name('search_term')
        elementByNameProm.send_keys("мобильные телефоны")
        if elementByNameProm is not None:
            print ("The 'search_term' element was found by name on Prom")


FF = Findbyid()
FF.test()









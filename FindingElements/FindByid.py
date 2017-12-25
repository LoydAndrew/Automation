from  selenium import webdriver

class Findbyid(object):
    def test(self):
        #baseUrl = "https://letskodeit.teachable.com/p/practice"
        promUrl = 'https://prom.ua'
        driver = webdriver.Firefox()
        #driver.get(baseUrl)
        driver.get(promUrl)
        #elementById = driver.find_element_by_id("name")
        #elementByName = driver.find_element_by_name("show-hide")
        #if elementById is not None:
            #print ("The name element was found by id")
        elementByName = driver.find_element_by_name('search_term')
        if elementByName is not None:
            print ("The name element was found by name")

FF = Findbyid()
FF.test()









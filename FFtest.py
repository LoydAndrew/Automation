from selenium import webdriver

class RunFFtest(object):
    def test(self):
        driver = webdriver.Firefox() #evoking Firefox
        driver.get("http://www.letskodeit.com") #evoking testpage


FF = RunFFtest()
FF.test()






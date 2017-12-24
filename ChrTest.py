from selenium import webdriver

class RunCHRtest(object):
    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")


Chr = RunCHRtest()
Chr.test()

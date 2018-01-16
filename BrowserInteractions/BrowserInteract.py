from selenium import webdriver

class BrowserInteract():

    def Test(self):
        self.driver = webdriver.Firefox()
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        self.driver.maximize_window()
        self.driver.get(baseUrl)
        title = self.driver.title
        print("Title of the webpage is: " + title)
        currentUrl = self.driver.current_url
        print("Current url is: " + currentUrl)
        self.driver.refresh()
        print("Refreshing browser for the 1 time")
        self.driver.get(currentUrl)
        print("Refreshing browser for the second time")
        self.driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        currentUrl = self.driver.current_url
        print("Current url is: " + currentUrl)
        self.driver.back()
        print("One page back in browser history")
        currentUrl = self.driver.current_url
        print("Current url is: " + currentUrl)
        self.driver.forward()
        print("Going one step forward")
        currentUrl = self.driver.current_url
        print("Current url is: " + currentUrl)
        pageSource = self.driver.page_source
        print(pageSource)
        self.driver.quit()



FF = BrowserInteract()
FF.Test()
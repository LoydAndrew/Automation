from selenium.webdriver.common.by import By


class HandyWrapper():
    def __init__(self, driver):
        self.driver = driver

    def GetByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID

        if locator_type == "xpath":
            return By.XPATH

        if locator_type == "css":
            return By.CSS_SELECTOR

        if locator_type == "class_name":
            return By.CLASS_NAME

        if locator_type == "link_text":
            return By.LINK_TEXT

        if locator_type == "tag_name":
            return By.TAG_NAME

        if locator_type == "name":
            return By.NAME

        if locator_type == "partial_link_text":
            return By.PARTIAL_LINK_TEXT

        else:
            print("Locator type " + str(locator_type) + "is not supported")
        return False

    def get_element(self,locator,locator_type="id"):
        element = None
        try:
            by_type = self.GetByType(locator_type)
            element = self.driver.find_element(by_type,locator)
            print("Element was found by: " + str(by_type))
        except:
            print("Element was not found")
        return element


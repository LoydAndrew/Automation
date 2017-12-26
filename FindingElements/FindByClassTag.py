from  selenium import webdriver


class FindByClassTag(object):
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByClass = driver.find_element_by_class_name("displayed-class")
        elementByClass.send_keys("Testing input")

        elementByTag = driver.find_element_by_tag_name("h1")
        text = elementByTag.text
        if elementByClass is not None:
            print ("The 'Hide-show' element was found by class-name on Letskodeit")
        if elementByTag is not None:
            print ("The 'Practise' element was found by tag Letskodeit " + text )




FF = FindByClassTag()
FF.test()









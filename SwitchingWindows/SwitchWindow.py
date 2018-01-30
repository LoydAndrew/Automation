from selenium import webdriver
from selenium.webdriver.common.by import By
from Constants import kodeit_practise_url
from time import sleep

class Switch():

    def switch_to_window(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(kodeit_practise_url)
        driver.implicitly_wait(5)

        try:
            #Finding parent handle
            parent_handle = driver.current_window_handle
            print("Parent handle is " + str(parent_handle))
            driver.find_element(By.ID, "openwindow").click()
            sleep(2)
            #Finding all handles
            handles = driver.window_handles
            #Switching to window
            for handle in handles:
                print("Parent_handle: " + str(handle))
                if handle not in parent_handle:
                    driver.switch_to.window(handle)
                    print("Switch to window: " + handle)
                    search_box = driver.find_element(By.ID, "search-courses")
                    search_box.send_keys("python")
                    sleep(2)
                    driver.close()
            #switch back to parent window

            driver.switch_to.window(parent_handle)
            driver.find_element(By.ID, "name").send_keys("success")
            sleep(2)
        finally:
            driver.quit()


CH = Switch()
CH.switch_to_window()
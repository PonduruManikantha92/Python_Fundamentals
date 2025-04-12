from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class types_of_exceptions():
    def no_such_element_exception(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")


        # try:
        #     driver = webdriver.Chrome()
        #     driver.find_element(By.ID, "nonexistent-id")
        # except NoSuchElementException:
        #     print("Element not found!")
        #

testing = types_of_exceptions()
testing.no_such_element_exception()
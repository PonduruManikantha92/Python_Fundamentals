from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class invoke_browser():
    def headed_browser(self):
        driver = webdriver.Chrome
        driver.get("https://www.google.com")

    def headless_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        

browser = invoke_browser()
browser.headed_browser()
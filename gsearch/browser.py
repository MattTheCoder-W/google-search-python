from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Browser:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://google.com")
        sleep(1)
        self.reject_google_cookies()

    def reject_google_cookies(self):
        button_selector = "button#W0wltc"
        button_element = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        button_element.click()

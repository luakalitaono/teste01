from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located


class Config:

    def __init__(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(chrome_options=option, executable_path="C:/chromedriver.exe")
        self.driver.get("https://app.iclinic.com.br/")

    def find(self, *locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))
        return element

    def find_not(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(invisibility_of_element_located(*locator))

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located


class LoginIn:

    def __init__(self, driver, username, password):
        self.driver = driver
        self.NAME = (By.ID, "email")
        self.PASS = (By.ID, "password")
        self.SUBMIT = (By.CSS_SELECTOR, "span[class='MuiButton-label']")
        self.LOGOUT = (By.ID, "bt_logout")
        self.RESULT = (By.CSS_SELECTOR, "div[class='name-employee']")
        self.login(username, password)

    def find(self, *locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))
        return element

    def find_not(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(invisibility_of_element_located(*locator))

    def login(self, user, password):
        self.find(self.NAME).send_keys(user)
        self.find(self.PASS).send_keys(password)
        self.find(self.SUBMIT).click()
        sleep(2)

        assert user == self.find(self.RESULT).get_attribute("innerHTML")
        print("User: " + self.find(self.RESULT).get_attribute("innerHTML"))

    def logout(self):
        self.find(self.LOGOUT).click()

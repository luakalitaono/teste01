from selenium.webdriver.common.by import By
from time import sleep
"""Register New User"""


class RegisterUser:

    def __init__(self, config):
        self.config = config
        self.driver = config.driver

        """STEP 01"""
        self.EMAIL = (By.ID, "email")
        self.CHECKBOX_TERMS = (By.CSS_SELECTOR, "span[data-ga='setup-termsOfServiceAndPrivacyPolicy']")
        self.SUBMIT01 = (By.CSS_SELECTOR, "button[type='submit']")

        """STEP 02"""
        self.NAME = (By.ID, "name")
        self.PHONE = (By.ID, "billing_phone")
        self.PROFESSION = (By.ID, "profession")
        self.OPTION_PROFESSION = (By.CSS_SELECTOR, "li[data-value='Recepcionista']")
        self.SUBMIT02 = (By.CSS_SELECTOR, "button[data-ga='setup-avancar_2_etapa']")

        """STEP03"""
        self.PASS = (By.ID, "password")
        self.SUBMIT03 = (By.CSS_SELECTOR, "button[data-ga='setup-avancar_3_etapa']")

        self.LOGOUT = (By.ID, "bt_logout")
        self.RESULT = (By.CSS_SELECTOR, "div[class='name-employee']")

        self.test_start()

    def test_start(self):
        self.step01("usuariogithub@iclinic.com.br")
        self.step02("usuario1", "92981993613")
        self.step03("Usuario1!")

    def step01(self, email):
        self.config.find(self.EMAIL).send_keys(email)
        self.config.find(self.CHECKBOX_TERMS).click()
        sleep(1)

        self.config.find(self.SUBMIT01).click()
        sleep(1)

    def step02(self, name, phone):
        self.config.find(self.NAME).send_keys(name)
        self.config.find(self.PHONE).send_keys(phone)
        self.config.find(self.PROFESSION).click()
        self.config.find(self.OPTION_PROFESSION).click()
        sleep(1)

        self.config.find(self.SUBMIT02).click()
        sleep(1)

    def step03(self, password):
        self.config.find(self.PASS).send_keys(password)
        sleep(1)
        self.config.find(self.SUBMIT03).click()

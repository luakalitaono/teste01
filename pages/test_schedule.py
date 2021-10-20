from selenium.webdriver.common.by import By
from time import sleep


class Schedule:

    def __init__(self, config):
        self.config = config
        self.driver = config.driver
        self.SCHEDULE = (By.LINK_TEXT, "Agenda")
        self.DATE = (By.CSS_SELECTOR, "div[class='week-day-inner'] [data-reactid='.4.0.1.2.0.0.0.0.$=1$0.$0.2.$1.0']")
        self.PROCEDURE = (By.CSS_SELECTOR, "div[class='filter-option']")
        self.OPTION_PROCEDURE = (By.ID, "bs-select-1-1")
        self.QUANTITY = (By.CSS_SELECTOR, "input[class='form-control']")
        self.PATIENT_NAME = (By.CSS_SELECTOR, "input[name='patient_name']")
        self.PHONE_MOBILE = (By.CSS_SELECTOR, "input[name='patient_mobile_phone']")
        self.HOME_PHONE = (By.CSS_SELECTOR, "input[name='patient_home_phone']")
        self.PATIENT_EMAIL = (By.CSS_SELECTOR, "input[name='patient_email']")
        self.INSURANCE = (By.CSS_SELECTOR, "select[name='insurance']")
        self.OPTION_INSURANCE = (By.CSS_SELECTOR, "a[id='bs-select-5-1']")
        self.DESCRIPTION = (By.CSS_SELECTOR, "input[name='description']")
        self.BT_SAVE = (By.CSS_SELECTOR, "button[data-ga='modal_agendamento-btn_salvar']")

        self.test_start()

    def test_start(self):
        self.access("https://app.iclinic.com.br/agenda/")
        self.schedule("2", "Paciente 01", "1699999999", "1655555555", "paciente01@gmail.com", "teste 01")

    def access(self, url):
        self.config.find(self.SCHEDULE).click()
        assert self.driver.current_url == url

    def schedule(self, quant, patient_name, phone_mobile, home_phone, patient_email, description):
        self.config.find(self.DATE).click()
        sleep(1)

        """Scheduling data"""
        self.config.find(self.PROCEDURE).click()
        self.config.find(self.OPTION_PROCEDURE).click()
        self.config.find(self.QUANTITY).clear()
        self.config.find(self.QUANTITY).send_keys(quant)
        self.config.find(self.PATIENT_NAME).send_keys(patient_name)
        self.config.find(self.PHONE_MOBILE).send_keys(phone_mobile)
        self.config.find(self.HOME_PHONE).sende_keys(home_phone)
        self.config.find(self.PATIENT_EMAIL).send_keys(patient_email)
        self.config.find(self.INSURANCE).click()
        self.config.find(self.OPTION_INSURANCE).click()
        self.config.find(self.DESCRIPTION).send_keys(description)

        assert quant in self.config.find(self.QUANTITY).get_attribute("value")
        assert patient_name in self.config.find(self.PATIENT_NAME).get_attribute("value")
        assert phone_mobile in self.config.find(self.PHONE_MOBILE).get_attribute("value")
        assert home_phone in self.config.find(self.HOME_PHONE).get_attribute("value")
        assert patient_email in self.config.find(self.PATIENT_EMAIL).get_attribute("value")
        assert description in self.config.find(self.DESCRIPTION).get_attribute("value")

        print("Quantidade: " + self.config.find(self.QUANTITY).get_attribute("value"))
        print("Nome do paciente: " + self.config.find(self.PATIENT_NAME).get_attribute("value"))
        print("Telefone móvel: " + self.config.find(self.PHONE_MOBILE).get_attribute("value"))
        print("Telefone residencial: " + self.config.find(self.HOME_PHONE).get_attribute("value"))
        print("Email do paciente: " + self.config.find(self.PATIENT_EMAIL).get_attribute("value"))
        print("Observações: " + self.config.find(self.DESCRIPTION).get_attribute("value"))

        self.config.find(self.BT_SAVE).click()

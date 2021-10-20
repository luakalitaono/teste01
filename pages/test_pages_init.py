from helpers.test_configFind import Config
from time import sleep
from datetime import datetime
from pages.test_login import LoginIn
from pages.test_schedule import Schedule


def test_schedule():
    start = datetime.now().replace(microsecond=0)
    print('-- Init Schedule Test --', start)
    login = LoginIn(driver, 'usuariogithub@iclinic.com.br', 'Usuario1!')
    sleep(2)

    print('Now testing: Schedule')
    Schedule(config)
    sleep(2)

    login.logout()
    duration = datetime.now().replace(microsecond=0) - start
    print('-- End Schedule Test --', duration)


config = Config()
driver = config.driver
test_schedule()
driver.quit()

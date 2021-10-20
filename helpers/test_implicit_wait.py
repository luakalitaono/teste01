from selenium import webdriver
import time


def calculate_implicit_wait_time(driver, wait_value):

    # somente entre se tiver valor.
    if wait_value:
        driver.implicitly_wait(wait_value)

    # dou o clique no elemento.
    driver.find_element_by_id("bt01").click()

    # função para pegar o tempo em segundos.
    now = time.time()

    try:
        myelement = driver.find_element_by_id("meuId")

    # caso der erro vai entrar na exceção e imprimir o erro.
    except Exception as x:
        print(x)

    # mostrando que é preciso aplicar somente uma vez.
    # fazendo o teste com o outro botão.
    driver.find_element_by_id("bt02").click()

    try:
        myelement = driver.find_element_by_id("meuId2")

    # caso der erro vai entrar na exceção e imprimir o erro.
    except Exception as x:
        print(x)

    # imprime a media do tempo.
    print(str(int(time.time()-now))+'--Seconds')


driver = webdriver.Chrome()
driver.get("http://10.60.70.204/home")
calculate_implicit_wait_time(driver, 100, "test")
driver.close()

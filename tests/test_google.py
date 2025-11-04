from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_busqueda_google():
    options = Options()
    options.add_argument("--headless")  # Modo sin interfaz gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")

    caja = driver.find_element(By.NAME, "q")
    caja.send_keys("ChatGPT\n")

    # Espera corta para que la búsqueda complete (mejor que depender del título)
    time.sleep(1)

    # Verificamos la URL de búsqueda de forma robusta
    cond = ("search" in driver.current_url) or ("q=ChatGPT" in driver.current_url)
    assert cond, f"URL inesperada: {driver.current_url}"

    # (Opcional) verificar que aparezcan elementos de resultados
    resultados = driver.find_elements(By.CSS_SELECTOR, "div.g")
    assert len(resultados) > 0, "No se encontraron resultados en Google"

    driver.quit()


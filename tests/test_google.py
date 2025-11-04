from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_busqueda_google():
    options = Options()
    options.add_argument("--headless")  # Modo sin interfaz gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")

    caja = driver.find_element(By.NAME, "q")
    caja.send_keys("ChatGPT\n")

    assert "ChatGPT" in driver.title
    driver.quit()

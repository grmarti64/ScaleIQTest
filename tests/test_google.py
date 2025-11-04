from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_busqueda_google():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")

    caja = driver.find_element(By.NAME, "q")
    caja.send_keys("ChatGPT")
    caja.submit()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
        )
    except Exception:
        driver.quit()
        assert False, "No se encontraron resultados visibles en Google"

    assert "search" in driver.current_url or "ChatGPT" in driver.page_source

    driver.quit()

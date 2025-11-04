from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_busqueda_en_python_org():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.python.org")

    titulo = driver.title
    print("Título:", titulo)

    # Verificamos que el título contenga "Python"
    assert "Python" in titulo

    # Buscamos el campo de búsqueda y escribimos algo
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("testing\n")

    assert "results" in driver.current_url
    driver.quit()

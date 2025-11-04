from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_busqueda_en_python_org():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.python.org")

    assert "Python" in driver.title

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("testing")
    search_box.submit()  # en lugar de \n

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    assert "/search/" in driver.current_url or "search" in driver.page_source

    driver.quit()
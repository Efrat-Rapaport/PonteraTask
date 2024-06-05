from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import URL

def login(driver, username, password, select_firm_value):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        username_input = wait.until(EC.presence_of_element_located((By.ID, "loginEmail")))
        username_input.send_keys(username)

        password_input = driver.find_element(By.ID, "loginPassword")
        password_input.send_keys(password)

        button_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-blue-light")))
        button_element.click()

        select_firm = wait.until(EC.presence_of_element_located((By.NAME, "orgId")))
        select = Select(select_firm)
        select.select_by_value(select_firm_value)

        button_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-blue-light")))
        button_element.click()

        return driver
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()
        return None

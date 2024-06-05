from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import new_client_fn, new_client_ln


def add_new_client(driver):
    wait = WebDriverWait(driver, 20)
    try:
        add_client_button = wait.until(EC.element_to_be_clickable((By.ID, "addNewClientBtnId")))
        add_client_button.click()

        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "first_name")))
        first_name_input.send_keys(new_client_fn)

        last_name_input = driver.find_element(By.ID, "last_name")
        last_name_input.send_keys(new_client_ln)

        # Fill all other inputs...

        add_client_button = wait.until(EC.element_to_be_clickable((By.ID, "save-client-changes-btn")))
        add_client_button.click()

        return driver
    except Exception as e:
        print(f"Add new client failed: {e}")
        driver.quit()
        return None


def validate_client_in_grid(driver, client_name):
    wait = WebDriverWait(driver, 10)
    clients_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "my-clients-table")))

    client_found = False
    clients = clients_grid.find_elements(By.TAG_NAME, "tr")
    for client in clients:
        if client_name in client.text:
            client_found = True
            break

    assert client_found, f"Client {client_name} not found in the clients grid."


def delete_client(driver, full_name):
    wait = WebDriverWait(driver, 10)
    clients_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "my-clients-table")))
    clients = clients_grid.find_elements(By.TAG_NAME, "tr")
    for client in clients:
        if full_name in client.text:
            client.click()

            delete_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fa-trash-can")))
            delete_icon.click()

            delete_button = wait.until(EC.element_to_be_clickable((By.ID, "feedback5")))
            delete_button.click()

            confirm_delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light-blue.btn-lg[type='submit']")))
            confirm_delete_button.click()
            break

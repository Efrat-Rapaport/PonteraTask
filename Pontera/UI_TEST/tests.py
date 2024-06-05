from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import user_name, password, select_firm_value, new_client_fn, new_client_ln
from login import login
from client_funcs import add_new_client, validate_client_in_grid, delete_client


def test_new_client_appears_in_clients_grid():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        full_name = f"{new_client_fn} {new_client_ln}"

        login(driver, user_name, password, select_firm_value)
        # add_new_client(driver)
        validate_client_in_grid(driver, full_name)
        delete_client(driver, full_name)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_new_client_appears_in_clients_grid()

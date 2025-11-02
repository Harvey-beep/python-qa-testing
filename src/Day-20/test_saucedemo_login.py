import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # --- Setup ---
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    # This is an "implicit wait" - a bad idea, but simple for now
    # driver.implicitly_wait(5)

    # Yield controls the driver back to the test
    yield driver

    # --- Teardown ---
    driver.quit()

# Test names MUST start with test_
def test_valid_login(driver):
    # Use the 'driver' fixture
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify we are on the inventory page
    # Use an explicit wait for the URL
    WebDriverWait(driver, 5).until(
        EC.url_contains("inventory.html")
    )
    assert "inventory.html" in driver.current_url
    time.sleep(2)

@pytest.mark.smoke
def test_invalid_login_locked_user(driver):
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify error message appears
    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Sorry, this user has been locked out." in error_msg.text
    time.sleep(3)
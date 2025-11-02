import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

try:
    # Find elements
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.NAME, "password")
    # A better locator for the button: CSS Selector
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Interact with them
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(1) # See it type
    login_button.click()

    # Verify the result
    time.sleep(1)
    flash_message = driver.find_element(By.ID, "flash")

    # Get the text from the green box
    message_text = flash_message.text
    print(f"Message: {message_text}")

    assert "You logged into a secure area!" in message_text
    print("Login successful!")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    time.sleep(2)
    driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:   
    google_search_field = driver.find_element(By.NAME, "q")
    for char in "selenium python":
        google_search_field.send_keys(char)
        time.sleep(0.2)

    wait = WebDriverWait(driver, 10)
    finish_submit_button = wait.until(
        EC.presence_of_element_located((By.NAME, "btnK"))
    )
    google_search_buttons = driver.find_elements(By.NAME, "btnK")
    for button in google_search_buttons:
        if button.is_displayed():
            time.sleep(2)
            button.click()
            break

    finish_text_element = wait.until(
        EC.title_contains("selenium python")
    )

    print("Test passed!")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    driver.quit()
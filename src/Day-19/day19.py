from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

try:
    # Find start button using XPath
    # //tag[@attribute='value]
    start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    start_button.click()

    # Now we MUST wait for the "Hello World" text to appear
    # Create a wait object: 10 second timeout
    wait = WebDriverWait(driver, 10)

    # Wait until the element with ID 'finish' is visible
    # This is an EXPLICIT WAIT
    finish_text_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    # Once it's visible, get the text
    finish_text = finish_text_element.text
    print(f"Found text: {finish_text}")
    assert finish_text == "Hello World!"
    print("Test Passed!")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    driver.quit()

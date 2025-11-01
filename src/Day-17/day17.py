import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

try:
    # Find the username field by its ID
    # In Chrome: Right-click > Inspect on the field to find its ID
    username_field = driver.find_element(By.ID, "username")
    print("Found username field by ID.")

    # Find the password field by its NAME
    password_field = driver.find_element(By.NAME, "password")
    print("Found password field by NAME.")

    # Find the login button by its CLASS
    # Note: This class 'radius' might be on other elements!
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    print("Found login button by CLASS_NAME.")

    time.sleep(2)

except Exception as e:
    print(f"Error finding element: {e}")

finally: 
    driver.quit()

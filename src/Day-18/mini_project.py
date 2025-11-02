# Mini Project for Day 18
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://httpbin.org/forms/post")

try:
    customer_name_field = driver.find_element(By.NAME, "custname")
    telephone_field = driver.find_element(By.NAME, "custtel")
    delivery_time_radio = driver.find_element(By.NAME, "delivery")
    submit_button = driver.find_element(By.TAG_NAME, "button")

    customer_name_field.send_keys("John Doe")
    telephone_field.send_keys("09562314567")
    delivery_time_radio.send_keys("11:00AM")
    time.sleep(1)
    submit_button.click()

    print(f"Current URL after submission: {driver.current_url}")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    time.sleep(2)
    driver.quit()



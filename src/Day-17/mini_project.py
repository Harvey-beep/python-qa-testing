# Mini Project for Day 17
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://httpbin.org/forms/post")

try:
    customer_name_field = driver.find_element(By.NAME, "custname")
    print("Found customer name field by NAME.")

    telephone_field = driver.find_element(By.NAME, "custtel")
    print("Found telephone field by NAME.")

    delivery_time_field = driver.find_element(By.NAME, "delivery")
    print("Found delivery time field by NAME.")

    time.sleep(2)

except Exception as e:
    print(f"Error finding element: {e}")

finally:
    driver.quit()
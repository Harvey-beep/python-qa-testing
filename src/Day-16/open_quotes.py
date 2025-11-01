# Mini Project for Day 16
import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com")

print(f"Page Title: {driver.title}")

assert "Quotes" in driver.title
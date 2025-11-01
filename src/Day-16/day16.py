import time
from selenium import webdriver

# Initialize the Chrome driver
# Selenium will look for chromedriver.exe in the same folder
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print the title of the page
print(f"Page Title: {driver.title}")

# Wait for 3 seconds to see it
time.sleep(3)

# Close the browser
driver.quit()
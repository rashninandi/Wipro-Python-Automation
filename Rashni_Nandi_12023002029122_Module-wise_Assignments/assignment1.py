from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Wait for page to load
time.sleep(2)

# Find username using ID
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Wait
time.sleep(1)

# Find password using NAME
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

# Wait
time.sleep(1)

# Find login button using XPATH
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()

# Wait for next page
time.sleep(3)

# Validate URL
assert "/inventory.html" in driver.current_url

print("Assignment 1 Passed")
print("Current URL:", driver.current_url)

# Close browser
driver.quit()
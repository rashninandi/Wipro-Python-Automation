from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()

# Wait for page to load
time.sleep(2)


# =========================================================
# 1. JAVASCRIPT ALERT
# =========================================================

# Click the Alert button
alert_button = driver.find_element(
    By.ID, "alertBtn"
)
alert_button.click()

# Switch to the alert
alert = driver.switch_to.alert

# Print alert message
print("Alert message:", alert.text)

# Accept the alert
alert.accept()

# Wait
time.sleep(3)


# =========================================================
# 2. JAVASCRIPT CONFIRM
# =========================================================

# Click the Confirm button
confirm_button = driver.find_element(
    By.ID, "confirmBtn"
)
confirm_button.click()

# Switch to the confirm box
confirm = driver.switch_to.alert

# Print confirm message
print("Confirm message:", confirm.text)

# Dismiss the confirm box
confirm.dismiss()

# Wait
time.sleep(3)


# =========================================================
# 3. JAVASCRIPT PROMPT
# =========================================================

# Click the Prompt button
prompt_button = driver.find_element(
    By.ID, "promptBtn"
)
prompt_button.click()

# Switch to the prompt
prompt = driver.switch_to.alert

# Print prompt message
print("Prompt message:", prompt.text)

# Enter text into the prompt
prompt.send_keys("Rashni")

# Accept the prompt
prompt.accept()

# Wait
time.sleep(3)

print("Assignment 4 Passed")

# Close browser
driver.quit()
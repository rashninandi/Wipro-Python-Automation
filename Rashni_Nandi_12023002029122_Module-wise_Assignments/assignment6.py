from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# =========================================================
# 1. IFRAME
# =========================================================

# Open Frames page
driver.get("https://demo.automationtesting.in/Frames.html")

# Wait for page to load
time.sleep(2)

# Locate the iframe
iframe = driver.find_element(By.XPATH, "//iframe")

# Switch to iframe
driver.switch_to.frame(iframe)

# Locate input field inside iframe
input_box = driver.find_element(By.TAG_NAME, "input")

# Enter text
input_box.send_keys("Hello Selenium")

print("Text entered inside iframe successfully.")

# Wait for screenshot
time.sleep(3)

# Switch back to main page
driver.switch_to.default_content()

print("Switched back to main page.")

# =========================================================
# 2. NEW TAB
# =========================================================

# Store main window handle
main_window = driver.current_window_handle

# Open a new browser tab using JavaScript
driver.execute_script("window.open('https://www.selenium.dev/', '_blank');")

# Wait for new tab
time.sleep(3)

# Get all window handles
windows = driver.window_handles

print("Number of open windows:", len(windows))

# Switch to the new tab
for window in windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Get the title of the new tab
new_tab_title = driver.title

print("New tab title:", new_tab_title)

# Wait for screenshot
time.sleep(3)

# Close the new tab
driver.close()

print("New tab closed.")

# Switch back to the main window
driver.switch_to.window(main_window)

print("Switched back to main window.")
print("Main page title:", driver.title)

# Wait for screenshot
time.sleep(3)

print("Assignment 6 Passed")

# Close browser
driver.quit()
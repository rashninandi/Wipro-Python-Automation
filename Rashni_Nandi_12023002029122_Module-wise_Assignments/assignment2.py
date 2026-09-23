from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome
driver = webdriver.Chrome()

# Open Selenium dynamic page
driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Locate the "Reveal a new input" button
reveal_button = wait.until(
    EC.element_to_be_clickable((By.ID, "reveal"))
)

# Click the button
reveal_button.click()

# Wait until the hidden input field becomes visible
input_box = wait.until(
    EC.visibility_of_element_located((By.ID, "revealed"))
)

# Enter text into the dynamically revealed input
input_box.send_keys("Displayed")

# Validate that the text was entered
assert input_box.get_attribute("value") == "Displayed"

print("Assignment 2 Passed")
print("Dynamic input appeared successfully.")
print("Text entered:", input_box.get_attribute("value"))

# Close browser
driver.quit()
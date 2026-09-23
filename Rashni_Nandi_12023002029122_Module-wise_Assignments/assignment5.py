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

# Find all rows in the web table
rows = driver.find_elements(
    By.XPATH, "//table[@id='productTable']/tbody/tr"
)

# Name we want to search for
search_name = "Laptop"

# Variable to store the result
found = False

# Iterate through each row
for row in rows:

    # Get all columns in the current row
    columns = row.find_elements(By.TAG_NAME, "td")

    # Iterate through each column
    for i in range(len(columns)):

        # Check whether the current column contains the name
        if columns[i].text == search_name:

            # Print the complete row
            print("Row found:", row.text)

            # Get the value from the Price column
            price = columns[2].text

            print("Product:", search_name)
            print("Price:", price)

            found = True
            break

    # Stop searching once the row is found
    if found:
        break

# Validate that the product was found
assert found

print("Assignment 5 Passed")

# Close browser
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import json
import time
import os
from datetime import datetime
from html import escape


# =========================================================
# READ TEST DATA FROM JSON
# =========================================================

with open("testdata.json", "r") as file:
    data = json.load(file)


# =========================================================
# CREATE FOLDERS
# =========================================================

os.makedirs("screenshots", exist_ok=True)


# =========================================================
# START BROWSER
# =========================================================

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

steps = []
start_time = datetime.now()


# =========================================================
# REPORT FUNCTION
# =========================================================

def report(step, status):
    steps.append((step, status))


def screenshot(name):
    driver.save_screenshot("screenshots/" + name)


def handle_alert():
    try:
        alert = driver.switch_to.alert
        alert.accept()
        return True
    except NoAlertPresentException:
        return False


# =========================================================
# TEST EXECUTION
# =========================================================

try:

    # 1. Launch browser
    driver.get(data["url"])

    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    screenshot("01_home_page.png")
    report("Launch browser and open application", "PASS")


    # 2. Login
    driver.find_element(
        By.XPATH, "//a[contains(text(),'Signup / Login')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Login to your account')]")
        )
    )

    driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='login-email']"
    ).send_keys(data["email"])

    driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='login-password']"
    ).send_keys(data["password"])

    driver.find_element(
        By.CSS_SELECTOR, "button[data-qa='login-button']"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Logged in as')]")
        )
    )

    screenshot("02_login.png")
    report("Login with existing account", "PASS")


    # 3. Search product
    driver.find_element(
        By.XPATH, "//a[contains(text(),'Products')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'All Products')]")
        )
    )

    search = driver.find_element(By.ID, "search_product")
    search.send_keys(data["product"])

    driver.find_element(By.ID, "submit_search").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Searched Products')]")
        )
    )

    screenshot("03_search_product.png")
    report("Search product: " + data["product"], "PASS")


    # 4. Add product to cart
    product = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'productinfo')][.//p[text()='"
                + data["product"]
                + "']]"
            )
        )
    )

    add_button = product.find_element(
        By.XPATH, ".//a[contains(@class,'add-to-cart')]"
    )

    driver.execute_script(
        "arguments[0].click();",
        add_button
    )

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//u[contains(text(),'View Cart')]")
        )
    )

    screenshot("04_product_added.png")
    report("Add product to cart", "PASS")


    # 5. Open cart
    driver.find_element(
        By.XPATH, "//u[contains(text(),'View Cart')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//section[@id='cart_items']")
        )
    )

    screenshot("05_cart.png")
    report("Open shopping cart", "PASS")


    # 6. Update quantity

    quantity = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.cart_quantity_input")
        )
    )

    # Quantity given in JSON
    json_quantity = int(data["quantity"])

    # Required updated quantity
    updated_quantity = json_quantity + 1

    # Clear existing quantity
    quantity.click()
    quantity.clear()

    # Enter updated quantity
    quantity.send_keys(str(updated_quantity))

    # Click outside the quantity field
    driver.find_element(
        By.XPATH, "//h2[contains(text(),'Shopping Cart')]"
    ).click()

    time.sleep(2)

    # Verify updated quantity
    actual_quantity = quantity.get_attribute("value")

    assert actual_quantity == str(updated_quantity)

    screenshot("06_quantity_updated.png")

    report(
        "Update quantity from "
        + str(json_quantity)
        + " to "
        + actual_quantity,
        "PASS"
    )


    # 7. Verify cart details

    product_name = driver.find_element(
        By.XPATH,
        "//td[contains(@class,'cart_description')]//a"
    ).text

    price = driver.find_element(
        By.XPATH,
        "//td[contains(@class,'cart_price')]//p"
    ).text

    cart_quantity = driver.find_element(
        By.CSS_SELECTOR,
        "input.cart_quantity_input"
    ).get_attribute("value")

    assert product_name == data["product"]
    assert cart_quantity == str(updated_quantity)

    screenshot("07_cart_verified.png")

    report(
        "Verify cart details: "
        + product_name
        + " | "
        + price
        + " | Quantity: "
        + cart_quantity,
        "PASS"
    )


    # 8. Handle popup/alert if available

    handle_alert()

    report(
        "Handle popup/alert if available",
        "PASS"
    )


except Exception as e:

    screenshot("error.png")

    report(
        "Execution error: " + str(e),
        "FAIL"
    )


finally:

    # =====================================================
    # GENERATE EXECUTION REPORT
    # =====================================================

    end_time = datetime.now()

    passed = sum(
        1 for step, status in steps
        if status == "PASS"
    )

    failed = sum(
        1 for step, status in steps
        if status == "FAIL"
    )

    rows = ""

    for step, status in steps:

        rows += (
            "<tr>"
            "<td>" + escape(step) + "</td>"
            "<td>" + status + "</td>"
            "</tr>"
        )

    report_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Capstone Assignment 1 Execution Report</title>

    <style>
        body {
            font-family: Arial;
            margin: 40px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid black;
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: #eeeeee;
        }
    </style>
</head>

<body>

<h1>Capstone Assignment 1 Execution Report</h1>

<p><b>Application:</b> Automation Exercise</p>

<p><b>Start Time:</b> """ + str(start_time) + """</p>

<p><b>End Time:</b> """ + str(end_time) + """</p>

<p><b>Total Steps:</b> """ + str(len(steps)) + """</p>

<p><b>Passed:</b> """ + str(passed) + """</p>

<p><b>Failed:</b> """ + str(failed) + """</p>

<table>

<tr>
    <th>Test Step</th>
    <th>Status</th>
</tr>

""" + rows + """

</table>

</body>
</html>
"""

    with open(
        "execution_report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report_html)

    driver.quit()

    print("Execution completed.")
    print("Execution report: execution_report.html")
# Capstone Assignment 1: Selenium WebDriver Automation

## 1. Project Overview

This project automates an e-commerce purchase scenario using **Selenium WebDriver with Python** on the Automation Exercise website.

The automation covers:

- Launching the browser
- Login using existing credentials
- Searching for a product
- Adding the product to the cart
- Updating the product quantity
- Verifying cart details
- Capturing screenshots
- Reading test data from JSON
- Handling popup/alerts if available
- Generating an HTML execution report

## 2. Application

**Website:** https://automationexercise.com/

## 3. Tools and Technologies

- Python
- Selenium WebDriver
- Google Chrome
- JSON
- HTML

## 4. Project Structure

~~~text
Capstone_Assignment1/
│
├── capstoneProject.py
├── testdata.json
├── execution_report.html
├── README.md
│
└── screenshots/
    ├── 01_home_page.png
    ├── 02_login.png
    ├── 03_search_product.png
    ├── 04_product_added.png
    ├── 05_cart.png
    ├── 06_quantity_updated.png
    ├── 07_cart_verified.png
    └── error.png
~~~

## 5. Test Data

Test data is stored in `testdata.json`.

~~~json
{
    "url": "https://automationexercise.com/",
    "email": "rashninandi2005@gmail.com",
    "password": "Rashni@123",
    "product": "Blue Top",
    "quantity": "2"
}
~~~

The email and password should be replaced with the credentials of the existing Automation Exercise account.

## 6. Test Scenario

### Step 1: Launch Browser

The Chrome browser is launched and the Automation Exercise website is opened.

### Step 2: Login

The existing user credentials are read from `testdata.json` and used to log in.

### Step 3: Search Product

The product name from the JSON file is entered in the search field.

### Step 4: Add Product to Cart

The searched product is selected and added to the shopping cart.

### Step 5: Open Cart

The shopping cart is opened using the `View Cart` option.

### Step 6: Update Quantity

The quantity from `testdata.json` is read and updated.
For example:

~~~text
JSON Quantity = 2
Updated Quantity = 3
~~~

The updated quantity is then verified.

### Step 7: Verify Cart Details

The following cart details are verified:

- Product name
- Product price
- Product quantity

### Step 8: Handle Popup/Alert

The program checks whether a JavaScript alert is available.

If an alert is present, it is accepted.

If no alert is available, execution continues normally.

### Step 9: Screenshots

Screenshots are captured during the important stages of execution and stored in the `screenshots` folder.

The screenshots include:

- Home page
- Login
- Product search
- Product added to cart
- Shopping cart
- Updated quantity
- Verified cart details

### Step 10: Execution Report

After execution, an HTML report named `execution_report.html` is automatically generated.

The report contains:

- Start time
- End time
- Total steps
- Passed steps
- Failed steps
- Execution status of each step

## 7. How to Execute

Open the project folder in Command Prompt or PowerShell.

Run the following command:

~~~bash
python capstoneProject.py
~~~

After successful execution, the following will be generated:

~~~text
execution_report.html
screenshots/
~~~

## 8. Execution Report

The generated HTML execution report is:

~~~text
execution_report.html
~~~

Open this file in a web browser to view the execution results.

## 9. Result

The e-commerce workflow was successfully automated using Selenium WebDriver with Python.

The automation performs login, product search, product addition, quantity update, cart verification, screenshot capture, optional alert handling, and HTML execution report generation.

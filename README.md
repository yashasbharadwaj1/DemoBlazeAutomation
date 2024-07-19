# DemoBlazeAutomation

## About

Automated E-commerce Application (https://www.demoblaze.com/) using Selenium, Pytest with page object mechanism, pytest data driven fixtures implemented in the framework design.

## Setup Instructions


pip install -r requirements.txt

# To run the test cases from the root folder: 

py.test --html="report.html"

# report.html 
# shows a comprehensive test report 

![image](https://github.com/user-attachments/assets/b8b898c9-63b8-4b2b-bce8-11506ac14378)


Chrome runs by default.

# For cross-browser testing, use the following commands: 

py.test --browser_name="chrome" 

py.test --browser_name="firefox" 

py.test --browser_name="edge" 

# Functional Issues Found
Empty Cart Purchasing: Empty cart purchasing is allowed, whereas it should not be possible.

Missing Form Validation: None of the forms (Signup, Login, Purchase) have any sort of data validation.
Example: Signup and Login forms allow numbers in the username field, which should not be allowed.
Purchase form fields allow any data type, whereas some fields, like country, should not allow numbers. This applies to all form fields.

Unrestricted Guest Purchases: Users can add items to the cart and purchase them without logging in.



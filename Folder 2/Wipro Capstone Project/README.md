# 🎓 CAPSTONE PROJECT REPORT

**Project Title:** Design and Development of a Selenium Python Automation Framework  
**Domain:** Quality Assurance & Test Automation  
**Application Under Test:** Demo E-Commerce Web Application (TutorialsNinja)  

---

## 📑 1. ABSTRACT
The objective of this capstone project is to design and develop a highly scalable, robust, and maintainable Test Automation Framework using Python and Selenium WebDriver. The framework is built to automate the core functionalities of an E-Commerce application, specifically the **User Authentication (Login)** and **Product Search** modules. By implementing industry-standard design patterns such as the Page Object Model (POM) and Data-Driven Testing (DDT), this project demonstrates a production-ready approach to software quality assurance.

## 🎯 2. PROBLEM STATEMENT
As web applications grow in complexity, manual testing becomes time-consuming, repetitive, and prone to human error. The goal was to eliminate manual regression efforts for critical E-Commerce workflows by building an automated framework that can:
1. Execute tests rapidly and reliably.
2. Separate test logic from UI locators for easy maintenance.
3. Test multiple datasets dynamically without duplicating code.
4. Automatically capture evidence (screenshots) upon test failure.
5. Generate comprehensive, readable execution reports for stakeholders.

## 🏗️ 3. PROPOSED SOLUTION & ARCHITECTURE
To address the problem statement, a hybrid automation framework was developed. The architecture is modularly divided to ensure maximum reusability and scalability.

### 📁 3.1 Framework Architecture (Directory Structure)
```text
📦 Wipro capstone project
 ┣ 📂 config
 ┃ ┗ 📜 config.ini            # Centralized configuration (URL, Browser, Timeouts)
 ┣ 📂 data
 ┃ ┗ 📜 test_data.csv         # External test data for Data-Driven execution
 ┣ 📂 pages
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 base_page.py          # Core Selenium wrapper methods (waits, clicks, interactions)
 ┃ ┣ 📜 login_page.py         # Encapsulated locators and actions for the Login Page
 ┃ ┗ 📜 search_page.py        # Encapsulated locators and actions for the Search Page
 ┣ 📂 reports
 ┃ ┗ 📜 report.html           # Auto-generated HTML Test Execution Report
 ┣ 📂 screenshots             # Auto-captured screenshots of failed test cases
 ┣ 📂 tests
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 conftest.py           # PyTest fixtures for WebDriver setup, teardown, and custom hooks
 ┃ ┣ 📜 test_login.py         # Login test scenarios (Unittest structure)
 ┃ ┗ 📜 test_search.py        # Product search test scenarios (Unittest structure)
 ┣ 📂 utils
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 config_reader.py      # Utility to parse the config.ini file
 ┃ ┗ 📜 csv_reader.py         # Utility to parse the test_data.csv file
 ┣ 📜 pytest.ini              # PyTest configuration flags and reporting directives
 ┣ 📜 requirements.txt        # Required Python packages and dependencies
 ┗ 📜 README.md               # Project documentation
```

## ⚙️ 4. IMPLEMENTATION DETAILS
The framework integrates several advanced automation concepts:

* **Page Object Model (POM):** UI locators (`By.XPATH`, `By.ID`) and interactions are strictly isolated inside the `pages/` directory. The test files in `tests/` only call high-level methods (e.g., `login_page.login()`), ensuring test scripts are clean and readable.
* **Unittest & PyTest Integration:** The test cases are written using Python's built-in `unittest.TestCase` class for object-oriented structure, while utilizing `pytest` as the test runner to leverage powerful fixtures (`conftest.py`) and plugins.
* **Data-Driven Testing (DDT):** The product search test iterates through `test_data.csv` using a utility reader, testing multiple scenarios (valid products, invalid products) against the exact same script logic.
* **Dynamic Rate-Limit Handling:** To prevent the application from blocking the automated bot due to excessive login attempts, the `test_login.py` script dynamically generates unique, timestamped email addresses at runtime.
* **Event Listeners (Screenshot on Failure):** A custom PyTest hook (`pytest_runtest_makereport`) is implemented in `conftest.py`. It listens for test failures and automatically triggers a Selenium screenshot, saving it to the `screenshots/` folder.

## 🛠️ 5. TOOLS AND TECHNOLOGIES USED
* **Programming Language:** Python 3.10+
* **Automation Tool:** Selenium WebDriver
* **Test Framework:** Unittest (Structure) & PyTest (Execution)
* **Reporting Engine:** `pytest-html`
* **Version Control / IDE:** Visual Studio Code (VS Code)

## 🧪 6. TEST EXECUTION & SCENARIOS
The following critical test scenarios were successfully automated:
1. **TC_01:** Verify the E-Commerce product search functionality with valid existing products (e.g., MacBook, iPhone).
2. **TC_02:** Verify the system behavior and error messaging when searching for an invalid/non-existent product.
3. **TC_03:** Verify user authentication failure when providing incorrect credentials (incorporating dynamic email generation).
4. **TC_04:** Intentional failure test case designed specifically to demonstrate the framework's automated screenshot-capturing capabilities.

### 🚀 Execution Instructions
To execute the test suite and generate the report, open the terminal in the project root directory and run:
```bash
python -m pytest
```
*(Note: `python -m pytest` is utilized to bypass Windows Application Control policies that may block direct `.exe` execution on enterprise/educational devices).*

## 📊 7. RESULTS AND REPORTING
Upon execution, the framework automatically compiles the results into a self-contained HTML report (`reports/report.html`). 
- **Pass/Fail Metrics:** Displays the total execution time, environment details, and clear pass/fail status for every test.
- **Visual Evidence:** For any test that fails, the HTML report automatically embeds the captured browser screenshot directly beneath the error stack trace, drastically reducing debugging time.

## 🏁 8. CONCLUSION
This capstone project successfully demonstrates the creation of a reliable, scalable, and maintainable Test Automation Framework. By combining POM, Data-Driven Testing, and automated HTML reporting, the framework meets modern industry standards for Quality Assurance, proving highly effective for continuous integration and regression testing environments.

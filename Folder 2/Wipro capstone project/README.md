# Selenium Python Automation Framework

This project is a robust Selenium Python Automation Framework built as part of Capstone Assignment 2.

## Framework Features
- **Unittest & PyTest**: Tests are written using the `unittest` structure but executed via `pytest` for advanced features like fixtures, hooks, and plugins.
- **Page Object Model (POM)**: The `pages` directory contains page classes (`base_page.py`, `login_page.py`, `search_page.py`) to separate test logic from UI elements.
- **Utility Classes**: Found in the `utils` directory (`config_reader.py`, `csv_reader.py`).
- **Configuration Management**: The `config.ini` file in the `config` directory stores basic configuration settings like the target URL and browser.
- **Test Data Handling (CSV)**: Test data for scenarios like searching is read from `test_data.csv` in the `data` directory using Python's `csv` module.
- **Screenshots on Failure**: A PyTest hook (`pytest_runtest_makereport` in `tests/conftest.py`) captures screenshots of the browser whenever a test fails. These are saved in the `screenshots` directory.
- **HTML Reporting**: Handled using the `pytest-html` plugin. The test report is generated automatically in the `reports` directory.

## Project Structure
```
d:\Wipro capstone project
|-- config/
|   |-- config.ini
|-- data/
|   |-- test_data.csv
|-- pages/
|   |-- __init__.py
|   |-- base_page.py
|   |-- login_page.py
|   |-- search_page.py
|-- reports/
|-- screenshots/
|-- tests/
|   |-- __init__.py
|   |-- conftest.py
|   |-- test_login.py
|   |-- test_search.py
|-- utils/
|   |-- __init__.py
|   |-- config_reader.py
|   |-- csv_reader.py
|-- pytest.ini
|-- requirements.txt
|-- README.md
```

## Setup and Execution

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests**
   Navigate to the project root directory and run:
   ```bash
   pytest
   ```
   
   PyTest will read the configurations from `pytest.ini` and automatically generate the HTML report in `reports/report.html`.

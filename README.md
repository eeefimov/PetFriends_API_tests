# PetFriends API Testing

## Overview

This repository contains a comprehensive set of test cases and issues for the PetFriends API. 
The API documentation can be found [here](https://petfriends.skillfactory.ru/apidocs/#/).

**API Methods Tested:**
- GET
- POST
- PUT
- DELETE

**Libraries Used:**
- [Allure](https://docs.qameta.io/allure/)
- [Requests](https://docs.python-requests.org/en/latest/)

## Test Cases and Issues

You can find our test cases and track issues in our [Google Sheets document](https://docs.google.com/spreadsheets/d/1Q1qjP4xNNqfmabxxUShZDmxZhvL3y1KzYyW1J2LAIM4/edit?usp=sharing).

## How to Execute Locally

**Prerequisites:**
- Python installed (3.9+ recommended)
- Python package manager (pip)

**Installation:**

1. Clone this repository to your local machine:
2. Navigate to the project directory: cd PetFriends
3. Create a virtual environment (optional but recommended): python -m venv venv
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required packages: pip install -r requirements.txt
6. Navigate to the TESTS directory: cd TESTS
7. Execute the tests: pytest -v
8. Generate allure report:
- pytest --alluredir=allure-results
- allure generate allure-results --clean   
- allure open  

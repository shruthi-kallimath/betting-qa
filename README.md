# Betting QA Tests

## Overview

This repository contains the deliverables for the Sports Betting QA Assessment, including:

* Test Plan
* Test Execution Results & Bug Reports
* QA Strategy & Recommendations
* UI Automation Test
* API Automation Test

The solution demonstrates a risk-based testing approach combining manual testing, API automation, and end-to-end UI automation.

---

## Tech Stack

* Python
* Pytest
* Selenium WebDriver
* Requests
* Allure Reporting

---

## Project Structure

```text
sports-betting-qa/
│
├── api/
├── config/
├── docs/
├── pages/
├── test_data/
├── tests/
│   ├── api/
│   └── ui/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Framework Components

### API Layer

**api/api_client.py**

* Generic HTTP client responsible for GET and POST requests.
* Centralizes request handling and headers.

**api/betting_api.py**

* Business-level API operations.
* Retrieves matches, places bets, and resets balance.
* Keeps test logic separate from API implementation details.

### Page Objects

**pages/base_page.py**

* Common Selenium utilities.
* Navigation, waits, element interactions, and value parsing.

**pages/betting_home_page.py**

* Home page interactions.
* Match selection, odds selection, balance retrieval, and page refresh.

**pages/bet_slip_page.py**

* Bet slip interactions.
* Stake entry, payout retrieval, bet placement, and empty state validation.

**pages/receipt_modal.py**

* Receipt validation.
* Verifies bet details, payout, timestamp, and modal interactions.

### Test Data

**test_data/bet_data.py**

* Centralized test data.
* Stake validation boundary inputs and reusable constants.

### Tests

**tests/ui/test_single_bet_placement.py**

* End-to-end UI automation.
* Validates successful bet placement, payout calculation, receipt generation, and balance updates.

**tests/api/test_stake_validation.py**

* API automation.
* Validates stake boundary rules using parameterized test data.

### Configuration

**config/config.ini**

* Application and browser configuration.

**config/config_reader.py**

* Utility for reading configuration values.

**conftest.py**

* Shared pytest fixtures for browser setup, API setup, and configuration management.

---

## Framework Highlights

* Page Object Model (POM) design for UI automation.
* Centralized configuration management.
* Reusable API client layer.
* Separation of test data from test logic.
* Pytest fixtures for setup and teardown.
* Parameterized API testing for boundary validation.
* Detailed execution logging for test execution visibility.
* Allure reporting.
* End-to-end validation across UI and API layers.
* Maintainable and scalable project structure.

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shruthi-kallimath/sports-betting-qa.git
cd sports-betting-qa
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

### Run All Tests

```bash
pytest -v
```

### Run UI Tests

```bash
pytest tests/ui -v
```

### Run API Tests

```bash
pytest tests/api -v
```

---

## Run UI Test with Detailed Execution Logs

The UI automation test includes detailed logging to provide visibility into the execution flow, selected match, stake value, payout calculations, receipt validation, and balance updates.

```bash
pytest tests/ui/test_single_bet_placement.py -v -s --log-cli-level=INFO
```

---

## Allure Reporting

### Generate Allure Results for UI Test

```bash
pytest tests/ui/test_single_bet_placement.py --alluredir=allure_results
```

### Generate Allure Results for API Test

```bash
pytest tests/api/test_stake_validation.py --alluredir=allure_results
```

### Open Allure Report

```bash
allure serve allure_results
```

---

## Deliverables

| Document                        | Location                               |
| ------------------------------- | -------------------------------------- |
| Test Plan                       | docs/test_plan.md                      |
| Execution Results & Bug Reports | docs/execution_results.md              |
| Strategy & Recommendations      | docs/strategies_and_recommendations.md |

---

## Automated Test Coverage

### UI Automation

**Successful Single Bet Placement**

Coverage:

* Match selection
* Odds selection
* Stake entry
* Payout calculation
* Bet placement
* Receipt validation
* Balance update validation
* Bet slip reset validation

### API Automation

**Stake Validation Boundary Testing**

Coverage:

* Minimum stake boundary
* Maximum stake boundary
* Invalid stake values
* Decimal precision validation
* Positive and negative scenarios

---

## Author

**Shruthi Kallimath**

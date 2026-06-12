## Selection of 2 Tests for Automation Over Other Candidates

Selection of the automated tests was based on risk, repeatability, business impact, and suitability for regression testing.

### TC-01: Successful Single Bet Placement - Automated UI Test

This scenario was selected for UI automation because:

It validates the most critical end-to-end user journey in the application.
It validates integration between the frontend and backend systems.
It is a stable and repeatable scenario, making it highly suitable for regression testing.
A failure in this flow would prevent users from placing a bet in the application.


### TC-02: Stake Validation - Automated API Test

This scenario was selected for API automation because:

* It validates a critical business rule that directly impacts bet placement.
* Stake validation has clearly defined boundaries, making it the best candidate for regression testing.
* Failures in stake validation can result in wrong calculations, invalid bets, and potential business losses.

### Why Other Scenarios Were Not Automated

The remaining scenarios were intentionally kept as manual tests because:

* These scenarios required exploratory testing to understand application behavior and identify potential defects.
* They involved UI interactions and visual checks that are more effective when tested manually.
* Given the limited timeframe, automation was focused on the highest-priority and most repeatable scenarios.

Key considerations include:

* Past Match Betting Validation (TC-03) and Insufficient Balance (TC-04)  were tested manually to validate business rules and understand system behavior. Both scenarios revealed critical defects and should be added to the automated regression suite once the issues are fixed.

* Selection Replacement (TC-05) was kept manual because it involves dynamic UI behavior and bet slip updates that are best verified through user interaction.

* Error Modal Retry & Close Behavior (TC-06) was kept manual because it requires validation of error messages, modal interactions, and overall user experience.


### Top Recommendations if the Project Were to Scale

#### 1. Integrate Automated Tests into CI/CD

* Run API tests automatically on every pull request to catch issues early.
* Execute critical UI regression tests before deployment.
* Block deployments when critical business rules fail.
* Generate and publish test reports automatically.
* Keep UI automation focused on key user journeys for fast and reliable execution.

#### 2. Expand API and Business Rule Test Coverage

* Add automated API tests for critical betting and financial validations, including stake limits, balance checks, invalid inputs, and completed matches.
* Ensure the API rejects all invalid bets, even when UI validations are bypassed.
* Use API tests as the primary regression layer for business rules because they are fast, reliable, and easy to maintain.

#### 3.Test Data Strategy and Specification Clarity

* Use reliable test data setup and cleanup to keep tests independent and repeatable.
* Reset key data before each test to ensure consistent results.
* Clearly define business rules and expected API responses so developers, testers, and automation scripts validate the same behavior.

#### 4. Maintain a Scalable Automation Framework

* Continue using the Page Object Model (POM) design to centralize UI locators and page actions.
* This reduces maintenance effort, avoids code duplication, and makes it easier to add new test scenarios in the future.





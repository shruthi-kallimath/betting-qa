# Test Plan

This test plan covers the Single Bet Placement feature for a desktop web application.  
The scenarios are prioritized on risk-based testing and to include positive, negative, boundary, business rule, UI, and API validation coverage.

---

## TC-01: Successful Single Bet Placement

**Type**     : Automated E2E UI Test  
**Severity** : Critical  
**Coverage** : Positive

### Risk Rationale

This is the main core functionality of the application. If a user cannot successfully place a valid single bet, the main revenue-generating functionality fails.  
This scenario also validates UI-to-backend integration, payout calculation, balance update, and receipt generation.

### Steps

1. Launch the desktop web application.
2. Verify that upcoming football matches are displayed.
3. Select one valid odds button for a match, for example Home win.
4. Verify that the selected match and outcome appear in the bet slip.
5. Enter a valid stake, for example '10.00'.
6. Verify that the potential payout is calculated as 'stake × odds'.
7. Click on Place Bet button.
8. Verify that the button changes to "Placing..." while the request is in progress.
9. Wait for the success receipt modal to appear.
10. Close the receipt modal.

### Expected Result

1. The selected bet is submitted successfully.
2. The stake amount is deducted from the available balance.
3. A success receipt modal is displayed.
4. Receipt shows:
   a. Bet ID  
   b. Match details  
   c. Selection  
   d. Stake  
   e. Odds at placement  
   f. Potential payout  
   g. Placement timestamp
5. Closing the receipt returns the user to the main flow.
6. No active selection remains in the bet slip.

---

## TC-02: Stake Validation

**Type**     : Automated API  
**Severity** : Critical  
**Coverage** : Negative + Boundary

### Risk Rationale

Incorrect validation may allow users to place bets with invalid amounts, exceed business limits, bypass decimal precision rules, or cause balance/payout calculation defects.  
API automation on stake feature is suitable because these checks are deterministic, fast, and provide high regression value.

### Test Data

| Stake | Expected Result |
|---------|----------------|
| 0.99 | Reject |
| 1.00 | Accept |
| 1.01 | Accept |
| 100.00 | Accept |
| 100.01 | Reject |
| 10.999 | Reject |

### Steps

1. Send a request to fetch available matches GET:/api/matches.
2. Extract the first available match id from above api response body.
3. Send POST:/api/place-bet with a valid 'x-user-id' header. Within the request body, set match id as extracted above, set selection parameter as "HOME", set the first stake from above test data and execute the request.
4. Repeat the request using each stake value from the test data table.
5. Verify the response status and response body for each stake value.

### Expected Result

1. Stake below the minimum allowed value is rejected.
2. Stake at the minimum boundary is accepted.
3. Stake slightly above minimum is accepted.
4. Stake at the maximum boundary is accepted.
5. Stake above the maximum value is rejected.
6. Stake with more than 2 decimal places is rejected.
7. Rejected requests return appropriate validation errors.
8. Accepted requests return successful placement response with correct stake, odds, payout, balance, and currency.

---

## TC-03: Allow placing bets only for Pre/Upcoming matches and reject bets on Past matches.

**Type**     : Manual  
**Severity** : Critical  
**Coverage** : Positive

### Risk Rationale

This test case directly impacts the core functionality of the web application. If the user is allowed to place a bet on the past match,  
then this leads to violation of one of the business rules and involves financial risk for the business.

### Steps

1. Open the web application.
2. Select a valid odds button for a past match.
3. Enter a valid stake.
4. Click on Place Bet.
5. Observe the result.
6. Try to place a bet on selecting a match with upcoming date.
7. Observe the result.

### Expected Result

Web application should not allow placing a bet on a past match. It should display error message that the bet cannot be placed on a past match.  
web application should allow users to place bet on the upcoming matches successfully.

---

## TC-04: Insufficient Balance

**Type**     : Manual  
**Severity** : Critical  
**Coverage** : Negative

### Risk Rationale

The system must prevent users from placing bets greater than their available balance since its directly affects the revenue/financial integrity of the business.

### Steps

1. Open the web application.
2. Start with base balance of 120 Euros. Verify this in balance header or in bet slip.
3. Select a valid odds button from any upcoming football match.
4. Enter the maximum stake 100 Euros.
5. Click on Place Bet button.
6. After seeing the successful bet placement message, refresh the page and verify remaining balance to be shown as 20 Euros in the balance header or bet slip.
7. Select a valid odds button from any upcoming football match and try to place another bet of 50 Euros.

### Expected Result

1. Bet placement is blocked.
2. User sees the error message: Insufficient balance.
3. No bet is placed.
4. No success receipt is shown.
5. User balance remains unchanged.

---

## TC-05: Selection Replacement

**Type**     : Manual  
**Severity** : High  
**Coverage** : Positive/Business Rule

### Risk Rationale

The feature supports single bets only. If multiple bet selections are allowed at once, then this violates the main business rule of only placing single bets.

### Steps

1. Open the web application.
2. Select one odds button from an upcoming match.
3. Verify that the selected outcome appears in the bet slip.
4. Select a different odds button from another match.
5. Observe the bet slip.
6. Select another odds button from the same match.
7. Observe the bet slip again.

### Expected Result

1. New odds selection replaces the previous selection.
2. Bet slip displays only the latest selected match and outcome.
3. No multi-bets get placed.

---

## TC-06: Error Modal Retry and Close Behavior

**Type**     : Manual  
**Severity** : High  
**Coverage** : Negative/Error Handling

### Risk Rationale

Bet placement failures must be handled safely and clearly with user-friendly messages. Users upon checks should be able to understand that the bet was not processed, and retry/close behavior must not create duplicate bets or deduct stake multiple times.

### Steps

1. Open the web application.
2. Select a valid odds button for an upcoming match.
3. Enter a valid stake.
4. Trigger or simulate a placement failure by turning off the internet connection.
5. Click on Place Bet button.
6. Verify that an error modal appears.
7. Click on Rebet button.
8. Verify that the system retries placement.
9. Trigger the failure again.
10. Click on Close button.

### Expected Result

1. Error modal title displays an error message.
2. Clicking on Rebet button closes the modal and retries the placement.
3. Clicking on Close button closes the modal and clears current selection/stake.
4. No duplicate bet is created during retry.

---
# Execution Results / Bug Reports

## BUG-01: Application is failing to reject the bet for the past matches.

**Severity:** Critical

### Reproduction Steps

1. Open the web application.
2. Select Date/Date Range from the past dates.
3. Select Odds: All or within a range 1 to 100.
4. From the list of Past Matches, Select one match and click on one of the ODDS 1/X/2.
5. Verify the Bet slip for the Selected Match.
6. Enter your desired stake value in the range 1 to 100 Euros.
7. Click on Place Bet Button.
8. Observe the Result.

### Expected Result

User should not be allowed to place a bet successfully.

### Actual Result

Place Bet Button leads to a receipt modal displaying the successful placement of the bet with Bet details like bet id, match details, stake and potential payout.

### Business Impact

Users can successfully place bets on matches that have already completed thereby resulting in potential financial loss, loss of platform credibility, violation of core betting regulations and business rules.

---

## BUG-02: Place Bet API accepts the bet when balance is insufficient.

**Severity:** Critical

### Reproduction Steps

1. Make a Post request to the API endpoint: `/api/reset-balance` to reset the balance to 125.5 EUR.
2. Make a Get request to the API endpoint: `/api/matches` to get the list of matches. Pick a match id for an upcoming match from the list.
3. Make a Post request to the API endpoint: `/api/place-bet` to place a bet. Provide matchId from previous step, provide selection as "HOME" and provide stake as 100.00.
4. Make a Get request to the API endpoint: `/api/balance` to get the balance after placing the bet of 100.00 EUR. Remaining balance should reflect as 25.5 EUR in response body of the API.
5. Repeat step 3.
6. Observe the result.

### Expected Result

API should throw an error code in the response body "insufficient_balance" with http status code 405.

### Actual Result

API provides a HTTP status 200 with successful bet placement message in response body with negative balance.

### Business Impact

Users can continue placing bets with insufficient funds, resulting in negative account balances. This leads to financial loss and loss of platform credibility.

---

## BUG-03: Place Bet API accepts negative stake values and increases account balance.

**Severity:** Critical

### Reproduction Steps

1. Make a POST request to the API endpoint: `/api/reset-balance` to reset the balance to 125.5 EUR.
2. Make a GET request to the API endpoint: `/api/matches` to retrieve the list of matches. Pick a matchId for any upcoming match.
3. Make a POST request to the API endpoint: `/api/place-bet`.
4. Provide the matchId from the previous step, selection as "HOME", and stake as -150.00.
5. Observe the response.
6. Make a GET request to the API endpoint: `/api/balance`.
7. Observe the updated balance.

### Expected Result

Place Bet API should reject negative stake values with an appropriate validation error message and HTTP error status code.

### Actual Result

API accepts the negative stake value, returns HTTP status 200 with successful bet placement response, and increases the user's balance from 120 EUR to 270 EUR.

### Business Impact

Users can increase their account balance by placing bets with negative stake values through the API, leading to financial fraud, incorrect account balances. This results in loss to the business.
```

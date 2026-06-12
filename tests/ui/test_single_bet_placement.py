from decimal import Decimal
import allure
import logging
import pytest
from test_data.bet_data import VALID_SELECTION, VALID_STAKE
from pages.betting_home_page import BettingHomePage
from pages.bet_slip_page import BetSlipPage
from pages.receipt_modal import ReceiptModal


logger = logging.getLogger(__name__)


@pytest.mark.ui
@pytest.mark.e2e
def test_successful_single_bet_placement(driver, app_url, betting_api):
    """
    Chosen for automation because it validates the critical end to end 
    user journey. This test verifies UI interactions, payout
    calculation, receipt generation, and balance updates across both ui and api integrated layers.
    """

    home_page = BettingHomePage(driver)
    bet_slip = BetSlipPage(driver)
    receipt = ReceiptModal(driver)

    response = betting_api.reset_balance()

    assert response.status_code == 200, (
        f"Balance reset failed. Status code: {response.status_code}"
    )

    stake = VALID_STAKE
    selection = VALID_SELECTION

    logger.info("Opening betting application")
    home_page.open(app_url)

    assert home_page.matches_are_displayed(), "Expected upcoming matches to be displayed"

    initial_balance = home_page.get_header_balance()
    logger.info(f"Initial balance: {initial_balance}")

    match_name, selected_odds = home_page.select_upcoming_match_odds(selection)

    logger.info(f"Selected Upcoming Match: {match_name}")
    logger.info(f"Selected odds: {selected_odds}")

    assert bet_slip.get_selected_match_name() == match_name, (
        f"Expected bet slip match to be {match_name}, "
        f"but got {bet_slip.get_selected_match_name()}"
    )

    assert bet_slip.get_selected_odds() == selected_odds, (
        f"Expected selected odds to be {selected_odds}, "
        f"but got {bet_slip.get_selected_odds()}"
    )

    
    bet_slip.enter_stake(stake)
    logger.info(f"Entered Stake: {stake}")

    expected_payout = (stake * selected_odds).quantize(Decimal("0.01"))
    bet_slip_payout = bet_slip.get_potential_payout()

    logger.info(f"Expected Payout Calculated : {expected_payout}")
    logger.info(f"Bet slip payout: {bet_slip_payout}")

    assert bet_slip_payout == expected_payout, (
        f"Expected bet slip payout to be {expected_payout}, "
        f"but got {bet_slip_payout}"
    )

    logger.info("Placing bet")
    bet_slip.place_bet()

    assert receipt.is_receipt_visible(), "Expected success receipt modal to be visible"
    logger.info("Receipt modal is visible")
    
    assert receipt.get_bet_id() != "", "Expected Bet ID to be displayed"
    logger.info("Bet-ID is visible")


    assert receipt.get_stake() == stake, (
        f"Expected receipt stake to be {stake}, "
        f"but got {receipt.get_stake()}"
    )

    assert receipt.get_odds() == selected_odds, (
        f"Expected receipt odds to match selected {selection} odds {selected_odds}, "
        f"but got {receipt.get_odds()}"
    )

    receipt_payout = receipt.get_payout()
    logger.info(f"Receipt payout: {receipt_payout}")
    bug_messages = []

    if receipt_payout != bet_slip_payout:
        allure.attach(
            driver.get_screenshot_as_png(),
            name = "Receipt Payout Mismatch",
            attachment_type = allure.attachment_type.PNG
    )

        bug_messages.append(
        f"BUG-01: Receipt payout does not match bet slip payout. "
        f"Expected receipt payout: {bet_slip_payout}, "
        f"Actual receipt payout: {receipt_payout}"
    )

    assert receipt.get_timestamp() != "", "Expected placement timestamp to be displayed"

    logger.info("Closing Receipt")
    receipt.close()

    logger.info("Refreshing Home Page")
    home_page.refresh()

    expected_balance = initial_balance - stake
    logger.info(f"Expected balance: {expected_balance}")

    home_page.wait_for_header_balance_to_be(expected_balance)

    actual_balance = home_page.get_header_balance()
    logger.info(f"Actual balance: {actual_balance}")

    assert actual_balance == expected_balance, (
    f"Expected balance to be {expected_balance}, "
    f"but got {actual_balance}"
    )

    assert bet_slip.is_empty(), "Expected bet slip to be empty after successful placement"

    assert not bug_messages, "\n".join(bug_messages)

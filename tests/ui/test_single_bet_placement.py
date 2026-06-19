from decimal import Decimal

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.betting_home_page import BettingHomePage
from pages.bet_slip_page import BetSlipPage
from pages.receipt_modal import ReceiptModal
from services.betting_service import BettingService
from test_data.bet_data import VALID_SELECTION, VALID_STAKE
from utils.bet_calculator import BettingCalculator
from validators.receipt_validator import ReceiptValidator

@allure.feature("Bet Placement")
@allure.story("Single Bet Placement")
@pytest.mark.ui
@pytest.mark.e2e
def test_successful_single_bet_placement(
    driver: WebDriver,
    app_url: str,
    betting_service: BettingService,
) -> None:

    home_page = BettingHomePage(driver)
    bet_slip = BetSlipPage(driver)
    receipt = ReceiptModal(driver)

    with allure.step("Reset user balance"):
        betting_service.reset_balance()

    with allure.step("Open betting application"):
        home_page.open(app_url)
        assert home_page.matches_are_displayed()

    with allure.step("Capture initial balance"):
        initial_balance: Decimal = home_page.get_header_balance()

    with allure.step("Select an upcoming match"):
        selected_match = home_page.select_upcoming_match_odds(
            selection=VALID_SELECTION
        )

        assert bet_slip.get_selected_match_name() == selected_match.match_name
        assert bet_slip.get_selected_odds() == selected_match.odds

    with allure.step("Enter stake and verify payout"):
        bet_slip.enter_stake(VALID_STAKE)

        expected_payout = BettingCalculator.calculate_payout(
            VALID_STAKE,
            selected_match.odds,
        )

        assert bet_slip.get_potential_payout() == expected_payout

    with allure.step("Place bet"):
        bet_slip.place_bet()

    with allure.step("Verify receipt"):
        ReceiptValidator.verify_successful_receipt(
            receipt=receipt,
            expected_stake=VALID_STAKE,
            expected_odds=selected_match.odds,
            expected_payout=expected_payout,
        )

    with allure.step("Verify updated balance"):
        receipt.close()

        home_page.refresh()

        expected_balance = initial_balance - VALID_STAKE

        home_page.wait_for_header_balance_to_be(expected_balance)

        assert home_page.get_header_balance() == expected_balance
        assert bet_slip.is_empty()
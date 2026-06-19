from decimal import Decimal

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BetSlipPage(BasePage):
    SELECTED_MATCH = (By.CLASS_NAME, "betSelectionTeams")
    SELECTED_ODDS = (By.CLASS_NAME, "betSelectionOdds")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    POTENTIAL_PAYOUT = (By.ID, "bet-slip-potential-payout")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")
    EMPTY_BET_SLIP = (By.CLASS_NAME, "betSlipBodyEmpty")

    @allure.step("Get selected match name from bet slip")
    def get_selected_match_name(self) -> str:
        return self.get_text(self.SELECTED_MATCH)

    @allure.step("Get selected odds from bet slip")
    def get_selected_odds(self) -> Decimal:
        odds_text = self.get_text(self.SELECTED_ODDS)
        return self.parse_decimal(odds_text)

    @allure.step("Enter stake amount: {stake}")
    def enter_stake(self, stake: Decimal) -> None:
        self.type_text(self.STAKE_INPUT, str(stake))

    @allure.step("Get potential payout from bet slip")
    def get_potential_payout(self) -> Decimal:
        payout_text = self.get_text(self.POTENTIAL_PAYOUT)
        return self.parse_money(payout_text)

    @allure.step("Place bet")
    def place_bet(self) -> None:
        self.click(self.PLACE_BET_BUTTON)

    @allure.step("Check if bet slip is empty")
    def is_empty(self) -> bool:
        return self.is_visible(self.EMPTY_BET_SLIP)
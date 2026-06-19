from decimal import Decimal

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ReceiptModal(BasePage):
    MODAL = (
        By.XPATH,
        "//h2[normalize-space()='Bet Placed Successfully!']"
        "/ancestor::div[contains(@class,'modalBody')]",
    )

    BET_ID = (By.ID, "modal-success-bet-id")
    MATCH = (By.ID, "modal-success-match")
    STAKE = (By.ID, "modal-success-stake")
    ODDS = (By.ID, "modal-success-odds")
    PAYOUT = (By.ID, "modal-success-payout")
    TIMESTAMP = (By.ID, "modal-success-placed-at")
    CLOSE_BUTTON = (By.ID, "modal-success-close")

    @allure.step("Get bet ID from receipt")
    def get_bet_id(self) -> str:
        return self.get_text(self.BET_ID)

    @allure.step("Get match name from receipt")
    def get_match_name(self) -> str:
        return self.get_text(self.MATCH)

    @allure.step("Get stake from receipt")
    def get_stake(self) -> Decimal:
        return self.parse_money(self.get_text(self.STAKE))

    @allure.step("Get odds from receipt")
    def get_odds(self) -> Decimal:
        return self.parse_decimal(self.get_text(self.ODDS))

    @allure.step("Get payout from receipt")
    def get_payout(self) -> Decimal:
        return self.parse_money(self.get_text(self.PAYOUT))

    @allure.step("Get timestamp from receipt")
    def get_timestamp(self) -> str:
        return self.get_text(self.TIMESTAMP)

    @allure.step("Verify receipt modal is visible")
    def is_receipt_visible(self) -> bool:
        return self.is_visible(self.MODAL)

    @allure.step("Close receipt modal")
    def close(self) -> None:
        self.click(self.CLOSE_BUTTON)
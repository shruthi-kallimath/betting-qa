from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ReceiptModal(BasePage):
    MODAL = (
        By.XPATH,
        "//h2[normalize-space()='Bet Placed Successfully!']/ancestor::div[contains(@class,'modalBody')]"
    )

    BET_ID = (By.ID, "modal-success-bet-id")
    MATCH = (By.ID, "modal-success-match")
    STAKE = (By.ID, "modal-success-stake")
    ODDS = (By.ID, "modal-success-odds")
    PAYOUT = (By.ID, "modal-success-payout")
    TIMESTAMP = (By.ID, "modal-success-placed-at")
    CLOSE_BUTTON = (By.ID, "modal-success-close")


    def get_bet_id(self):
        return self.get_text(self.BET_ID)

    def get_match_name(self):
        return self.get_text(self.MATCH)

    def get_stake(self):
        return self.parse_money(self.get_text(self.STAKE))

    def get_odds(self):
        return self.parse_decimal(self.get_text(self.ODDS))

    def get_payout(self):
        return self.parse_money(self.get_text(self.PAYOUT))

    def get_timestamp(self):
        return self.get_text(self.TIMESTAMP)
    
    def is_receipt_visible(self):
        visible = self.is_visible(self.MODAL)
        self.pause_for_demo()
        return visible

    def close(self):
        self.click(self.CLOSE_BUTTON)
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BetSlipPage(BasePage):
    
    SELECTED_MATCH = (By.CLASS_NAME, "betSelectionTeams")
    SELECTED_ODDS = (By.CLASS_NAME,"betSelectionOdds")
    STAKE_INPUT = (By.ID,"bet-slip-stake-input")
    POTENTIAL_PAYOUT = (By.ID,"bet-slip-potential-payout")
    PLACE_BET_BUTTON = (By.ID,"bet-slip-place-bet")
    EMPTY_BET_SLIP = (By.CLASS_NAME,"betSlipBodyEmpty")

  

    def get_selected_match_name(self):
        return self.get_text(self.SELECTED_MATCH)

    def get_selected_odds(self):
        odds_text = self.get_text(self.SELECTED_ODDS)
        return self.parse_decimal(odds_text)

    def enter_stake(self, stake):
        self.type_text(self.STAKE_INPUT, stake)

    def get_potential_payout(self):
        payout_text = self.get_text(self.POTENTIAL_PAYOUT)
        return self.parse_money(payout_text)

    def place_bet(self):
        self.click(self.PLACE_BET_BUTTON)

    def is_empty(self):
        return self.is_visible(self.EMPTY_BET_SLIP)
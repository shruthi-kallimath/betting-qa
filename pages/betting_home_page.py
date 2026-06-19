from decimal import Decimal
from typing import NamedTuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MatchSelection(NamedTuple):
    match_name: str
    odds: Decimal


class BettingHomePage(BasePage):
    MATCH_CARDS = (By.CSS_SELECTOR, "[id^='match-card-']")
    HEADER_BALANCE = (By.ID, "header-balance")

    def open(self, app_url: str) -> None:
        self.open_url(app_url)

    def refresh(self) -> None:
        self.refresh_page()

    def matches_are_displayed(self) -> bool:
        return len(self.finds(self.MATCH_CARDS)) > 0

    def wait_for_header_balance_to_be(self, expected_balance: Decimal) -> None:
        self.wait.until(
            lambda _: self.get_header_balance() == expected_balance
        )

    def get_header_balance(self) -> Decimal:
        balance_text = self.get_text(self.HEADER_BALANCE)
        return self.parse_money(balance_text)

    def get_first_upcoming_match(self) -> WebElement:
        match_cards = self.finds(self.MATCH_CARDS)

        for card in match_cards:
            badge_text = card.find_element(
                By.CLASS_NAME,
                "badge",
            ).text.strip().upper()

            if badge_text == "UPCOMING":
                return card

        raise ValueError("No upcoming match found on betting home page.")

    def get_upcoming_match_name(self) -> str:
        upcoming_match = self.get_first_upcoming_match()
        return self._get_match_name(upcoming_match)

    def select_upcoming_match_odds(self, selection: str) -> MatchSelection:
        upcoming_match = self.get_first_upcoming_match()

        match_name = self._get_match_name(upcoming_match)

        odds_button = upcoming_match.find_element(
            By.CSS_SELECTOR,
            f"[id$='-{selection.lower()}']",
        )

        odds_value = odds_button.find_element(
            By.CLASS_NAME,
            "oddsButtonValue",
        ).text

        odds = self.parse_decimal(odds_value)

        odds_button.click()

        return MatchSelection(
            match_name=match_name,
            odds=odds,
        )

    def _get_match_name(self, match_card: WebElement) -> str:
        teams = match_card.find_elements(
            By.CLASS_NAME,
            "teamName",
        )

        if len(teams) < 2:
            raise ValueError("Expected at least two teams in match card.")

        return f"{teams[0].text} vs {teams[1].text}"
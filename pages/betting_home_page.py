from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BettingHomePage(BasePage):
    MATCH_CARDS = (By.CSS_SELECTOR, "[id^='match-card-']")
    HEADER_BALANCE = (By.ID, "header-balance")

    def open(self, app_url):
        self.open_url(app_url)

    def refresh(self):
        self.refresh_page()

    def matches_are_displayed(self):
        return len(self.finds(self.MATCH_CARDS)) > 0
    
    def wait_for_header_balance_to_be(self, expected_balance):
        self.wait.until(
            lambda driver: self.get_header_balance() == expected_balance
    )

    def get_header_balance(self):
        balance_text = self.get_text(self.HEADER_BALANCE)
        return self.parse_money(balance_text)

    def get_first_upcoming_match(self):
        match_cards = self.finds(self.MATCH_CARDS)

        for card in match_cards:
            badge_text = card.find_element(
                By.CLASS_NAME, "badge"
            ).text.strip().upper()

            if badge_text == "UPCOMING":
                return card

        raise Exception("No upcoming match found")

    def get_upcoming_match_name(self):
        upcoming_match = self.get_first_upcoming_match()

        teams = upcoming_match.find_elements(
            By.CLASS_NAME, "teamName"
        )

        return f"{teams[0].text} vs {teams[1].text}"

    def select_upcoming_match_odds(self, selection):
        upcoming_match = self.get_first_upcoming_match()

        teams = upcoming_match.find_elements(
            By.CLASS_NAME, "teamName"
        )
        match_name = f"{teams[0].text} vs {teams[1].text}"

        odds_button = upcoming_match.find_element(
            By.CSS_SELECTOR,
            f"[id$='-{selection.lower()}']"
        )

        odds_value = odds_button.find_element(
            By.CLASS_NAME, "oddsButtonValue"
        ).text

        odds = self.parse_decimal(odds_value)

        odds_button.click()

        return match_name, odds
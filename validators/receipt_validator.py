from decimal import Decimal

import allure

from pages.receipt_modal import ReceiptModal


class ReceiptValidator:

    @staticmethod
    @allure.step("Verify successful bet receipt")
    def verify_successful_receipt(
        receipt: ReceiptModal,
        expected_stake: Decimal,
        expected_odds: Decimal,
        expected_payout: Decimal,
    ) -> None:

        assert receipt.is_receipt_visible(), (
            "Expected receipt modal to be visible."
        )

        assert receipt.get_bet_id(), (
            "Expected Bet ID to be displayed."
        )

        assert receipt.get_timestamp(), (
            "Expected placement timestamp to be displayed."
        )

        actual_stake = receipt.get_stake()
        actual_odds = receipt.get_odds()
        actual_payout = receipt.get_payout()

        assert actual_stake == expected_stake, (
            f"Expected stake {expected_stake}, "
            f"but found {actual_stake}."
        )

        assert actual_odds == expected_odds, (
            f"Expected odds {expected_odds}, "
            f"but found {actual_odds}."
        )

        assert actual_payout == expected_payout, (
            f"Expected payout {expected_payout}, "
            f"but found {actual_payout}."
        )
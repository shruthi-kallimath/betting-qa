from decimal import Decimal


class BettingCalculator:

    @staticmethod
    def calculate_payout(
        stake: Decimal,
        odds: Decimal,
    ) -> Decimal:
        return (stake * odds).quantize(Decimal("0.01"))
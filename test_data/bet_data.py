from decimal import Decimal


VALID_SELECTION = "HOME"
VALID_STAKE = Decimal("10.00")

STAKE_VALIDATION_DATA = [
    (0.99, 422),
    (1.00, 200),
    (100.00, 200),
    (100.01, 422),
    (150.00, 422),
    (10.999, 422),
    (1000.00, 422)
    
]



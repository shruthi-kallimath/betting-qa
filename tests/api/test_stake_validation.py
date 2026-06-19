import allure
import pytest
from requests import Response

from services.betting_service import BettingService
from test_data.bet_data import STAKE_VALIDATION_DATA
from validators.api_response_validator import ApiResponseValidator


@pytest.mark.api
@allure.feature("Bet Placement")
@allure.story("Stake Validation")
@pytest.mark.parametrize("stake, expected_status", STAKE_VALIDATION_DATA)
def test_stake_validation_boundaries(
    betting_service: BettingService,
    stake: int,
    expected_status: int,
) -> None:
    with allure.step("Get first available match"):
        match_id: int = betting_service.get_first_match_id()

    with allure.step(f"Place bet with stake: {stake}"):
        response: Response = betting_service.place_bet_raw(
            match_id=match_id,
            selection="HOME",
            stake=stake,
        )

    with allure.step("Verify API response status code"):
        ApiResponseValidator.verify_status_code(
            response=response,
            expected_status_code=expected_status,
        )
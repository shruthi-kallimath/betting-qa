import pytest

from test_data.bet_data import STAKE_VALIDATION_DATA

@pytest.mark.api
@pytest.mark.parametrize("stake, expected_status", STAKE_VALIDATION_DATA)
def test_stake_validation_boundaries(betting_api, stake, expected_status):

    """
    Chosen for automation as stake validation is a stable business rule
    with clear positive, negative, and boundary conditions. API testing provides
    fast execution and reliable validation of user inputs and constraints.
    """

    match_id = betting_api.get_first_match_id()

    response = betting_api.place_bet(
        match_id=match_id,
        selection="HOME",
        stake=stake
    )

    assert response.status_code == expected_status
    
    


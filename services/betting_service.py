from requests import Response


class BettingService:
    def __init__(self, api_client) -> None:
        self.api_client = api_client

    def get_matches(self) -> Response:
        return self.api_client.get("/matches")

    def place_bet(
        self,
        match_id: int,
        selection: str,
        stake: float,
    ) -> Response:
        payload = {
            "matchId": match_id,
            "selection": selection,
            "stake": stake,
        }

        return self.api_client.post(
            "/place-bet",
            payload=payload,
        )

    def get_first_match_id(self) -> int:
        response = self.get_matches()
        response.raise_for_status()

        matches = response.json()

        if not matches:
            raise ValueError("No matches returned from API.")

        return matches[0]["id"]

    def reset_balance(self) -> Response:
        return self.api_client.post("/reset-balance")
    
    


    def place_bet_raw(self,
        match_id: int,
        selection: str,
        stake: int | float,
        ) -> Response:
        payload = {
        "matchId": match_id,
        "selection": selection,
        "stake": stake,
    }

        return self.api_client.post(
        "/place-bet",
        payload=payload,
    )
class BettingApi:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_matches(self):
        return self.api_client.get("/matches")

    def place_bet(self, match_id, selection, stake):
        payload = {
            "matchId": match_id,
            "selection": selection,
            "stake": stake
        }

        return self.api_client.post("/place-bet", json=payload)

    def get_first_match_id(self):
        response = self.get_matches()
        response.raise_for_status()

        matches = response.json()
        return matches[0]["id"]
    
    def reset_balance(self):
        return self.api_client.post(
            "/reset-balance"
        )
import requests


class ApiClient:
    def __init__(self, base_url, user_id):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "x-user-id": user_id,
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = self._build_url(endpoint)
        return requests.get(url, headers=self.headers)

    def post(self, endpoint, json=None):
        url = self._build_url(endpoint)
        return requests.post(url, headers=self.headers, json=json)

    def _build_url(self, endpoint):
        endpoint = endpoint.lstrip("/")
        return f"{self.base_url}/{endpoint}"
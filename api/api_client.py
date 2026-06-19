from typing import Any

import requests
from requests import Response, Session


class ApiClient:
    def __init__(self, base_url: str, user_id: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session: Session = requests.Session()
        self.session.headers.update(
            {
                "x-user-id": user_id,
                "Content-Type": "application/json",
            }
        )

    def get(self, endpoint: str) -> Response:
        url = self._build_url(endpoint)
        return self.session.get(url)

    def post(self, endpoint: str, payload: dict[str, Any] | None = None) -> Response:
        url = self._build_url(endpoint)
        return self.session.post(url, json=payload)

    def _build_url(self, endpoint: str) -> str:
        endpoint = endpoint.lstrip("/")
        return f"{self.base_url}/{endpoint}"
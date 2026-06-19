from requests import Response


class ApiResponseValidator:
    @staticmethod
    def verify_status_code(
        response: Response,
        expected_status_code: int,
    ) -> None:
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, "
            f"but got {response.status_code}. "
            f"Response body: {response.text}"
        )
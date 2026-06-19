import pytest
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.api_client import ApiClient
from config.config_reader import ConfigReader
from api.api_client import ApiClient
from services.betting_service import BettingService


@pytest.fixture(scope="session")
def config() -> ConfigReader:
    return ConfigReader()


@pytest.fixture(scope="session")
def base_url(config: ConfigReader) -> str:
    return config.get("app", "base_url")


@pytest.fixture(scope="session")
def user_id(config: ConfigReader) -> str:
    return config.get("app", "user_id")


@pytest.fixture(scope="session")
def app_url(base_url: str, user_id: str) -> str:
    return f"{base_url}/?user-id={user_id}"


@pytest.fixture(scope="session")
def api_base_url(base_url: str) -> str:
    return f"{base_url}/api"


@pytest.fixture
def api_client(api_base_url: str, user_id: str) -> ApiClient:
    return ApiClient(
        base_url=api_base_url,
        user_id=user_id,
    )


@pytest.fixture
def betting_service(api_client: ApiClient) -> BettingService:
    return BettingService(api_client)


@pytest.fixture
def reset_balance(betting_api: BettingApi) -> dict:
    response: Response = betting_api.reset_balance()

    assert response.status_code == 200, (
        f"Failed to reset balance. "
        f"Status code: {response.status_code}, Response: {response.text}"
    )

    return response.json()


@pytest.fixture
def driver(config: ConfigReader) -> WebDriver:
    options = webdriver.ChromeOptions()

    if config.get_boolean("browser", "headless"):
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver_instance = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    driver_instance.implicitly_wait(
        config.get_int("browser", "implicit_wait")
    )

    yield driver_instance

    driver_instance.quit()
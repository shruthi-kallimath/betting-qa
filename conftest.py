import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.api_client import ApiClient
from api.betting_api import BettingApi
from config.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture(scope="session")
def base_url(config):
    return config.get("app", "base_url")


@pytest.fixture(scope="session")
def user_id(config):
    return config.get("app", "user_id")


@pytest.fixture(scope="session")
def app_url(base_url, user_id):
    return f"{base_url}/?user-id={user_id}"


@pytest.fixture(scope="session")
def api_base_url(base_url):
    return f"{base_url}/api"


@pytest.fixture
def api_client(api_base_url, user_id):
    return ApiClient(
        base_url=api_base_url,
        user_id=user_id
    )


@pytest.fixture
def betting_api(api_client):
    return BettingApi(api_client)

@pytest.fixture
def reset_balance(betting_api):
    response = betting_api.reset_balance()

    assert response.status_code == 200

    return response.json()


@pytest.fixture
def driver(config):
    options = webdriver.ChromeOptions()

    if config.get_boolean("browser", "headless"):
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(
        config.get_int("browser", "implicit_wait")
    )

    yield driver

    driver.quit()



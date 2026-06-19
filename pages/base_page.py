from decimal import Decimal
import os
import re
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def refresh_page(self) -> None:
        self.driver.refresh()

    def pause_for_demo(self) -> None:
        if os.getenv("SLOW_UI", "false").lower() == "true":
            time.sleep(2)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def finds(self, locator: Locator) -> list[WebElement]:
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator: Locator) -> None:
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self, locator: Locator, text: str | int | float | Decimal) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(str(text))

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text.strip()

    def is_visible(self, locator: Locator) -> bool:
        return self.find(locator).is_displayed()

    def parse_money(self, text: str) -> Decimal:
        return self._parse_decimal(text)

    def parse_decimal(self, text: str) -> Decimal:
        return self._parse_decimal(text)

    def _parse_decimal(self, text: str) -> Decimal:
        cleaned_text = re.sub(r"[^\d.,]", "", text).replace(",", ".")
        return Decimal(cleaned_text).quantize(Decimal("0.01"))
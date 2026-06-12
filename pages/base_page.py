from decimal import Decimal
import re
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def pause_for_demo(self):
        if os.getenv("SLOW_UI", "false").lower() == "true":
            time.sleep(2)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def finds(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(str(text))

    def get_text(self, locator):
        return self.find(locator).text.strip()

    def is_visible(self, locator):
        return self.find(locator).is_displayed()

    def parse_money(self, text):
        cleaned_text = re.sub(r"[^\d.,]", "", text).replace(",", ".")
        return Decimal(cleaned_text).quantize(Decimal("0.01"))

    def parse_decimal(self, text):
        cleaned_text = re.sub(r"[^\d.,]", "", text).replace(",", ".")
        return Decimal(cleaned_text).quantize(Decimal("0.01"))
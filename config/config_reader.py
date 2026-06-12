import configparser
from pathlib import Path


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()

        config_path = (
            Path(__file__).parent / "config.ini"
        )

        self.config.read(config_path)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)

    def get_boolean(self, section, key):
        return self.config.getboolean(section, key)
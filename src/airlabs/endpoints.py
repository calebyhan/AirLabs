import functions
import requests
import json


class API:
    def __init__(self, api_key: str):
        """
        Instantiation to input api key.

        Args:
            api_key:
        """
        self.api_key = api_key
        self.version = "9"
        self.url = f"https://airlabs.co/api/v{self.version}/"

    def _check_api_key(self):
        """
        Check if api key exists

        Returns:
            Raises a ValueError if api key is not defined.
        """
        if self.api_key == "":
            raise ValueError("Empty API Key.")

    def flights(self, ) -> dict:

        self._check_api_key()

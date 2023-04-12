import airlabs.functions as functions
import requests


class API:
    def __init__(self, api_key: str):
        """
        Instantiation to input api key.

        Args:
            api_key: Input api key
        """

        self.api_key = api_key
        self.version = "9"
        self.url = f"https://airlabs.co/api/v{self.version}/"

    def _check_api_key(self, params: dict) -> dict:
        """
        Check if api key exists, if so return parameters with the api key.

        Args:
            params: dict to parse

        Returns:
            Raises a ValueError if api key is not defined. If defined, return a dict with the api key.
        """

        if self.api_key == "":
            raise ValueError("Empty API Key.")
        else:
            return {"api_key": self.api_key} | params

    def flights(self, **input_params) -> dict:
        """
        Flights endpoint: https://airlabs.co/docs/flights.

        Args:
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "flights", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def schedules(self, **input_params) -> dict:
        """
        Schedules endpoint: https://airlabs.co/docs/schedules.

        Args:
            **input_params: Optional input parameters (NOTE: need one required argument of one listed)

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "schedules", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def delays(self, delay: str, type: str, **input_params) -> dict:
        """
        Delays endpoint: https://airlabs.co/docs/delays.

        Args:
            delay: Minimum delayed time (in minutes. > 30 min)
            type: Flights type - departures or arrivals
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        input_params = input_params | {"delay": delay,
                                       "type": type}
        params = self._check_api_key(input_params)
        response = requests.get(self.url + "delays", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def flight(self, **input_params) -> dict:
        """
        Flight endpoint: https://airlabs.co/docs/flight.

        Args:
            **input_params: Optional input parameters (NOTE: need one required argument of one listed)

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "flight", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def nearby(self, lat: str, lng: str, distance: str, **input_params) -> dict:
        """
        NearBy endpoint: https://airlabs.co/docs/nearby.

        Args:
            lat: Geo location Latitude.
            lng: Geo location Longitude.
            distance: Distance from required Geo location (km)
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        input_params = input_params | {"lat": lat, "lng": lng, "distance": distance}
        params = self._check_api_key(input_params)
        response = requests.get(self.url + "nearby", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def suggest(self, q: str, **input_params) -> dict:
        """
        Suggest endpoint: https://airlabs.co/docs/suggest.

        Args:
            q: Part of the destination name - airport, city or country. Between 3 and 30 characters.
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        input_params = input_params | {"q": q}
        params = self._check_api_key(input_params)
        response = requests.get(self.url + "suggest", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def airlines(self, **input_params) -> dict:
        """
        Airlines endpoint: https://airlabs.co/docs/airlines.

        Args:
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "airlines", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def airports(self, **input_params) -> dict:
        """
        Airports endpoint: https://airlabs.co/docs/airports.

        Args:
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "airports", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def cities(self, **input_params) -> dict:
        """
        Cities endpoint: https://airlabs.co/docs/cities.

        Args:
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "cities", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def fleets(self, **input_params) -> dict:
        """
        Fleets endpoint: https://airlabs.co/docs/fleets.

        Args:
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "fleets", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def routes(self, **input_params) -> dict:
        """
        Routes endpoint: https://airlabs.co/docs/routes.

        Args:
            **input_params: Optional input parameters (NOTE: need one required argument of one listed)

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "routes", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def countries(self, **input_params) -> dict:
        """
        Countries endpoint: https://airlabs.co/docs/countries.

        Args:
            **input_params: Optional input parameters

        Returns:
            If no error, returns dict object from api.
        """

        params = self._check_api_key(input_params)
        response = requests.get(self.url + "countries", params=params).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def timezones(self) -> dict:
        """
        Timezones endpoint: https://airlabs.co/docs/timezones.

        Returns:
            If no error, returns dict object from api.
        """

        response = requests.get(self.url + "timezones", params={"api_key": self.api_key}).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

    def taxes(self) -> dict:
        """
        Taxes endpoint: https://airlabs.co/docs/taxes.

        Returns:
            If no error, returns dict object from api.
        """

        response = requests.get(self.url + "taxes", params={"api_key": self.api_key}).json()
        error = functions.error(response)
        if error[0]:
            raise ValueError("Error from calling API - " + error[1])
        return response

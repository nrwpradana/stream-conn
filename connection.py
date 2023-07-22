from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import requests
import pandas as pd

class OpenWeatherMapConnection(ExperimentalBaseConnection):
    """Basic st.experimental_connection implementation for OpenWeatherMap"""

    def _connect(self, **kwargs) -> None:
        # You can put any setup code here if needed
        pass

    def _get_api_key(self):
        # Replace 'your_openweathermap_api_key' with your actual API key
        # You can get an API key by signing up on the OpenWeatherMap website
        return '34ef5fe7db281490d556352cba3a3890'

    def get_weather_data(self, city: str, country: str = "US") -> pd.DataFrame:
        api_key = self._get_api_key()
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": f"{city},{country}",
            "appid": api_key,
            "units": "metric",  # Change to "imperial" for Fahrenheit units
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame({
                "City": [data["name"]],
                "Country": [data["sys"]["country"]],
                "Temperature (°C)": [data["main"]["temp"]],
                "Description": [data["weather"][0]["description"]],
            })
            return df
        else:
            # In case of an error, return an empty DataFrame
            return pd.DataFrame()

    def query(self, city: str, country: str = "US", ttl: int = 3600) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(city: str, country: str, **kwargs) -> pd.DataFrame:
            return self.get_weather_data(city, country)

        return _query(city, country)

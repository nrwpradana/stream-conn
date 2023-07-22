import streamlit as st
import requests
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

class OpenWeatherMapConnection(ExperimentalBaseConnection[OpenWeatherMapConnection]):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def _connect(self):
        # No specific connection setup is required for OpenWeatherMap API
        pass

    def cursor(self):
        # Return the OpenWeatherMap API instance, which is just the base URL
        return self.base_url

    @st.cache_data(ttl=600)  # Cache data for 10 minutes to reduce API calls
    def query(self, city_name):
        # Perform the API query and return weather data for the specified city
        url = f"{self.base_url}?q={city_name}&appid={self.api_key}"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            return data
        else:
            st.error("Error fetching weather data from OpenWeatherMap API.")
            st.error(data["message"])
            return None

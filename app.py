import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import requests

class OpenWeatherMapConnection(ExperimentalBaseConnection[requests.Session]):
    """Basic st.experimental_connection implementation for OpenWeatherMap API"""

    def _connect(self, api_key: str, **kwargs) -> requests.Session:
        session = requests.Session()
        session.params = {"appid": api_key}
        st.success("Connected to OpenWeatherMap API successfully.")
        return session

    def cursor(self) -> requests.Session:
        return self._instance

    def query(self, city: str, ttl: int = 3600) -> dict:
        @cache_data(ttl=ttl)
        def _query(city: str) -> dict:
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "units": "metric"}
            response = self.cursor().get(url, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                st.error(f"Failed to fetch weather data. Error code: {response.status_code}")
                return {}

        return _query(city)

def main():
    st.title("OpenWeatherMap Streamlit App")

    # API key input
    api_key = st.text_input("Enter your OpenWeatherMap API key:")

    if not api_key:
        st.warning("Please enter your OpenWeatherMap API key.")
        st.stop()

    # Create a connection object
    connection = OpenWeatherMapConnection(api_key)

    # Query form
    st.subheader("Fetch Weather Data")
    city = st.text_input("Enter the city name:")

    if st.button("Fetch"):
        if city:
            weather_data = connection.query(city)
            if weather_data:
                st.write("Weather Data for", city)
                st.write(weather_data)
            else:
                st.warning("Weather data not available for the provided city.")
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()

import streamlit as st
from connection import OpenWeatherMapConnection

def main():
    st.title("OpenWeatherMap API Connection Demo")

    # Get the OpenWeatherMap API key from the user through a text input
    api_key = st.text_input("Enter your OpenWeatherMap API key", type="password")

    # Get the OpenWeatherMapConnection instance from the connection
    connection = st.connection.get_connection(
        key="openweathermap_connection",
        config=OpenWeatherMapConnection,
        api_key=api_key
    )

    if connection.api_key:
        st.success("OpenWeatherMap API connected successfully!")

        # Demo OpenWeatherMap API functionality
        st.header("Demo OpenWeatherMap API Functionality")

        # Example query to retrieve weather data for a specific city
        city_name = st.text_input("Enter a city name")
        if city_name:
            weather_data = connection.query(city_name)
            if weather_data:
                st.write("Weather Data:")
                st.write(weather_data)

if __name__ == "__main__":
    main()

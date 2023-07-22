import streamlit as st
from connection import OpenWeatherMapConnection

def get_connection(connection_name):
    if connection_name not in st.session_state:
        api_key = st.text_input("Enter your OpenWeatherMap API key", type="password")
        st.session_state[connection_name] = OpenWeatherMapConnection(api_key)
    return st.session_state[connection_name]

def main():
    st.title("OpenWeatherMap API Connection Demo")

    # Get the OpenWeatherMapConnection instance from the connection
    connection_name = "openweathermap_connection"
    connection = get_connection(connection_name)

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

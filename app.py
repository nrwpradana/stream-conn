import streamlit as st
from connection import OpenWeatherMapConnection

def main():
    st.title("OpenWeatherMap Streamlit App")

    # Create an instance of the OpenWeatherMapConnection
    connection = OpenWeatherMapConnection()

    # Get user input for the city and country
    city = st.text_input("Enter the city name", "London")
    country = st.text_input("Enter the country code", "GB")

    if st.button("Get Weather"):
        # Call the query method to retrieve weather data for the specified city
        weather_data = connection.query(city, country)

        if not weather_data.empty:
            st.subheader("Weather Information")
            st.write(weather_data)
        else:
            st.error("Weather data not available. Please check the city and country code.")

if __name__ == "__main__":
    main()

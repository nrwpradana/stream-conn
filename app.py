import streamlit as st
import pandas as pd
from connection import VirusTotalConnection

st.title("VirusTotal API Test")

# Input for user to enter the VirusTotal API key
API_KEY = st.text_input("Enter your VirusTotal API key", type="password")

# Check if the API key is provided
if API_KEY:
    connection = VirusTotalConnection(API_KEY)

    # Input for user to enter the URL
    url = st.text_input("Enter the URL you want to test")

    # Check if the URL is provided
    if url:
        url_report = connection.get_url_report(url)

        st.subheader("URL Report:")
        st.write(pd.DataFrame.from_dict(url_report))
    else:
        st.warning("Please enter a URL.")
else:
    st.warning("Please enter your VirusTotal API key.")


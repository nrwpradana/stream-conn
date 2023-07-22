import streamlit as st
import pandas as pd
from connection import VirusTotalConnection

st.title("VirusTotal API Test")

# Input for user to enter the VirusTotal API key
API_KEY = st.text_input("Enter your VirusTotal API key", type="password")

# Check if the API key is provided
if API_KEY:
    connection = VirusTotalConnection(API_KEY)

    # Test the connection with a SHA256 hash
    sha256_hash = "8c52bb3c67a0de4c0f1590057b2a864158e30aa9c717eaa01a32b1cf8ae9bbfd"
    file_report = connection.get_file_report(sha256_hash)

    # Test the connection with a URL
    url = "YOUR_URL"
    url_report = connection.get_url_report(url)

    st.subheader("File Report:")
    st.write(pd.DataFrame.from_dict(file_report))

    st.subheader("URL Report:")
    st.write(pd.DataFrame.from_dict(url_report))
else:
    st.warning("Please enter your VirusTotal API key.")

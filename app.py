import streamlit as st
import pandas as pd
from connection import VirusTotalConnection

st.title("VirusTotal API Test")

# Input for user to enter the VirusTotal API key
API_KEY = st.text_input("Enter your VirusTotal API key", type="password")

# Check if the API key is provided
if API_KEY:
    connection = VirusTotalConnection(API_KEY)

    # Input for user to enter the SHA256 hash
    sha256_hash = st.text_input("Enter the hash file (SHA256) you want to test")

    # Check if the SHA256 hash is provided
    if sha256_hash:
        file_report = connection.get_file_report(sha256_hash)

        st.subheader("File Report:")
        st.write(pd.DataFrame.from_dict(file_report))
    else:
        st.warning("Please enter a SHA256 hash.")
else:
    st.warning("Please enter your VirusTotal API key.")

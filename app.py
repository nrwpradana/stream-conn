import streamlit as st
import pandas as pd
import hashlib
from connection import VirusTotalConnection

st.title("VirusTotal API Test")

# Input for user to enter the VirusTotal API key
API_KEY = st.text_input("Enter your VirusTotal API key", type="password")

# Check if the API key is provided
if API_KEY:
    connection = VirusTotalConnection(API_KEY)

    # Input for user to upload a file
    uploaded_file = st.file_uploader("Upload a file")

    # Check if a file is uploaded
    if uploaded_file:
        # Calculate SHA256 hash of the uploaded file
        sha256_hash = hashlib.sha256(uploaded_file.read()).hexdigest()

        st.subheader("SHA256 Hash:")
        st.write(sha256_hash)

        # Get the report for the SHA256 hash
        file_report = connection.get_file_report(sha256_hash)

        st.subheader("File Report:")
        st.write(pd.DataFrame.from_dict(file_report))
    else:
        st.warning("Please upload a file.")
else:
    st.warning("Please enter your VirusTotal API key.")

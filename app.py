import streamlit as st
from connection import VirusTotalConnection

# Retrieve the VirusTotal API key from Streamlit secrets
API_KEY = st.secrets["1578cfbb6b7c950b6a61c56ab5bc30087254b25773a4560eb6d361091541ecde"]
connection = VirusTotalConnection(API_KEY)

st.title("VirusTotal API Test")

# Input for user to enter SHA256 hash or URL
input_type = st.radio("Select Input Type", ("SHA256 Hash", "URL"))

if input_type == "SHA256 Hash":
    sha256_hash = st.text_input("Enter SHA256 Hash")
    if st.button("Get File Report"):
        if sha256_hash:
            report = connection.get_file_report(sha256_hash)
            st.json(report)
        else:
            st.error("Please enter a valid SHA256 hash.")

else:
    url = st.text_input("Enter URL")
    if st.button("Get URL Report"):
        if url:
            report = connection.get_url_report(url)
            st.json(report)
        else:
            st.error("Please enter a valid URL.")

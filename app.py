import streamlit as st
import pandas as pd
from connection import VirusTotalConnection

st.title("VirusTotal API Test")

# Replace 'YOUR_VIRUSTOTAL_API_KEY' with your actual VirusTotal API key
API_KEY = '1578cfbb6b7c950b6a61c56ab5bc30087254b25773a4560eb6d361091541ecde'
connection = VirusTotalConnection(API_KEY)

# Test the connection with a SHA256 hash
sha256_hash = "8c52bb3c67a0de4c0f1590057b2a864158e30aa9c717eaa01a32b1cf8ae9bbfd"
file_report = connection.get_file_report(sha256_hash)

# Test the connection with a URL
#url = "YOUR_URL"
#url_report = connection.get_url_report(url)

st.subheader("File Report:")
st.write(pd.DataFrame.from_dict(file_report))

#st.subheader("URL Report:")
#st.write(pd.DataFrame.from_dict(url_report))

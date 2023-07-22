import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import kaggle
import pandas as pd

class KaggleConnection(ExperimentalBaseConnection[kaggle.api.KaggleApi]):
    """Basic st.experimental_connection implementation for Kaggle API"""

    def _connect(self, kaggle_json_path: str) -> kaggle.api.KaggleApi:
        api = kaggle.api.Api()
        api.authenticate(apikey_path=kaggle_json_path)
        st.success("Connected to Kaggle API successfully.")
        return api

    def cursor(self) -> kaggle.api.KaggleApi:
        return self._instance

    def query(self, competition_name: str, file_name: str, ttl: int = 3600) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(competition_name: str, file_name: str) -> pd.DataFrame:
            api = self.cursor()
            api.competition_download_file(competition=competition_name, file_name=file_name)
            df = pd.read_csv(file_name)
            return df

        return _query(competition_name, file_name)

def main():
    st.title("Kaggle Streamlit App")

    # Kaggle API token JSON file input
    kaggle_json_path = st.text_input("Enter the path to your Kaggle API token JSON file:")

    if not kaggle_json_path:
        st.warning("Please enter the path to your Kaggle API token JSON file.")
        st.stop()

    # Create a connection object
    connection = KaggleConnection(kaggle_json_path)

    # Query form
    st.subheader("Download Kaggle Competition Data")
    competition_name = st.text_input("Enter the competition name:")
    file_name = st.text_input("Enter the file name to download:")

    if st.button("Download"):
        if competition_name and file_name:
            df = connection.query(competition_name, file_name)
            if not df.empty:
                st.write("Downloaded Data:")
                st.write(df)
            else:
                st.warning("Data not available or failed to download.")
        else:
            st.warning("Please enter the competition name and file name.")

if __name__ == "__main__":
    main()

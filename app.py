import streamlit as st
import requests
import pandas as pd

# Define the Connection class for Etherscan API
class EtherscanConnection:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.etherscan.io/api"

    def _connect(self):
        # No specific connection setup is required for Etherscan API
        pass

    def cursor(self):
        # Return the Etherscan API instance, which is just the base URL
        return self.base_url

    @st.cache_data(allow_output_mutation=True)
    def query(self, module, action, params=None):
        # Perform the API query and return the response as a pandas DataFrame
        url = f"{self.base_url}?module={module}&action={action}&apikey={self.api_key}"

        if params:
            for key, value in params.items():
                url += f"&{key}={value}"

        response = requests.get(url)
        data = response.json()

        if data["status"] == "1":
            df = pd.DataFrame(data["result"])
            return df
        else:
            st.error("Error fetching data from Etherscan API.")
            st.error(data["message"])
            return None

# Create an instance of the EtherscanConnection class using st.experimental_connection
@st.experimental_connection(backend="etherscan_connection")
def create_connection():
    api_key = st.text_input("Enter your Etherscan API key", type="password")
    return EtherscanConnection(api_key)

def main():
    st.title("Etherscan API Connection Demo")

    # Get the EtherscanConnection instance from the connection
    connection = create_connection()

    if connection.api_key:
        st.success("Etherscan API connected successfully!")

        # Demo Etherscan API functionality
        st.header("Demo Etherscan API Functionality")

        # Example query to retrieve Ethereum transactions by address
        address = st.text_input("Enter an Ethereum address")
        if address:
            params = {
                "address": address,
                "startblock": 0,
                "endblock": 99999999,
                "sort": "asc",
                "apikey": connection.api_key
            }
            df = connection.query(module="account", action="txlist", params=params)

            if df is not None:
                st.write("Transactions for Address:")
                st.write(df)

if __name__ == "__main__":
    main()

import streamlit as st
import requests

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

    @st.cache(allow_output_mutation=True)
    def query(self, module, action, address, tag="latest"):
        # Perform the API query and return the balance for the specified Ethereum address
        url = f"{self.base_url}?module=account&action=balance&address={address}&tag=latest&apikey={self.api_key}"

        response = requests.get(url)
        data = response.json()

        if data["status"] == "1":
            balance = data["result"]
            return balance
        else:
            st.error("Error fetching data from Etherscan API.")
            st.error(data["message"])
            return None

# Create an instance of the EtherscanConnection class using st.experimental_connection
#@st.experimental_memo(backend="etherscan_connection")
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

        # Example query to retrieve Ethereum balance by address
        address = st.text_input("Enter an Ethereum address")
        if address:
            balance = connection.query(module="account", action="balance", address=address)
            if balance is not None:
                st.write("Ethereum Address Balance:")
                st.write(balance)

if __name__ == "__main__":
    main()

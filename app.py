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
#def create_connection:
    
    

def main():
    st.title("Etherscan API Connection Demo")

    api_key = st.text_input("Enter your Etherscan API key", type="password")
    # Get the EtherscanConnection instance from the connection
    connection = st.experimental_connection(EtherscanConnection(api_key))

    if connection.api_key:
        st.success("Etherscan API connected successfully!")

        # Demo Etherscan API functionality
        st.header("Demo Etherscan API Functionality")

        # Example query to retrieve Ethereum balance by address
        st.text("Example Address : 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae")
        address = st.text_input("Enter an Ethereum address")
        if address:
            balance = connection.query(module="account", action="balance", address=address)
            if balance is not None:
                st.write("Ethereum Address Balance:")
                st.write(balance)

    link_text = "Click here to visit Github"
    link_url = "https://github.com/nrwpradana/stream-conn"
    link_markdown = f"[{link_text}]({link_url})"
    st.markdown(link_markdown, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

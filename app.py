import streamlit as st
import requests

class EtherscanConnection(ExperimentalBaseConnection):
    def _connect(self, api_key):
        # Return the Etherscan API key as the connection object
        return api_key

    def cursor(self):
        # Return the Etherscan API key (connection object) as the cursor
        return self._instance

    @st.cache(allow_output_mutation=True)
    def query(self, module, action, address, tag="latest"):
        # Perform the API query and return the balance for the specified Ethereum address
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={self.cursor()}"

        response = requests.get(url)
        data = response.json()

        if data["status"] == "1":
            balance = data["result"]
            return balance
        else:
            st.error("Error fetching data from Etherscan API.")
            st.error(data["message"])
            return None

def main():
    st.title("Etherscan Streamlit App")

    # API key input
    api_key = st.text_input("Enter your Etherscan API key:")

    if not api_key:
        st.warning("Please enter your Etherscan API key.")
        st.stop()

    # Create a connection object
    connection = EtherscanConnection(api_key)

    # Query form
    st.subheader("Fetch Ethereum Balance")
    address = st.text_input("Enter the Ethereum address:")

    if st.button("Fetch"):
        if address:
            balance = connection.query(module="account", action="balance", address=address)
            if balance is not None:
                st.write(f"Balance of {address}: {balance} wei")
            else:
                st.warning("Failed to fetch balance.")
        else:
            st.warning("Please enter an Ethereum address.")

if __name__ == "__main__":
    main()
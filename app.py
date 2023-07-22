import os
import streamlit as st
import kaggle
import json

def authenticate_kaggle_api(json_data):
    # Load the Kaggle credentials from the JSON file
    kaggle_credentials = json.loads(json_data)

    # Set Kaggle environment variables
    os.environ['KAGGLE_USERNAME'] = kaggle_credentials['username']
    os.environ['KAGGLE_KEY'] = kaggle_credentials['key']

    # Verify the Kaggle API configuration
    kaggle.api.authenticate()

def main():
    st.title("Kaggle API Interaction with Streamlit")

    # File Uploader to upload Kaggle account JSON
    uploaded_file = st.file_uploader("Upload Kaggle Account JSON", type=["json"])

    if uploaded_file is not None:
        # Read the JSON file data
        json_data = uploaded_file.read()

        # Try authenticating the Kaggle API using the uploaded JSON data
        try:
            authenticate_kaggle_api(json_data)
            st.success("Kaggle API authentication successful!")
        except Exception as e:
            st.error("Kaggle API authentication failed. Please check the JSON file.")
            st.error(e)
            return

        # You can now use the Kaggle API here
        # For example, list Kaggle datasets
        datasets = kaggle.api.dataset_list()
        st.write("List of Kaggle Datasets:")
        st.write(datasets)

if __name__ == "__main__":
    main()

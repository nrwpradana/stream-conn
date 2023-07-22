from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import pandas as pd
import requests

class VirusTotalConnection(ExperimentalBaseConnection):
    """Basic st.experimental_connection implementation for VirusTotal API"""

    def __init__(self, api_key):
        self.api_key = api_key

    def _request(self, endpoint, params=None):
        headers = {
            'x-apikey': self.api_key
        }
        url = f'https://www.virustotal.com/api/v3/{endpoint}'
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def _connect(self, **kwargs) -> "VirusTotalConnection":
        return self

    def get_file_report(self, sha256, ttl: int = 3600) -> dict:
        @cache_data(ttl=ttl)
        def _get_file_report(sha256):
            return self._request(f'files/{sha256}')
        
        return _get_file_report(sha256)

    def get_url_report(self, url, ttl: int = 3600) -> dict:
        @cache_data(ttl=ttl)
        def _get_url_report(url):
            params = {'resource': url}
            return self._request('urls', params=params)
        
        return _get_url_report(url)

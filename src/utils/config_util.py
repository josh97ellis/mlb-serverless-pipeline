import json
from pathlib import Path


class ConfigUtil:
    config_path: str = f"{Path(__file__).parent.parent.parent}/config/config.json"

    def __init__(self):
        with open(self.config_path) as f:
            self.config_data = json.load(f)
    
    def get_rapid_api_key(self):
        return self.config_data['rapid-api']['X-RapidAPI-Key']
    
    def get_rapid_api_host(self):
        return self.config_data['rapid-api']['X-RapidAPI-Host']
    
    def get_api_baseball_url(self):
        return self.config_data['api-baseball']['root-url']
    
    def get_storage_account_url(self):
        return self.config_data['azure']['storage-account-url']
    
    def get_container_name(self):
        return self.config_data['azure']['ingest-container-name']

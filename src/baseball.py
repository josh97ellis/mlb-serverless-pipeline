import requests
from utils.config_util import ConfigUtil


class Baseball:
    routing_information = {
        "container_name": ConfigUtil().get_container_name()}
    
    def __init__(self, get: str):
        self.storage_account_url = ConfigUtil().get_storage_account_url()
        self.api_url = f"{ConfigUtil().get_api_baseball_url()}/{get}"
        self.querystring = None
        self.headers = {
            "X-RapidAPI-Key": ConfigUtil().get_rapid_api_key(),
            "X-RapidAPI-Host": ConfigUtil().get_rapid_api_host()
        }
    
    def _get_api_response(self) -> None:
        response = requests.get(
            url=self.api_url,
            headers=self.headers,
            params=self.querystring
        )
        
        self.data = response.json()['response']

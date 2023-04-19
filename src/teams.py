import pandas as pd
import json
from baseball import Baseball


class Teams(Baseball):
    """
    Interaction with https://api-baseball.p.rapidapi.com/teams api endpoint
    """
    schema: dict = {
        'id': str,
        'name': str,
        'logo': str}

    def __init__(self, get='teams'):
        super().__init__(get)
        self.querystring = {"league":"1", 'season':'2023'}
        self._get_api_response()  # Creates the data attribute
    
    def parse_response(self):
        list = []
        for i in self.data:
            row = {
                'id': i["id"],
                'name': i["name"],
                "logo": i["logo"]}
            list.append(row)
        
        payload = json.loads(pd.DataFrame(list).to_json(orient='records'))
        return payload
        
    def upload_blob(self, data: dict):
        json_struct = {
            "routing_information": self.routing_information,
            "schema": self.schema,
            "payload": {
                "leagues": data
            }
        }
        
        return json_struct
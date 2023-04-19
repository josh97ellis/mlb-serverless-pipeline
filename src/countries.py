import pandas as pd
import json
from baseball import Baseball


class Countries(Baseball):
    """
    Interaction with https://api-baseball.p.rapidapi.com/countries api endpoint
    """
    schema: dict = {
        'id': str,
        'name': str,
        'code': str,
        'flag': str}

    def __init__(self, get='countries'):
        super().__init__(get)
    
    def parse_response(self):
        list = []
        for i in self.data:
            row = {
                'id': i["id"],
                'name': i["name"],
                "code": i["code"],
                "flag": i["flag"]}
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

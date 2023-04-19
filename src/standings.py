import pandas as pd
import json
from baseball import Baseball


class Standings(Baseball):
    """
    Interaction with https://api-baseball.p.rapidapi.com/standings api endpoint
    """
    schema: dict = {
        'position': int,
        'stage': str,
        'group': str,
        'team_id': str,
        'league_id': str,
        'games_played': int,
        'games_won': int,
        'games_lost': int,
        'runs_for': int,
        'runs_against': int,
        'form': str
        }
    
    object_name: str = 'standings'

    def __init__(self, get='standings'):
        super().__init__(get)
        self.querystring = {
            "league": "1",
            "season": "2023"}
        self._get_api_response()  # Creates the data attribute
    
    def parse_response(self):
        list = []
        for i in self.data[0]:
            row = {
                "position": i["position"],
                "stage": i["stage"],
                "group": i['group']['name'],
                "team_id": i["team"]["id"],
                "league_id": i["league"]["id"],
                "games_played": i['games']['played'],
                "games_won": i['games']['win']['total'],
                "games_lost": i['games']['lose']['total'],
                "runs_for": i["points"]["for"],
                "runs_against": i["points"]["against"],
                "form": i["form"]}
            list.append(row)
        
        payload = json.loads(pd.DataFrame(list).to_json(orient='records'))
        return payload
        
    def upload_blob(self, data: dict):
        json_struct = {
            "routing_information": self.routing_information,
            "schema": self.schema,
            "payload": {
                self.object_name: data
            }
        }
        
        return json_struct
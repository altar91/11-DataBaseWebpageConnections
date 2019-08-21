import json
import requests
import csv
import warnings
warnings.filterwarnings("ignore")


def zoho_connections():
    parameters_app = {'authtoken': 'token_id',
                      'scope': 'creatorapi', 'zc_ownername': 'user_name', 'raw': 'true'}

    res_app = requests.get(r'https://zoho_URL/api/json/applications',
                           params=parameters_app)

    res_app.raise_for_status()  #Checks the connection
    app_json_data = json.loads(res_app.text) #Convernts data to json format

#read the json files and provide the json data
#read from the excel files
import json


def get_payload_auth():
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


# read the json files and provide the json data
# read from the excel files
import json


def get_payload_auth():
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json",
    }
    return headers


def update_headers(temp_t):
    update_booking_headers = {
        "content_type": "application/json",
        "Cookie": "token=" + temp_t
    }
    return update_booking_headers

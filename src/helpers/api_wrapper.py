import json

import requests


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_request(url, auth, headers, payload, in_json):
    # Call the function to get the payload dictionary
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def put_data(url, headers, payload):
    patch_response_data = requests.patch(url=url, headers=headers,  json=payload)

    return patch_response_data


def delete_data(url, headers):
    delete_response_data = requests.delete(url=url, headers=headers)
    return delete_response_data

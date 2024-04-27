'''
author:Megha

# tc1 verify status code,headers
tc2 verify the body id
tc3 verify json shcema is valid
'''
import pytest
import requests

from src.constant.apiconstant import base_url, url_create_booking, url_update_delete_booking, url_create_token
from src.helpers.api_wrapper import post_request, put_data, delete_data
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.utils import common_headers, update_headers
from src.helpers.common_verification import *


class TestIntegration(object):
    @pytest.fixture()
    def test_create_token(self):
        response_token = post_request(url_create_token(), headers=common_headers(), auth=None,
                                      payload=payload_create_token(), in_json=False)
        token = (response_token.json()['token'])
        print("beforetoken", token)
        return token

    @pytest.fixture()
    def test_create_booking_tc1(self):
        response_booking = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                        payload=payload_create_booking(), in_json=False)
        bookingid = (response_booking.json()['bookingid'])
        print("booking_id is", bookingid)
        return bookingid

    def test_update(self, test_create_token, test_create_booking_tc1):
        temp_token = test_create_token
        print("after token", temp_token)

        put_url = url_update_delete_booking(test_create_booking_tc1)
        print("URL for updating booking:", put_url)  # Print the URL for updating the booking

        response_update = put_data(put_url, payload=payload_update_booking(),
                                   headers=update_headers(temp_token))

        print("json after updating", response_update.json())

    def test_delete_booking(self, test_create_booking_tc1, test_create_token):
        temp_token = test_create_token
        print("after token", temp_token)
        print("id which we want to delete",test_create_booking_tc1)
        delete_url = url_update_delete_booking(test_create_booking_tc1)

        response_delete = delete_data(delete_url, headers=update_headers(temp_token))

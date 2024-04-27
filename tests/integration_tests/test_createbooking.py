'''
author:Megha

# tc1 verify status code,headers
tc2 verify the body id
tc3 verify json shcema is valid
'''

from src.constant.apiconstant import base_url, url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import *

'''
class TestIntegration(object):

    def test_crete_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        print(response.json())
       # booking_id = response.json()["bookingid"]
        verify_key(response.json() ["bookingid"])


'''
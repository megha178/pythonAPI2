def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking():
    payload_update = {
        "firstname": "ereeeee",
        "lastname": "jawn",
        "totalprice": 151,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    return payload_update


def payload_create_token():
    create_token_payload = {
        "username": "admin",
        "password": "password123"

    }
    return create_token_payload


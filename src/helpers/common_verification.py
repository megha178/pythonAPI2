def verify_http_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected HTTP status: " + expected_data


def verify_key(key):
    assert key != 0, "Bookingd is non empty" + key
    assert key > 0, "key should be greater than 0" + key

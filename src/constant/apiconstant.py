# add ur constants here
# adding url constants

def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_update_delete_booking(bookingid):
    return "https://restful-booker.herokuapp.com/booking/" + str(bookingid)

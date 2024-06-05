import datetime
import pytest
from .book_entities import Book, BookingDates
from .booking_client import create_booking
from ..config import first_name_cnfg, last_name_cnfg, totalprice_cnfg, depositpaid_cnfg, additionalneeds_cnfg


def booking_dates():
    checkin_date = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    checkout_date = (datetime.date.today() + datetime.timedelta(days=9)).strftime("%Y-%m-%d")
    return checkin_date, checkout_date


def create_booking_data(firstname, lastname, totalprice, depositpaid, additionalneeds):
    checkin_date, checkout_date = booking_dates()
    booking = Book(
        firstname=firstname,
        lastname=lastname,
        totalprice=totalprice,
        depositpaid=depositpaid,
        bookingdates=BookingDates(checkin=checkin_date, checkout=checkout_date),
        additionalneeds=additionalneeds
    )
    return booking


@pytest.fixture
def create_booking_fixture():
    booking=create_booking_data(first_name_cnfg, last_name_cnfg, totalprice_cnfg, depositpaid_cnfg, additionalneeds_cnfg)
    booking_id = create_booking(booking)
    return booking_id

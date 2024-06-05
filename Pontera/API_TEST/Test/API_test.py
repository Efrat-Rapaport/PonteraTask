import pytest
from Pontera.API_TEST.infra.booking_client import get_all_bookings
from ..infra.book_helper import create_booking_fixture


def test_new_booking_appears_in_all_booking_results(create_booking_fixture):
    booking_id = create_booking_fixture
    print(f"Booking created with ID: {booking_id}")

    bookings = get_all_bookings()
    booking_ids = [booking['bookingid'] for booking in bookings]
    assert booking_id in booking_ids, print(f"Booking ID {booking_id} not found in booking list")

    print("New booking appears in all booking results")


if __name__ == "__main__":
    pytest.main()
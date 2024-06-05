import requests
from dataclasses import asdict

BASE_URL = "https://restful-booker.herokuapp.com"


def create_booking(booking_payload):
    booking_dict = asdict(booking_payload)

    response = requests.post(f"{BASE_URL}/booking", json=booking_dict)
    assert response.status_code == 200, f"Failed to create booking: {response.text}"
    booking_id = response.json().get('bookingid')
    return booking_id


def get_all_bookings():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200, f"Failed to get bookings: {response.text}"
    return response.json()
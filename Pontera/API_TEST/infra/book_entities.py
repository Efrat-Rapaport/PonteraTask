from dataclasses import dataclass

@dataclass
class BookingDates:
    checkin: str
    checkout: str

@dataclass
class Book:
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str = ""
import abc

import pandas
import abc

df = pandas.read_csv("files/hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("files/hotels.csv", index=False)

    def __eq__(self, other):
        if self.name == other.name \
                and self.hotel_id == other.hotel_id:
            return True
        else:
            return False

    def __add__(self, other):
        print("You cannot add hotels together, silly.")
        return None

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    @staticmethod
    def convert(amount):
        return amount * 2


class Ticket(abc.ABC):
    @abc.abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name


hotel_one = Hotel(hotel_id="188")
hotel_two = Hotel(hotel_id="188")
print(hotel_one.available())
print(hotel_one.hotel_id)
print(hotel_two.name)
print(Hotel.watermark)
print(Hotel.get_hotel_count(data=df))
print(hotel_one.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="John smith  ", hotel_object=hotel_one)
print(ticket.the_customer_name)
ticket.generate()
print(Hotel.convert(4))
print(hotel_one.__eq__(hotel_two))



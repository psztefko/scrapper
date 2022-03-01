from dataclasses import dataclass


@dataclass
class Whisky:
    name: str
    whisky_url: str
    image_url: str
    rating: float
    user_rating: float
    amount_of_user_ratings: int
    price: float

    def __init__(self, name: str,
                 whisky_url, image_url: str,
                 rating: float, user_rating: float,
                 amount_of_user_ratings: int,
                 price: float):
        self.name = name
        self.whisky_url = whisky_url
        self.image_url = image_url
        self.rating = rating
        self.user_rating = user_rating
        self.amount_of_user_ratings = amount_of_user_ratings
        self.price = price


    def __str__(self):
        return {
            "name": self.name,
            "whisky_url": self.whisky_url,
            "image_url": self.image_url,
            "rating": self.rating,
            "user_rating": self.user_rating,
            "amount_of_user_ratings": self.amount_of_user_ratings,
            "price": self.price
        }
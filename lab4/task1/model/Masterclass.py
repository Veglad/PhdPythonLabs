from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Masterclass:
    id: int
    name: str
    location: str
    base_price: Decimal
    datetime: datetime

    def __str__(self):
        return """
    ------------------------------
    {}
    ID: {}
    Location: {}
    At: {}
    ------------------------------
        """.format(self.id, self.name, self.location, self.datetime)

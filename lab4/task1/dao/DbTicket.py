from dataclasses import dataclass


@dataclass
class DbTicket:
    number: str
    type: str
    person_name: str
    master_class_id: int

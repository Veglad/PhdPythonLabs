from decimal import Decimal

from lab4.task1.model.Masterclass import Masterclass


class Ticket:
    def __init__(self, number: str, person_name: str, master_class: Masterclass):
        self.number = number
        self.person_name = person_name
        self.master_class = master_class

    def get_price(self):
        return self.master_class.base_price

    def __str__(self):
        return """
    ------------------------------
    {} #{} to {}
    Visitor: {}
    Price: {}
    Location: {}
    At: {}
    ------------------------------
        """.format(self.ticket_type(), self.number, self.master_class.name, self.person_name, self.get_price(),
                   self.master_class.location,
                   self.master_class.datetime)

    @staticmethod
    def ticket_type():
        return "Ticket"


class EarlyBirdTicket(Ticket):

    def __init__(self, number: str, person_name: str, master_class: Masterclass):
        super().__init__(number, person_name, master_class)

    def get_price(self):
        return self.master_class.base_price - self.master_class.base_price * Decimal('0.21')

    @staticmethod
    def ticket_type():
        return "Early Bird Ticket"


class NightOwlTicket(Ticket):

    def __init__(self, number: str, person_name: str, master_class: Masterclass):
        super().__init__(number, person_name, master_class)

    def get_price(self):
        return self.master_class.base_price + self.master_class.base_price * Decimal('0.29')

    @staticmethod
    def ticket_type():
        return "Night Owl Ticket"


class StudentTicket(Ticket):

    def __init__(self, number: str, person_name: str, master_class: Masterclass):
        super().__init__(number, person_name, master_class)

    def get_price(self):
        return self.master_class.base_price - self.master_class.base_price * Decimal('0.41')

    @staticmethod
    def ticket_type():
        return "Student Ticket"

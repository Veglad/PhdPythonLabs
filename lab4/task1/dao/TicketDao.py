import pickle
from typing import List

from lab4.task1.dao.DbTicket import DbTicket


class TicketDao:

    _storage_file_name = "./resources/ticket.pkl"

    def __init__(self):
        # tickets = [
        #     DbTicket("A1SADB", Ticket.ticket_type(), "Hugh Jackman", 1),
        #     DbTicket("B3E1SD", StudentTicket.ticket_type(), "Ivan Dudko", 1),
        #     DbTicket("B3531D", EarlyBirdTicket.ticket_type(), "Anna Lowec", 2),
        #     DbTicket("C3E1SD", NightOwlTicket.ticket_type(), "Vlad Shchehlov", 3),
        # ]
        self._load_from_file()


    def _save_to_file(self):
        with open(self._storage_file_name, 'wb') as f:
            pickle.dump(self._tickets, f)

    def _load_from_file(self):
        with open(self._storage_file_name, 'rb') as f:
            self._tickets = pickle.load(f)

    def get_by_number(self, number) -> DbTicket:
        db_ticket = self._tickets.get(number)

        if not db_ticket:
            raise Exception("Ticket with id {} is not found".format(number))

        return db_ticket

    def get_all(self) -> List[DbTicket]:
        return list(self._tickets.values())

    def save(self, ticket: DbTicket) -> DbTicket:
        self._tickets[ticket.number] = ticket
        self._save_to_file()
        return ticket

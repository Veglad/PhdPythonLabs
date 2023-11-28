import random
import string
from datetime import datetime
from typing import List

from lab4.task1.dao import TicketDao, MasterclassDao
from lab4.task1.dao.DbTicket import DbTicket
from lab4.task1.model.Ticket import (
    Ticket,
    StudentTicket,
    EarlyBirdTicket,
    NightOwlTicket
)


class TicketService:
    def __init__(self, ticket_dao: TicketDao, masterclass_dao: MasterclassDao):
        self.master_class_dao = masterclass_dao
        self.ticket_dao = ticket_dao
        self._ticket_types = {
            ticket_cls.ticket_type(): ticket_cls for ticket_cls in
            [Ticket, StudentTicket, EarlyBirdTicket, NightOwlTicket]
        }

    def get_by_number(self, number) -> Ticket:
        db_ticket = self.ticket_dao.get_by_number(number)
        return self._convert_to_ticket(db_ticket)

    def get_all(self) -> List[Ticket]:
        return list(map(lambda db: self._convert_to_ticket(db), self.ticket_dao.get_all()))

    def buy(self, person_name: str, master_class_id: int, student: bool) -> Ticket:
        number = self._generate_number()
        master_class = self.master_class_dao.get_by_id(master_class_id)
        days_before_mc = (master_class.datetime - datetime.now()).days

        if student:
            ticket = StudentTicket(number, person_name, master_class)
        elif days_before_mc >= 90:
            ticket = EarlyBirdTicket(number, person_name, master_class)
        elif days_before_mc >= 7:
            ticket = Ticket(number, person_name, master_class)
        elif days_before_mc >= 0:
            ticket = NightOwlTicket(number, person_name, master_class)
        else:
            raise Exception("Can't buy a ticket. Masterclass has already been started.")

        self.ticket_dao.save(self._convert_to_db_ticket(ticket))
        return self.get_by_number(number)

    def _convert_to_db_ticket(self, ticket: Ticket) -> DbTicket:
        return DbTicket(
            ticket.number,
            ticket.ticket_type(),
            ticket.person_name,
            ticket.master_class.id
        )

    def _convert_to_ticket(self, ticket: DbTicket) -> Ticket:
        ticket_class = self._get_ticket_class(ticket.type)
        return ticket_class(
            ticket.number,
            ticket.person_name,
            self.master_class_dao.get_by_id(ticket.master_class_id)
        )

    def _get_ticket_class(self, ticket_type) -> Ticket.__class__:
        ticket_cls = self._ticket_types.get(ticket_type)

        if not ticket_cls:
            raise Exception("Incorrect ticket type: {}".format(ticket_type))

        return ticket_cls

    @staticmethod
    def _generate_number():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

from typing import List

from lab4.task1.dao import MasterclassDao
from lab4.task1.model.Masterclass import Masterclass
from lab4.task1.model.Ticket import Ticket
from lab4.task1.service import TicketService


class TicketOffice:
    def __init__(self, ticket_service: TicketService, masterclass_dao: MasterclassDao):
        self.master_class_dao = masterclass_dao
        self.ticket_service = ticket_service

    def get_by_number(self, number) -> Ticket:
        return self.ticket_service.get_by_number(number)

    def get_all(self) -> List[Ticket]:
        return self.ticket_service.get_all()

    def buy_ticket(self, person_name: str, master_class_id: int, student: bool) -> Ticket:
        return self.ticket_service.buy(person_name, master_class_id, student)

    def get_all_master_classes(self) -> List[Masterclass]:
        return self.master_class_dao.get_all()

from TicketOfficeConsoleUI import TicketOfficeConsoleUI
from dao.MasterclassDao import MasterclassDao
from dao.TicketDao import TicketDao
from service.TicketOffice import TicketOffice
from service.TicketService import TicketService

if __name__ == '__main__':
    masterclass_dao = MasterclassDao()
    ticket_service = TicketService(TicketDao(), masterclass_dao)
    ticket_office = TicketOffice(ticket_service, masterclass_dao)
    application = TicketOfficeConsoleUI(ticket_office)
    application.start()

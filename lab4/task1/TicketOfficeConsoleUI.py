from lab4.task1.service.TicketOffice import TicketOffice


class TicketOfficeConsoleUI:
    def __init__(self, ticket_office: TicketOffice):
        self.ticket_office = ticket_office

    def start(self):

        while True:
            self._print_menu()
            key = input(">")
            if key == 'exit':
                print('Finishing...')
                return
            elif key.isdigit():
                self._handle_key(int(key))

    def _print_menu(self):
        print("""
---------------------------------------
|   Masterclasses Ticket Office App   |
---------------- Menu -----------------

[1] - Print all tickets
[2] - Find ticket by number
[3] - Buy a ticket
[4] - Print all masterclasses

Input "exit" to close...    

--------------------------------------
        """)

    def _handle_key(self, key: int):
        flows = {
            1: self._print_all_tickets,
            2: self._print_ticket_by_number,
            3: self._buy_a_ticket,
            4: self._print_all_master_classes,
        }
        flow_function = flows.get(key)
        if flow_function is not None:
            flow_function()
        else:
            print("Please, input correct key...")

    def _print_ticket_by_number(self):
        print("--- Find ticket by number ---")
        number = input("Input ticket number:")
        try:
            ticket = self.ticket_office.get_by_number(number)
            print(ticket)
        except Exception:
            print("Ticket is not found.")

    def _print_all_tickets(self):
        print("--- Print all tickets ---")
        for ticket in self.ticket_office.get_all():
            print(ticket.__str__())

    def _buy_a_ticket(self):
        print("--- Buy a ticket ---")

        person_name = input("Input visitor name:")
        master_class_id = self._get_int("Masterclass ID: ")
        student_response = input("Are you student? Y - yes, any key - no:")

        try:
            ticket = self.ticket_office.buy_ticket(person_name, master_class_id, student_response == 'Y')
            print(ticket)
        except Exception as e:
            print("Can't buy a ticket: {}", e)

    def _print_all_master_classes(self):
        print("--- Print all master classes ---")
        for masterclass in self.ticket_office.get_all_master_classes():
            print(masterclass)

    @staticmethod
    def _get_int(message):
        while True:
            master_class_id = input(message)
            if master_class_id.isdigit():
                return int(master_class_id)

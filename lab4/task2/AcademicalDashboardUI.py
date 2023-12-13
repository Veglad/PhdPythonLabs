from lab4.task2.AcademicalDashboardService import AcademicalDashboardService


class AcademicalDashboardUI:
    def __init__(self, service: AcademicalDashboardService):
        self._service = service

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
|        Academical Dashboard         |
---------------- Menu -----------------

[1] - Print all students
[2] - Print all groups
[3] - Print all subjects
[4] - Print all lecturers

Input "exit" to close...    

--------------------------------------
        """)

    def _handle_key(self, key: int):
        flows = {
            1: self._print_all_students,
            2: self._print_all_groups,
            3: self._print_all_subjects,
            4: self._print_all_lecturers,
        }
        flow_function = flows.get(key)
        if flow_function is not None:
            flow_function()
        else:
            print("Please, input correct key...")

    def _print_all_students(self):
        print("--- Print all students ---")
        for student in self._service.get_students():
            print(student)

    def _print_all_groups(self):
        print("--- Print all groups ---")
        for group in self._service.get_groups():
            print(group)

    def _print_all_subjects(self):
        print("--- Print all subjects ---")
        for subject in self._service.get_subjects():
            print(subject)

    def _print_all_lecturers(self):
        print("--- Print all lecturers ---")
        for lecturer in self._service.get_lecturers():
            print(lecturer)

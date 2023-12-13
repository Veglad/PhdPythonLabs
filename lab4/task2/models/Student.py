from decimal import Decimal

from lab4.task2.models.Person import Person


class Student(Person):

    def __init__(self, first_name: str, last_name: str, middle_name: str, birth_year: int, application_year: int):
        super().__init__(first_name, last_name, middle_name, birth_year)
        self._application_year = application_year

    @property
    def application_year(self):
        return self._application_year

    @application_year.setter
    def application_year(self, value):
        self._application_year = value

    def _university_info(self):
        return {"Application year": self.application_year}

    def __str__(self):
        university_info_text = " | ".join(["{} - {}".format(key, value) for key, value in self._university_info().items()])
        return """
----------Student-------------
Name - {}
Birth year - {}
-- University info -- 
{}
------------------------------
        """.format(self.full_name(), self.birth_year, university_info_text)

    @staticmethod
    def type():
        return "Student"


class StateFundedStudent(Student):

    def __init__(self, first_name: str, last_name: str, middle_name: str,
                 birth_year: int, application_year: int, scholarship: Decimal):
        super().__init__(first_name, last_name, middle_name, birth_year, application_year)
        self._scholarship = scholarship

    @property
    def scholarship(self):
        return self._scholarship

    @scholarship.setter
    def scholarship(self, value):
        self._scholarship = value

    def _university_info(self):
        info = super()._university_info()
        info["Scholarship"] = self.scholarship
        return info

    @staticmethod
    def type():
        return "StateFundedStudent"

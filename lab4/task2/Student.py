from decimal import Decimal


class Student:

    def __init__(self, first_name: str, last_name: str, middle_name: str):
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value


class StateFundedStudent(Student):

    def __init__(self, first_name: str, last_name: str, middle_name: str, scholarship: Decimal):
        super().__init__(first_name, last_name, middle_name)
        self._scholarship = scholarship

    @property
    def scholarship(self):
        return self._scholarship

    @scholarship.setter
    def scholarship(self, value):
        self._scholarship = value

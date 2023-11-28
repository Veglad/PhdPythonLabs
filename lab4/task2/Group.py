from typing import List

from Student import Student


class Group:

    def __init__(self, number: str, students: List[Student]):
        self._number = number
        self._students = students

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, value):
        self._students = value

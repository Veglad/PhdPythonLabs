from typing import List

from Subject import Subject


class Lecturer:

    def __init__(self, first_name: str, last_name: str, middle_name: str, birth_year: int, experience: float,
                 subjects: List[Subject]):
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._birth_year = birth_year
        self._experience = experience
        self._subjects = subjects

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

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        self._birth_year = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        self._subjects = value

    def total_subject

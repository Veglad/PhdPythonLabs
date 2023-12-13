import pickle
from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class DbStudent:
    id: int
    first_name: str
    last_name: str
    middle_name: str
    birth_year: int
    application_year: int
    group_number: str
    student_type: str
    scholarship: Decimal


class StudentDao:
    _storage_file_name = "./resources/student.pkl"

    def __init__(self):
        self._load_from_file()

    def _save_to_file(self):
        with open(self._storage_file_name, 'wb') as f:
            pickle.dump(self._students, f)

    def _load_from_file(self):
        with open(self._storage_file_name, 'rb') as f:
            self._students = pickle.load(f)

    def get_by_id(self, number) -> DbStudent:
        student = self._students.get(number)

        if not student:
            raise Exception("Student with id {} is not found".format(number))

        return student

    def get_all(self) -> List[DbStudent]:
        return list(self._students.values())

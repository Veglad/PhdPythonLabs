import pickle
from dataclasses import dataclass
from typing import List


@dataclass
class DbLecturer:
    id: int
    first_name: str
    last_name: str
    middle_name: str
    birth_year: int
    teaching_experience: float


class LecturerDao:
    _storage_file_name = "./resources/lecturer.pkl"

    def __init__(self):
        self._load_from_file()

    def _save_to_file(self):
        with open(self._storage_file_name, 'wb') as f:
            pickle.dump(self._lecturers, f)

    def _load_from_file(self):
        with open(self._storage_file_name, 'rb') as f:
            self._lecturers = pickle.load(f)

    def get_by_name(self, name) -> DbLecturer:
        lecturer = self._lecturers.get(name)

        if not lecturer:
            raise Exception("Subject with name {} is not found".format(name))

        return lecturer

    def get_all(self) -> List[DbLecturer]:
        return list(self._lecturers.values())

import pickle
from dataclasses import dataclass
from typing import List


@dataclass
class DbSubject:
    name: str
    credits: float
    semester: int
    lecturer_id: int


class SubjectDao:
    _storage_file_name = "./resources/subject.pkl"

    def __init__(self):
        self._load_from_file()

    def _save_to_file(self):
        with open(self._storage_file_name, 'wb') as f:
            pickle.dump(self._subjects, f)

    def _load_from_file(self):
        with open(self._storage_file_name, 'rb') as f:
            self._subjects = pickle.load(f)

    def get_by_name(self, name) -> DbSubject:
        subject = self._subjects.get(name)

        if not subject:
            raise Exception("Subject with name {} is not found".format(name))

        return subject

    def get_all(self) -> List[DbSubject]:
        return list(self._subjects.values())

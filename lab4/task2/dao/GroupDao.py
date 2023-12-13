import pickle
from dataclasses import dataclass
from typing import List


@dataclass
class DbGroup:
    number: str


class GroupDao:
    _storage_file_name = "./resources/group.pkl"

    def __init__(self):
        self._load_from_file()

    def _save_to_file(self):
        with open(self._storage_file_name, 'wb') as f:
            pickle.dump(self._groups, f)

    def _load_from_file(self):
        with open(self._storage_file_name, 'rb') as f:
            self._groups = pickle.load(f)

    def get_by_number(self, number) -> DbGroup:
        group = self._groups.get(number)

        if not group:
            raise Exception("Group with number {} is not found".format(number))

        return group

    def get_all(self) -> List[DbGroup]:
        return list(self._groups.values())

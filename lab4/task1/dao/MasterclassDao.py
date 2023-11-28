import pickle
from typing import List

from lab4.task1.model.Masterclass import Masterclass


class MasterclassDao:

    _storage_file_name = "./resources/masterclass.pkl"

    def __init__(self):
        # master_classes = [
        #     Masterclass(1, "Soccer professional day", "Kyiv, Olimpiyskiy Stadium", Decimal("900"),
        #                 datetime.strptime("21.11.2023 10:30", "%d.%m.%Y %H:%M")),
        #     Masterclass(2, "Twerk master class", "Kharkiv, KhATOB", Decimal("900"),
        #                 datetime.strptime("25.11.2023 16:30", "%d.%m.%Y %H:%M")),
        #     Masterclass(3, "Swimming freestyle", "Odesa, Nemo hotel", Decimal("900"),
        #                 datetime.strptime("15.12.2023 11:00", "%d.%m.%Y %H:%M")),
        # ]
        self._load_from_file()

    def _save_to_file(self):
        with open(self._storage_file_name, 'wb') as f:
            pickle.dump(self._master_classes, f)

    def _load_from_file(self):
        with open(self._storage_file_name, 'rb') as f:
            self._master_classes = pickle.load(f)

    def get_by_id(self, mc_id) -> Masterclass:
        master_class = self._master_classes.get(mc_id)
        if not master_class:
            raise Exception("Masterclass with id {} is not found".format(mc_id))
        return master_class

    def get_all(self) -> List[Masterclass]:
        return list(self._master_classes.values())

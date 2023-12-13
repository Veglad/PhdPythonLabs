from typing import List

from lab4.task2.models.Subject import Subject
from lab4.task2.models.Person import Person


class Lecturer(Person):

    def __init__(self, first_name: str, last_name: str, middle_name: str, birth_year: int,
                 teaching_experience: float, subjects: List[Subject]):
        super().__init__(first_name, last_name, middle_name, birth_year)
        self._teaching_experience = teaching_experience
        self._subjects = subjects

    @property
    def teaching_experience(self):
        return self._teaching_experience

    @teaching_experience.setter
    def teaching_experience(self, value):
        self._teaching_experience = value

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        self._subjects = value

    # returns sum of all subject credits
    def total_subject(self):
        if self._subjects is None:
            return 0
        else:
            return sum(map(lambda sub: sub.credits, self._subjects))

    def _university_info(self):
        subjects_text = " | ".join(map(lambda s: s.name, self.subjects))
        return {
            "Teaching experience": self.teaching_experience,
            "Total subject credits": self.total_subject(),
            "Subjects": subjects_text
        }

    def __str__(self):
        university_info_text = "\n".join(["{} - {}".format(key, value) for key, value in self._university_info().items()])
        return """
----------Lecturer-------------
Name - {}
Birth year - {}
-- University info -- 
{}
------------------------------
        """.format(self.full_name(), self.birth_year, university_info_text)

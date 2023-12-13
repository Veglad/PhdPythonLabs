class Subject:

    def __init__(self, name: str, credits: float, semester: int):
        self._semester = semester
        self._credits = credits
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        self._credits = value

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = value

    def __str__(self):
        return """
----------Subject-------------
Name - {}
Credits - {}
Semester - {}
------------------------------
        """.format(self.name, self.credits, self.semester)

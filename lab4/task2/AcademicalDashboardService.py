import itertools
from typing import List

from lab4.task2.dao import GroupDao, LecturerDao, SubjectDao, StudentDao
from lab4.task2.dao.GroupDao import DbGroup
from lab4.task2.dao.LecturerDao import DbLecturer
from lab4.task2.dao.StudentDao import DbStudent
from lab4.task2.dao.SubjectDao import DbSubject
from lab4.task2.models.Group import Group
from lab4.task2.models.Lecturer import Lecturer
from lab4.task2.models.Student import Student, StateFundedStudent
from lab4.task2.models.Subject import Subject


class AcademicalDashboardService:
    def __init__(self, group_dao: GroupDao, lecturer_dao: LecturerDao, subject_dao: SubjectDao,
                 student_dao: StudentDao):
        self._group_dao = group_dao
        self._lecturer_dao = lecturer_dao
        self._subject_dao = subject_dao
        self._student_dao = student_dao

    def get_students(self) -> List[Student]:
        return list(map(self._db_student_to_dto, self._student_dao.get_all()))

    def get_groups(self) -> List[Group]:
        students = self._student_dao.get_all()
        group = itertools.groupby(students, lambda s: s.group_number)
        students_by_group = {
            group_id: list(map(self._db_student_to_dto, list(students)))
            for group_id, students in group
        }
        return list(map(lambda it: self._db_group_to_dto(it, students_by_group[it.number]), self._group_dao.get_all()))

    def get_subjects(self) -> List[Subject]:
        return list(map(self._db_subject_to_dto, self._subject_dao.get_all()))

    def get_lecturers(self) -> List[Lecturer]:
        subjects = self._subject_dao.get_all()
        group = itertools.groupby(subjects, lambda s: s.lecturer_id)
        subjects_by_lecturer = {
            lecturer_id: list(map(self._db_subject_to_dto, list(subjects)))
            for lecturer_id, subjects in group
        }
        return list(map(lambda it: self._db_lecturer_to_dto(it, subjects_by_lecturer[it.id]), self._lecturer_dao.get_all()))

    def _db_subject_to_dto(self, db: DbSubject) -> Subject:
        return Subject(db.name, db.credits, db.semester)

    def _db_student_to_dto(self, db: DbStudent) -> Student:
        if db.student_type == Student.type():
            return Student(db.first_name, db.last_name, db.middle_name, db.birth_year, db.application_year)
        elif db.student_type == StateFundedStudent.type():
            return StateFundedStudent(db.first_name, db.last_name, db.middle_name, db.birth_year, db.application_year,
                                      db.scholarship)

    def _db_group_to_dto(self, db: DbGroup, students: List[Student]) -> Group:
        return Group(db.number, students)

    def _db_lecturer_to_dto(self, db: DbLecturer, subjects: List[Subject]) -> Lecturer:
        return Lecturer(
            db.first_name,
            db.last_name,
            db.middle_name,
            db.birth_year,
            db.teaching_experience,
            subjects
        )

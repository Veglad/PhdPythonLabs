from lab4.task2.AcademicalDashboardService import AcademicalDashboardService
from lab4.task2.AcademicalDashboardUI import AcademicalDashboardUI
from lab4.task2.dao.GroupDao import GroupDao
from lab4.task2.dao.LecturerDao import LecturerDao
from lab4.task2.dao.StudentDao import StudentDao
from lab4.task2.dao.SubjectDao import SubjectDao

if __name__ == '__main__':
    group_dao = GroupDao()
    student_dao = StudentDao()
    subject_dao = SubjectDao()
    lecturer_dao = LecturerDao()
    service = AcademicalDashboardService(group_dao, lecturer_dao, subject_dao, student_dao)
    application = AcademicalDashboardUI(service)
    application.start()

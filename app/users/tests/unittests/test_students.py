import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import StudentRepository, UserRepository


class TestStudentRepo(TestClass):
    def create_students_for_methods(self):
        with TestingSessionLocal() as db:
            student_repository = StudentRepository(db)
            user_repository = UserRepository(db)
            user1 = user_repository.create_user("mihajlo1@gmail.com", "sifra123")
            user2 = user_repository.create_user("mihajlo2@gmail.com", "sifra123")
            user3 = user_repository.create_user("mihajlo3@gmail.com", "sifra123")
            user4 = user_repository.create_user("mihajlo4@gmail.com", "sifra123")
            student1 = student_repository.create_student("123", "name1", "pname", "123904141", "address", user1.id)
            student2 = student_repository.create_student("431", "name2", "pname", "123904141", "address", user2.id)
            student3 = student_repository.create_student("432", "name3", "pname", "123904141", "address", user3.id)
            student4 = student_repository.create_student("436", "name4", "pname", "123904141", "address", user4.id)

    def test_create_student(self):
        with TestingSessionLocal() as db:
            student_repository = StudentRepository(db)
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo@gmail.com", "sifra123")
            student = student_repository.create_student("123", "name1", "pname", "123904141", "address", user.id)
            assert student.index == "123"
            assert student.user_id == user.id
            assert student.name == "name1"
            assert student.parent_name == "pname"
            assert student.telephone_number == "123904141"
            assert student.address == "address"


    def test_create_student_error(self):
        with TestingSessionLocal() as db:
            student_repository = StudentRepository(db)
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo@gmail.com", "sifra123")
            student = student_repository.create_student("123", "name1", "pname", "123904141", "address", user.id)
            assert not student.index != "123"
            assert not student.user_id != user.id
            assert not student.name != "name1"
            assert not student.parent_name != "pname"
            assert not student.telephone_number != "123904141"
            assert not student.address != "address"
            with pytest.raises(IntegrityError) as e:
                student1 = student_repository.create_student("123", "name1", "pname", "123904141", "address", user.id)

    def test_get_user_by_id(self):
        with TestingSessionLocal() as db:
            student_repository = StudentRepository(db)
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo@gmail.com", "sifra123")
            student = student_repository.create_student("123", "name1", "pname", "123904141", "address", user.id)
            student1 = student_repository.get_student_by_id(student.id)

            assert student == student1

    def test_get_user_by_id_error(self):
        with TestingSessionLocal() as db:
            student_repository = StudentRepository(db)
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo@gmail.com", "sifra123")
            student = student_repository.create_student("123", "name1", "pname", "123904141", "address", user.id)
            student1 = student_repository.get_student_by_id(student.id)

            assert not student != student1

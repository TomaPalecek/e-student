from app.db.database import SessionLocal
from app.users.repository.student_repository import StudentRepository


class StudentServices:
    @staticmethod
    def create_student(index, name, parent_name, telephone_number, address, user_id):
        with SessionLocal() as db:
            try:
                student_repository = StudentRepository(db)
                return student_repository.create_student(index, name, parent_name, telephone_number, address, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_student_by_id(student_id: str):
        with SessionLocal() as db:
            try:
                student_repository = StudentRepository(db)
                return student_repository.get_student_by_id(student_id=student_id)
            except Exception as e:
                raise e

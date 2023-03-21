from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import Student


class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, index, name, parent_name, telephone_number, address, user_id):
        try:
            student = Student(index, name, parent_name, telephone_number, address, user_id)
            self.db.add(student)
            self.db.commit()
            self.db.refresh(student)
            return student

        except IntegrityError as e:
            raise e

    def get_student_by_id(self, student_id: str):
        student = self.db.query(Student).filter(Student.id == student_id).first()
        return student

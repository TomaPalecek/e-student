from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.users.services import StudentServices


class StudentController:
    @staticmethod
    def create_student(index, name, parent_name, telephone_number, address, user_id):
        try:
            student = StudentServices.create_student(index, name, parent_name, telephone_number, address, user_id)
            return student
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Student with provided index, {index}, already exist.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="Some error happened, call backend eng. and f him.",
            )

    @staticmethod
    def get_student_by_id(student_id: str):
        try:
            return StudentServices.get_student_by_id(student_id=student_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import *
from app.users.models import EmployeeType


class EmployeeTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee_type(self, employee_type):
        try:
            employee_type = EmployeeType(employee_type)
            self.db.add(employee_type)
            self.db.commit()
            self.db.refresh(employee_type)
            return employee_type
        except IntegrityError as e:
            raise e

    def read_employee_type_by_id(self, employee_type_id: str):
        employee_type = self.db.query(EmployeeType).filter(EmployeeType.id == employee_type_id).first()
        if employee_type is None:
            raise EmployeeTypeNotFoundException(f"Employee type with provided ID: {employee_type_id} not found.", 400)
        return employee_type

    def read_employee_type_by_type(self, employee_type: str):
        e_type = self.db.query(EmployeeType).filter(EmployeeType.employee_type == employee_type).first()
        return e_type

    def read_all_employee_types(self):
        employee_types = self.db.query(EmployeeType).all()
        return employee_types

    def delete_employee_type_by_id(self, employee_type_id: str):
        try:
            employee_type = self.db.query(EmployeeType).filter(EmployeeType.id == employee_type_id).first()
            if employee_type is None:
                raise EmployeeTypeNotFoundException(
                    f"Employee type with provided ID: {employee_type_id} not found.",
                    400,
                )
            self.db.delete(employee_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee_type(self, employee_type_id: str, employee_type: str):
        try:
            e_type = self.db.query(EmployeeType).filter(EmployeeType.id == employee_type_id).first()
            if e_type is None:
                raise EmployeeTypeNotFoundException(
                    f"Employee type with provided ID: {employee_type_id} not found.",
                    400,
                )
            e_type.employee_type = employee_type
            self.db.add(e_type)
            self.db.commit()
            self.db.refresh(e_type)
            return e_type
        except Exception as e:
            raise e

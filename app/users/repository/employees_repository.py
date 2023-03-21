from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import *
from app.users.models import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, name, last_name, employee_type_id):
        try:
            employee = Employee(name, last_name, employee_type_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def get_employee_by_id(self, employee_id: str):
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(f"Employee with provided ID: {employee_id} not found.", 400)
        return employee

    def get_employees_by_characters(self, characters: str):
        employees = self.db.query(Employee).filter(Employee.name.like(characters + "%")).all()
        if employees is None:
            raise EmployeeNotFoundException(f"Employee with provided characters: {characters} not found.", 400)
        return employees

    def get_employees_by_employee_type_id(self, employee_type_id: str):
        employees = self.db.query(Employee).filter(Employee.employee_type_id == employee_type_id).first()
        if employees is None:
            raise EmployeeNotFoundException(
                f"Employee with provided employee type id: {employee_type_id} not found.",
                400,
            )
        return employees

    def get_all_employees(self):
        employee = self.db.query(Employee).all()
        return employee

    def delete_employee_by_id(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided ID: {employee_id} not found.", 400)
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee(
        self,
        employee_id: str,
        name: str = None,
        last_name: str = None,
        employee_type_id: str = None,
    ):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided ID: {employee_id} not found.", 400)
            if name is not None:
                employee.name = name
            if last_name is not None:
                employee.last_name = last_name
            if employee_type_id is not None:
                employee.employee_type_id = employee_type_id
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e

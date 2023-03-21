from app.db.database import SessionLocal
from app.users.repository.employees_repository import EmployeeRepository


class EmployeeServices:
    @staticmethod
    def create_employee(name, last_name, employee_type_id):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create_employee(name, last_name, employee_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_employees_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employees_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_employees_by_employee_type_id(employee_type_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_employees_by_employee_type_id(employee_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employees():
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.get_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee_repository.delete_employee_by_id(employee_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_employee(
        employee_id: str,
        name: str = None,
        last_name: str = None,
        employee_type_id: str = None,
    ):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.update_employee(employee_id, name, last_name, employee_type_id)
        except Exception as e:
            raise e

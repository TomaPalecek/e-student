from app.db.database import SessionLocal
from app.users.exceptions import *
from app.users.repository.employee_type_repository import EmployeeTypeRepository


class EmployeeTypeServices:
    @staticmethod
    def create_employee_type(employee_type):
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                e_type = employee_type_repository.read_employee_type_by_type(employee_type)
                if e_type is None:
                    return employee_type_repository.create_employee_type(employee_type)
                raise EmployeeTypeExistsException(message="Type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_employee_type_by_id(employee_type_id: str):
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                return employee_type_repository.read_employee_type_by_id(employee_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employee_types():
        with SessionLocal() as db:
            employee_type_repository = EmployeeTypeRepository(db)
            return employee_type_repository.read_all_employee_types()

    @staticmethod
    def delete_employee_type_by_id(employee_type_id: str):
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                employee_type_repository.delete_employee_type_by_id(employee_type_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_employee_type(employee_type_id: str, employee_type: str):
        try:
            with SessionLocal() as db:
                employee_type_repository = EmployeeTypeRepository(db)
                return employee_type_repository.update_employee_type(employee_type_id, employee_type)
        except Exception as e:
            raise e

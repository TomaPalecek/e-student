from fastapi import HTTPException, Response, status

from app.users.exceptions import *
from app.users.services import EmployeeServices, EmployeeTypeServices


class EmployeeController:
    @staticmethod
    def create_employee(name, last_name, employee_type_id):
        try:
            EmployeeTypeServices.get_employee_type_by_id(employee_type_id)
            employee = EmployeeServices.create_employee(name, last_name, employee_type_id)
            return employee
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_by_id(employee_id: str):
        employee = EmployeeServices.get_employee_by_id(employee_id)
        if employee:
            return employee
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Employee with provided id {employee_id} does not exist",
        )

    @staticmethod
    def get_employees_by_characters(characters: str):
        employees = EmployeeServices.get_employees_by_characters(characters)
        if employees:
            return employees
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Employee with provided characters {characters} does not exist",
        )

    @staticmethod
    def get_employees_by_employee_type_id(employee_type_id: str):
        employees = EmployeeServices.get_employees_by_employee_type_id(employee_type_id)
        if employees:
            return employees
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Employee with provided employee type id {employee_type_id} does not exist",
        )

    @staticmethod
    def get_all_employees():
        employee = EmployeeServices.get_all_employees()
        return employee

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            EmployeeServices.delete_employee_by_id(employee_id)
            return Response(content=f"Employee with id - {employee_id} is deleted")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_employee(
        employee_id: str,
        name: str = None,
        last_name: str = None,
        employee_type_id: str = None,
    ):
        try:
            employee = EmployeeServices.update_employee(employee_id, name, last_name, employee_type_id)
            return employee
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

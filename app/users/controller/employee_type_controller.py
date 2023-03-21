from fastapi import HTTPException, Response

from app.users.exceptions import *
from app.users.services import EmployeeTypeServices


class EmployeeTypeController:
    @staticmethod
    def create_employee_type(employee_type):
        try:
            e_type = EmployeeTypeServices.create_employee_type(employee_type)
            return e_type

        except EmployeeTypeExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_type_by_id(employee_type_id: str):
        try:
            employee_type = EmployeeTypeServices.get_employee_type_by_id(employee_type_id)
            if employee_type:
                return employee_type
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_type_by_type_name(employee_type_name: str):
        try:
            employee_type = EmployeeTypeServices.get_employee_type_by_id(employee_type_name)
            if employee_type:
                return employee_type
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_employee_types():
        employee_types = EmployeeTypeServices.get_all_employee_types()
        return employee_types

    @staticmethod
    def delete_employee_type_by_id(employee_type_id: str):
        try:
            EmployeeTypeServices.delete_employee_type_by_id(employee_type_id)
            return Response(content=f"Employee type with id - {employee_type_id} is deleted")
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_employee_type(employee_type_id: str, employee_type: str):
        try:
            e_type = EmployeeTypeServices.update_employee_type(employee_type_id, employee_type)
            return e_type
        except EmployeeTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

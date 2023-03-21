from fastapi import HTTPException, Response

from app.faculties.exceptions import FacultyExceptionCode, FacultyNotFoundException
from app.faculties.services import FacultyService


class FacultyController:
    @staticmethod
    def create_new_faculty(address: str, city: str, name: str, acronym: str):
        try:
            faculty = FacultyService.create_new_faculty(address, city, name, acronym)
            return faculty
        except FacultyExceptionCode as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_faculties():
        faculties = FacultyService.read_all_faculties()
        return faculties

    @staticmethod
    def get_faculty_by_id(faculty_id: str):
        try:
            faculty = FacultyService.read_faculty_by_id(faculty_id)
            return faculty
        except FacultyNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_faculty_by_id(faculty_id: str):
        try:
            FacultyService.delete_faculty_by_id(faculty_id)
            return Response(
                content=f"Faculty with provided ID: {faculty_id} deleted.",
                status_code=200,
            )
        except FacultyNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_faculty_by_acronym(faculty_acronym: str):
        try:
            faculty = FacultyService.read_faculty_by_acronym(faculty_acronym)
            return faculty
        except FacultyNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_faculty_by_city(city: str):
        try:
            faculty = FacultyService.read_faculty_by_city(city)
            return faculty
        except FacultyNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_faculty_by_name(name: str):
        try:
            faculty = FacultyService.read_faculty_by_name(name)
            return faculty
        except FacultyNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_faculty_by_name_or_city(namecity: str):
        try:
            faculty = FacultyService.read_faculty_by_name_or_city(namecity)
            return faculty
        except FacultyNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

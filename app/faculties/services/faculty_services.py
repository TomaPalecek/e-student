from sqlalchemy.exc import IntegrityError

from app.db import SessionLocal
from app.faculties.exceptions import FacultyExceptionCode
from app.faculties.models import Faculty
from app.faculties.repositories import FacultyRepository


class FacultyService:
    @staticmethod
    def create_new_faculty(address: str, city: str, name: str, acronym: str) -> FacultyExceptionCode or Faculty:
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                faculty = repository.read_faculty_by_acronym(acronym)
                if bool(faculty) is False:
                    return repository.create_faculty(address, city, name, acronym)
                raise FacultyExceptionCode(message="Acronym already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_faculties():
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.read_all_faculties()
        except Exception as e:
            raise e

    @staticmethod
    def read_faculty_by_id(faculty_id: str):
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.read_faculty_by_id(faculty_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_faculty_by_id(faculty_id: str):
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.delete_faculty(faculty_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_faculty_by_acronym(acronym: str) -> FacultyExceptionCode or Faculty:
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.read_faculty_by_acronym(acronym)
        except Exception as e:
            raise e

    @staticmethod
    def read_faculty_by_city(city: str):
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.read_faculty_by_city(city)
        except Exception as e:
            raise e

    @staticmethod
    def read_faculty_by_name(name: str):
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.read_faculty_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def read_faculty_by_name_or_city(namecity: str):
        try:
            with SessionLocal() as db:
                repository = FacultyRepository(db)
                return repository.read_faculty_by_name_or_city(namecity)
        except Exception as e:
            raise e

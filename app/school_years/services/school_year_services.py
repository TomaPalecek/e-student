from sqlalchemy.exc import IntegrityError

from app.db import SessionLocal
from app.school_years.exceptions import SchoolYearExceptionName
from app.school_years.models import SchoolYear
from app.school_years.repositories import SchoolYearRepository


class SchoolYearService:
    @staticmethod
    def create_new_school_year(name, start, end):
        try:
            with SessionLocal() as db:
                repository = SchoolYearRepository(db)
                course = repository.read_school_year_by_name(name)
                if course is None:
                    return repository.create_school_year(name, start, end)
                raise SchoolYearExceptionName(message="School year already exists in the database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_school_years():
        try:
            with SessionLocal() as db:
                repository = SchoolYearRepository(db)
                return repository.read_all_school_years()
        except Exception as e:
            raise e

    @staticmethod
    def read_school_year_by_skg(school_year_skg):
        try:
            with SessionLocal() as db:
                repository = SchoolYearRepository(db)
                return repository.read_school_year_by_skg(school_year_skg)
        except Exception as e:
            raise e

    @staticmethod
    def delete_school_year_by_skg(school_year_skg):
        try:
            with SessionLocal() as db:
                repository = SchoolYearRepository(db)
                return repository.delete_school_year(school_year_skg)
        except Exception as e:
            raise e

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.school_years.exceptions import SchoolYearNotFoundException
from app.school_years.models import SchoolYear


class SchoolYearRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_school_year(self, name: str, start: str, end: str):
        try:
            school_year = SchoolYear(name, start, end)
            self.db.add(school_year)
            self.db.commit()
            self.db.refresh(school_year)
            return school_year
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_school_years(self):
        school_years = self.db.query(SchoolYear).all()
        return school_years

    def read_school_year_by_skg(self, school_year_skg: str):
        school_year = self.db.query(SchoolYear).filter(SchoolYear.skg == school_year_skg).first()
        if school_year is None:
            raise SchoolYearNotFoundException(f"School year with provided SKG: {school_year_skg} not found.", 400)
        return school_year

    def delete_school_year(self, school_year_skg: str):
        try:
            school_year = self.db.query(SchoolYear).filter(SchoolYear.skg == school_year_skg).first()
            if school_year is None:
                raise SchoolYearNotFoundException(f"School year with provided SKG: {school_year_skg} not found.", 400)
            self.db.delete(school_year)
            self.db.commit()
            # self.db.refresh(course)
            return True
        except Exception as e:
            raise e

    def read_school_year_by_name(self, name: str):
        course = self.db.query(SchoolYear).filter(SchoolYear.name == name).first()
        return course

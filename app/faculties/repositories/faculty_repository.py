from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.faculties.exceptions import FacultyNotFoundException
from app.faculties.models import Faculty


class FacultyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_faculty(self, address: str, city: str, name: str, acronym: str):
        try:
            faculty = Faculty(address, city, name, acronym)
            self.db.add(faculty)
            self.db.commit()
            self.db.refresh(faculty)
            return faculty
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_faculties(self):
        faculties = self.db.query(Faculty).all()
        return faculties

    def read_faculty_by_id(self, faculty_id: str):
        faculty = self.db.query(Faculty).filter(Faculty.id == faculty_id).first()
        if faculty is None:
            raise FacultyNotFoundException(f"Faculty with provided ID: {faculty_id} not found.", 400)
        return faculty

    def delete_faculty(self, faculty_id: str):
        try:
            faculty = self.db.query(Faculty).filter(Faculty.id == faculty_id).first()
            if faculty is None:
                raise FacultyNotFoundException(f"Faculty with provided ID: {faculty_id} not found.", 400)
            self.db.delete(faculty)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def read_faculty_by_acronym(self, faculty_acronym: str):
        faculty = self.db.query(Faculty).filter(Faculty.acronym.ilike(f"%{faculty_acronym}%")).all()

        return faculty

    def read_faculty_by_city(self, city: str):
        faculty = self.db.query(Faculty).filter(Faculty.city.ilike(f"%{city}%")).all()
        return faculty

    def read_faculty_by_name(self, name: str):
        faculty = self.db.query(Faculty).filter(Faculty.name.ilike(f"%{name}%")).all()
        return faculty

    def read_faculty_by_name_or_city(self, namecity: str):
        faculty = self.db.query(Faculty).filter(Faculty.name.ilike(f"%{namecity}%")).all()
        return faculty

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.study_programmes.exceptions import StudyProgrammeNotFoundException
from app.study_programmes.models import StudyProgramme


class StudyProgrammeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_study_programme(self, full_name: str, abbreviation: str, duration: int):
        try:
            study_programme = StudyProgramme(full_name, abbreviation, duration)
            self.db.add(study_programme)
            self.db.commit()
            self.db.refresh(study_programme)
            return study_programme
        except IntegrityError as e:
            raise e

    def get_all_study_programmes(self):
        study_programmes = self.db.query(StudyProgramme).all()
        return study_programmes

    def get_study_programme_by_id(self, study_programme_id: str):
        study_programme = self.db.query(StudyProgramme).filter(StudyProgramme.id == study_programme_id).first()
        return study_programme

    def get_study_programme_by_abbreviation(self, abbreviation: str):
        study_programme = self.db.query(StudyProgramme).filter(StudyProgramme.abbreviation == abbreviation).first()
        return study_programme

    def get_study_programme_by_full_name(self, full_name: str):
        study_programme = self.db.query(StudyProgramme).filter(StudyProgramme.full_name == full_name).first()
        return study_programme

    def delete_study_programme_by_id(self, study_programme_id: str):
        try:
            study_programme = self.db.query(StudyProgramme).filter(StudyProgramme.id == study_programme_id).first()
            if study_programme is None:
                raise StudyProgrammeNotFoundException(code=400, message="Study programme not found")
            self.db.delete(study_programme)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_study_programme(self):
        pass

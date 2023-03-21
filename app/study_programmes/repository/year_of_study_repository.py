from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.study_programmes.exceptions.year_of_study_exceptions import YearOfStudyNotFoundException
from app.study_programmes.models import YearOfStudy


class YearOfStudyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_year_of_study(self, year_of_study: int, study_programme_id: str):
        try:
            year_of_stdy = YearOfStudy(year_of_study, study_programme_id)
            self.db.add(year_of_stdy)
            self.db.commit()
            self.db.refresh(year_of_stdy)
            return year_of_stdy
        except IntegrityError as e:
            raise e

    def get_all_years_of_study(self):
        return self.db.query(YearOfStudy).all()

    def get_year_of_study_by_id(self, year_of_study_id: str):
        return self.db.query(YearOfStudy).filter(YearOfStudy.id == year_of_study_id).first()

    def get_year_of_study_by_study_programme_id(self, study_programme_id: str):
        return self.db.query(YearOfStudy).filter(YearOfStudy.study_programme_id == study_programme_id).first()

    def delete_year_of_study_by_id(self, year_of_study_id: str):
        try:
            year_of_study = self.db.query(YearOfStudy).filter(YearOfStudy.id == year_of_study_id).first()
            if year_of_study is None:
                raise YearOfStudyNotFoundException(
                    code=400,
                    message=f"Year of study with ID {year_of_study_id} not found",
                )
            self.db.delete(year_of_study)
            self.db.commit()
            return True
        except Exception as e:
            raise e

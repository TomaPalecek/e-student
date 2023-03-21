from sqlalchemy.exc import IntegrityError

from app.db import SessionLocal
from app.study_programmes.exceptions.year_of_study_exceptions import YearOfStudyOutOfBoundsException
from app.study_programmes.repository import StudyProgrammeRepository, YearOfStudyRepository


class YearOfStudyService:
    @staticmethod
    def create_year_of_study(year_of_study, study_programme_id):
        try:
            with SessionLocal() as db:
                repository = StudyProgrammeRepository(db)
                study_programme = repository.get_study_programme_by_id(study_programme_id)
                if study_programme:
                    if study_programme.duration < year_of_study:
                        raise YearOfStudyOutOfBoundsException(code=400, message="Year of study out of bounds")
                    year_of_study_repository = YearOfStudyRepository(db)
                    return year_of_study_repository.create_year_of_study(year_of_study, study_programme_id)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

from app.db import SessionLocal
from app.study_programmes.exceptions import StudyProgrammeExistsException, StudyProgrammeNotFoundException
from app.study_programmes.models import StudyProgramme
from app.study_programmes.repository import StudyProgrammeRepository


class StudyProgrammeService:
    @staticmethod
    def create_study_programme(
        full_name: str, abbreviation: str, duration: int
    ) -> StudyProgrammeExistsException or StudyProgramme:
        try:
            with SessionLocal() as db:
                repository = StudyProgrammeRepository(db)
                if repository.get_study_programme_by_full_name(full_name):
                    raise StudyProgrammeExistsException(
                        message="Study programme name already exists in database.",
                        code=400,
                    )
                if repository.get_study_programme_by_abbreviation(abbreviation):
                    raise StudyProgrammeExistsException(
                        message="Study programme abbreviation already exists in database.",
                        code=400,
                    )
                return repository.create_study_programme(full_name, abbreviation, duration)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_study_programmes():
        try:
            with SessionLocal() as db:
                repository = StudyProgrammeRepository(db)
                return repository.get_all_study_programmes()
        except Exception as e:
            raise e

    @staticmethod
    def get_study_programme_by_id(study_programme_id):
        try:
            with SessionLocal() as db:
                repository = StudyProgrammeRepository(db)
                return repository.get_study_programme_by_id(study_programme_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_study_programme_by_id(study_programme_id):
        try:
            with SessionLocal() as db:
                repository = StudyProgrammeRepository(db)
                if repository.delete_study_programme_by_id(study_programme_id):
                    return True
                raise StudyProgrammeNotFoundException(code=400, message="Study programme doesn't exist.")
        except Exception as e:
            raise e

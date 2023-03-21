from fastapi import HTTPException, Response

from app.study_programmes.exceptions import StudyProgrammeExistsException, StudyProgrammeNotFoundException
from app.study_programmes.services import StudyProgrammeService


class StudyProgrammeController:
    @staticmethod
    def create_study_programme(full_name: str, abbreviation: str, duration: int):
        try:
            study_programme = StudyProgrammeService.create_study_programme(full_name, abbreviation, duration)
            return study_programme
        except StudyProgrammeExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_study_programmes():
        study_programmes = StudyProgrammeService.get_all_study_programmes()
        return study_programmes

    @staticmethod
    def get_study_programme_by_id(study_programme_id: str):
        try:
            study_programme = StudyProgrammeService.get_study_programme_by_id(study_programme_id)
            if study_programme:
                return study_programme
            raise StudyProgrammeNotFoundException(code=400, message="Study programme with provided ID not found")
        except StudyProgrammeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_study_programme_by_id(study_programme_id: str):
        try:
            if StudyProgrammeService.delete_study_programme_by_id(study_programme_id):
                return Response(
                    content=f"StudyProgramme with provided ID: {study_programme_id} deleted.",
                    status_code=200,
                )
        except StudyProgrammeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

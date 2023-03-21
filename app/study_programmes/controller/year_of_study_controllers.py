from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError

from app.study_programmes.exceptions import YearOfStudyOutOfBoundsException
from app.study_programmes.services import YearOfStudyService


class YearOfStudyController:
    @staticmethod
    def create_year_of_study(year_of_study: int, study_programme_id: UUID4):
        try:
            return YearOfStudyService.create_year_of_study(year_of_study, study_programme_id)
        except YearOfStudyOutOfBoundsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, Depends

from app.users.controller.user_auth_controller import JWTBearer

from app.study_programmes.controller import StudyProgrammeController
from app.study_programmes.controller.year_of_study_controllers import YearOfStudyController
from app.study_programmes.schemas import (
    StudyProgrammeSchema,
    StudyProgrammeSchemaIn,
    YearOfStudySchema,
    YearOfStudySchemaIn,
)

study_programme_router = APIRouter(prefix="/api/study-programmes", tags=["Study programmes"])
year_of_study_router = APIRouter(prefix="/api/year-of-study", tags=["Years of study"])


@study_programme_router.post(
    "/create-study_programme", response_model=StudyProgrammeSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_study_programme(study_programme: StudyProgrammeSchemaIn):
    return StudyProgrammeController.create_study_programme(
        full_name=study_programme.full_name,
        abbreviation=study_programme.abbreviation,
        duration=study_programme.duration,
    )


@study_programme_router.get("/get-all-study_programmes", response_model=list[StudyProgrammeSchema])
def get_all_study_programmes():
    study_programmes = StudyProgrammeController.get_all_study_programmes()
    return study_programmes


@study_programme_router.get("/get-study_programme-by-id", response_model=StudyProgrammeSchema)
def get_study_programme_by_id(study_programme_id: str):
    return StudyProgrammeController.get_study_programme_by_id(study_programme_id)


@study_programme_router.delete("/delete-study_programme", dependencies=[Depends(JWTBearer("super_user"))])
def delete_study_programme_by_id(study_programme_id: str):
    return StudyProgrammeController.delete_study_programme_by_id(study_programme_id)



@year_of_study_router.post(
    "/create-year-of-study", response_model=YearOfStudySchema, dependencies=[Depends(JWTBearer("super_user"))]
)

def create_year_of_study(year_of_sty: YearOfStudySchemaIn):
    return YearOfStudyController.create_year_of_study(year_of_sty.year_of_study, year_of_sty.study_programme_id)

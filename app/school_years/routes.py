from fastapi import APIRouter, Depends

from app.school_years.controller import SchoolYearController
from app.school_years.schemas import SchoolYearSchema, SchoolYearSchemaIn
from app.users.controller import JWTBearer

school_year_router = APIRouter(prefix="/api/school_years", tags=["School years"])


@school_year_router.post("/create-new-school-year", response_model=SchoolYearSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_new_school_year(school_year: SchoolYearSchemaIn):
    return SchoolYearController.create_new_school_year(
        name=school_year.name, start=school_year.start, end=school_year.end
    )


@school_year_router.get("/get-all-school_years", response_model=list[SchoolYearSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_school_years():
    school_years = SchoolYearController.get_all_school_years()
    return school_years


@school_year_router.get("/get-school-year-by-skg", response_model=SchoolYearSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_school_year_by_skg(skg: str):
    return SchoolYearController.get_school_year_by_skg(skg)


@school_year_router.delete("/delete-school_year", dependencies=[Depends(JWTBearer("super_user"))])
def delete_school_year_by_skg(skg: str):
    return SchoolYearController.delete_school_year_by_skg(skg)

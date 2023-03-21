from fastapi import APIRouter, Depends
from app.users.controller.user_auth_controller import JWTBearer
from app.faculties.controller import FacultyController
from app.faculties.schemas import FacultySchema, FacultySchemaIn

faculty_router = APIRouter(prefix="/api/faculties", tags=["Faculties"])


@faculty_router.post("/create-new-faculty", response_model=FacultySchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_new_faculty(faculty: FacultySchemaIn):
    return FacultyController.create_new_faculty(
        address=faculty.address,
        city=faculty.city,
        name=faculty.name,
        acronym=faculty.acronym,
    )


@faculty_router.get("/get-all-faculties", response_model=list[FacultySchema])
def get_all_faculties():
    faculties = FacultyController.get_all_faculties()
    return faculties


@faculty_router.get("/get-faculty-by-id", response_model=FacultySchema)
def get_faculty_by_id(faculty_id: str):
    return FacultyController.get_faculty_by_id(faculty_id)


@faculty_router.get("/get-faculty-by-city", response_model=list[FacultySchema])
def get_faculty_by_city(city):
    return FacultyController.get_faculty_by_city(city)


@faculty_router.get("/get-faculty-by-name", response_model=list[FacultySchema])
def get_faculty_by_name(name):
    return FacultyController.get_faculty_by_name(name)


@faculty_router.get("/get-faculty-by-name-or-city", response_model=list[FacultySchema])
def get_faculty_by_name_or_city(namecity):
    return FacultyController.get_faculty_by_name_or_city(namecity)


@faculty_router.delete("/delete-faculty", dependencies=[Depends(JWTBearer("super_user"))])
def delete_faculty_by_id(faculty_id: str):
    return FacultyController.delete_faculty_by_id(faculty_id)

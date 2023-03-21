from fastapi import APIRouter, Depends

from app.users.controller import EmployeeController, EmployeeTypeController, UserController
from app.users.controller.student_controller import StudentController
from app.users.controller.user_auth_controller import JWTBearer

from app.users.schemas import *


user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id, is_active)


student_router = APIRouter(tags=["students"], prefix="/api/students")


@student_router.post(
    "/add-new-student",
    response_model=StudentSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_student(student: StudentSchemaIn):
    return StudentController.create_student(
        index=student.index,
        name=student.name,
        parent_name=student.parent_name,
        telephone_number=student.telephone_number,
        address=student.address,
        user_id=student.user_id,
    )


@student_router.get("/get-student-by-id", response_model=StudentSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_student_by_id(student_id: str):
    return StudentController.get_student_by_id(student_id=student_id)


employee_router = APIRouter(tags=["employee"], prefix="/api/employees")


@employee_router.post("/add-new-employee", response_model=EmployeeSchema,
                      dependencies=[Depends(JWTBearer("super_user"))])
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create_employee(employee.name, employee.last_name, employee.employee_type_id)


@employee_router.get("/id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.get("/get-employees-by-characters", response_model=list[EmployeeSchema])
def get_employees_by_characters(characters):
    return EmployeeController.get_employees_by_characters(characters)


@employee_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_employee_by_id(employee_id)


@employee_router.put("/update-employee-by-id", response_model=EmployeeSchema,
                     dependencies=[Depends(JWTBearer("super_user"))])
def update_employee(
    employee_id: str,
    name: str = None,
    last_name: str = None,
    employee_type_id: str = None,
):
    return EmployeeController.update_employee(employee_id, name, last_name, employee_type_id)


employee_type_router = APIRouter(tags=["Employee type"], prefix="/api/employee-type")


@employee_type_router.post(
    "/add-new-employee-type", response_model=EmployeeTypeSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_employee_type(employee_type: EmployeeTypeSchemaIn):
    return EmployeeTypeController.create_employee_type(employee_type.employee_type)


@employee_type_router.get("/id", response_model=EmployeeTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_employee_type_by_id(employee_type_id: str):
    return EmployeeTypeController.get_employee_type_by_id(employee_type_id)


@employee_type_router.get(
    "/get-all-employee-types", response_model=list[EmployeeTypeSchema], dependencies=[Depends(JWTBearer("super_user"))]
)
def get_all_employee_types():
    return EmployeeTypeController.get_all_employee_types()


@employee_type_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_employee_type_by_id(employee_type_id: str):
    return EmployeeTypeController.delete_employee_type_by_id(employee_type_id)


@employee_type_router.put("/update", response_model=EmployeeTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_employee_type(employee_type_id, employee_type):
    return EmployeeTypeController.update_employee_type(employee_type_id, employee_type)

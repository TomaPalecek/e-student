from pydantic import UUID4, BaseModel


class EmployeeTypeSchema(BaseModel):
    id: UUID4
    employee_type: str

    class Config:
        orm_mode = True


class EmployeeTypeSchemaIn(BaseModel):
    employee_type: str

    class Config:
        orm_mode = True

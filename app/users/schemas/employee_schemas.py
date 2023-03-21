from pydantic import UUID4, BaseModel


class EmployeeSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    employee_type_id: str

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    name: str
    last_name: str
    employee_type_id: str

    class Config:
        orm_mode = True

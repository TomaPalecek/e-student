from pydantic import UUID4, BaseModel


class CourseSchema(BaseModel):
    id: UUID4
    code: str
    name: str
    description: str

    class Config:
        orm_mode = True


class CourseSchemaIn(BaseModel):
    code: str
    name: str
    description: str

    class Config:
        orm_mode = True

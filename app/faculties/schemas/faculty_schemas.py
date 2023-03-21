from pydantic import UUID4, BaseModel


class FacultySchema(BaseModel):
    id: UUID4
    address: str
    city: str
    name: str
    acronym: str

    class Config:
        orm_mode = True


class FacultySchemaIn(BaseModel):
    address: str
    city: str
    name: str
    acronym: str

    class Config:
        orm_mode = True

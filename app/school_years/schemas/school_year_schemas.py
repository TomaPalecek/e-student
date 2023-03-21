from datetime import date

from pydantic import UUID4, BaseModel


class SchoolYearSchema(BaseModel):
    skg: UUID4
    name: str
    start: date
    end: date

    class Config:
        orm_mode = True


class SchoolYearSchemaIn(BaseModel):
    name: str
    start: str
    end: str

    class Config:
        orm_mode = True

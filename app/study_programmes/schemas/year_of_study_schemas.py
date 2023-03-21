from pydantic import BaseModel
from pydantic.types import UUID4, PositiveInt


class YearOfStudySchema(BaseModel):
    id: UUID4
    year_of_study: PositiveInt
    study_programme_id: UUID4

    class Config:
        orm_mode = True


class YearOfStudySchemaIn(BaseModel):
    year_of_study: PositiveInt
    study_programme_id: str

    class Config:
        orm_mode = True

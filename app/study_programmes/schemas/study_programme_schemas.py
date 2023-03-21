from typing import Optional

from pydantic import UUID4, BaseModel


class StudyProgrammeSchema(BaseModel):
    id: UUID4
    full_name: str
    abbreviation: str
    duration: int

    class Config:
        orm_mode = True


class StudyProgrammeSchemaIn(BaseModel):
    full_name: str
    abbreviation: str
    duration: int

    class Config:
        orm_mode = True


class StudyProgrammeSchemaUpdate(BaseModel):
    full_name: Optional[str]
    abbreviation: Optional[str]
    duration: Optional[int]

    class Config:
        orm_mode = True

from uuid import uuid4

from sqlalchemy import Column, Integer, String

from app.db import Base


class StudyProgramme(Base):
    __tablename__ = "study_programmes"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    full_name = Column(String(50), unique=True)
    abbreviation = Column(String(20), unique=True)
    duration = Column(Integer)

    def __init__(self, full_name: str, abbreviation: str, duration: int):
        self.full_name = full_name
        self.abbreviation = abbreviation
        self.duration = duration

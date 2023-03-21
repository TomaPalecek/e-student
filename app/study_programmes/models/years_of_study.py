from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db import Base


class YearOfStudy(Base):
    __tablename__ = "years_of_study"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    year_of_study = Column(Integer)

    study_programme_id = Column(String(50), ForeignKey("study_programmes.id"))
    study_programme = relationship("StudyProgramme", lazy="subquery")
    __table_args__ = (UniqueConstraint("year_of_study", "study_programme_id", name="yr_study_programme_uc"),)

    def __init__(self, year_of_study: int, study_programme_id: uuid4):
        self.year_of_study = year_of_study
        self.study_programme_id = study_programme_id

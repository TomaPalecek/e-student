from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Date, String, UniqueConstraint, CheckConstraint

from app.db import Base


class SchoolYear(Base):
    __tablename__ = "school_years"
    skg = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(9))  # i.e. '2021/2022'
    start = Column(Date)
    end = Column(Date)
    __table_args__ = (UniqueConstraint("name", "start", "end", name="name_start_end_uc"),
                      CheckConstraint(start < end, name='check_start_end'))

    def __init__(self, name: str, start: str, end: str):
        self.name = name
        self.start = datetime.strptime(start, "%Y-%m-%d")
        self.end = datetime.strptime(end, "%Y-%m-%d")

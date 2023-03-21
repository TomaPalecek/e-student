from uuid import uuid4

from sqlalchemy import Column, String, CheckConstraint

from app.db import Base


class Faculty(Base):
    __tablename__ = "faculties"
    __table_args__ = (CheckConstraint("length(acronym) < 20"),)
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    address = Column(String(200))
    city = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    acronym = Column(String(20), unique=True)

    def __init__(self, address: str, city: str, name: str, acronym: str):
        self.address = address
        self.city = city
        self.name = name
        self.acronym = acronym

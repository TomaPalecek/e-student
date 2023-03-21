from uuid import uuid4

from sqlalchemy import Column, String

from app.db.database import Base


class EmployeeType(Base):
    __tablename__ = "employee_types"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    employee_type = Column(String(50), unique=True)

    def __init__(self, employee_type):
        self.employee_type = employee_type

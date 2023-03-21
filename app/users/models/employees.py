from uuid import uuid4

from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, String

from app.db.database import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    last_name = Column(String(50))

    employee_type_id = Column(String(50), ForeignKey("employee_types.id"), nullable=False)

    def __init__(self, name, last_name, employee_type_id):
        self.name = name
        self.last_name = last_name
        self.employee_type_id = employee_type_id

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.last_name != other.last_name:
            return False
        if self.employee_type_id != other.employee_type_id:
            return False
        return True

    def __ne__(self, other):
        if self.name == other.name:
            return False
        if self.last_name == other.last_name:
            return False
        if self.employee_type_id == other.employee_type_id:
            return False
        return True

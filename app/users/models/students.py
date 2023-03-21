from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    index = Column(String(10), unique=True)
    name = Column(String(100))
    parent_name = Column(String(100))
    telephone_number = Column(String(100))
    address = Column(String(150))

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy="subquery")

    def __init__(self, index, name, parent_name, telephone_number, address, user_id):
        self.index = index
        self.name = name
        self.parent_name = parent_name
        self.telephone_number = telephone_number
        self.address = address
        self.user_id = user_id

    def __eq__(self, other):
        if self.index != other.index:
            return False
        if self.name != other.name:
            return False
        if self.parent_name != other.parent_name:
            return False
        if self.telephone_number != other.telephone_number:
            return False
        if self.address != other.address:
            return False
        if self.user_id != other.user_id:
            return False
        return True

    def __ne__(self, other):
        if self.index == other.index:
            return False
        if self.name == other.name:
            return False
        if self.parent_name == other.parent_name:
            return False
        if self.telephone_number == other.telephone_number:
            return False
        if self.address == other.address:
            return False
        if self.user_id == other.user_id:
            return False
        return True

from uuid import uuid4

from sqlalchemy import Boolean, Column, String

from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    is_active = Column(Boolean)
    is_superuser = Column(Boolean, default=False)

    def __init__(self, email, password, is_active=True, is_superuser=False):
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser

    def __eq__(self, other):
        if self.id != other.id:
            return False
        if self.email != other.email:
            return False
        if self.password != other.password:
            return False
        if self.is_active != other.is_active:
            return False
        if self.is_superuser != other.is_superuser:
            return False
        return True

    def __ne__(self, other):
        if self.id == other.id:
            return False
        if self.email == other.email:
            return False
        if self.password == other.password:
            return False
        if self.is_active == other.is_active:
            return False
        if self.is_superuser == other.is_superuser:
            return False
        return True

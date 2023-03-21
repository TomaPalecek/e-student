from pydantic import UUID4, BaseModel

from app.users.schemas.user_schemas import UserSchema


class StudentSchema(BaseModel):
    id: UUID4
    index: str
    name: str
    parent_name: str
    telephone_number: str
    address: str
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class StudentSchemaIn(BaseModel):
    index: str
    name: str
    parent_name: str
    telephone_number: str
    address: str
    user_id: str

    class Config:
        orm_mode = True

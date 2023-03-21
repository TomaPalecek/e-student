from pydantic import UUID4, BaseModel


class CourseSpecificationSchema(BaseModel):
    id: UUID4
    espb: int
    points: int
    pre_exam_points: int
    lectures: int
    exercises: int
    program: str
    course_id: str

    class Config:
        orm_mode = True


class CourseSpecificationSchemaIn(BaseModel):
    espb: int
    points: int
    pre_exam_points: int
    lectures: int
    exercises: int
    program: str
    course_id: str

    class Config:
        orm_mode = True

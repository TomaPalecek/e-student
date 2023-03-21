from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String

from app.db import Base


class CourseSpecification(Base):
    __tablename__ = "course_specification"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    espb = Column(Integer)
    points = Column(Integer)
    pre_exam_points = Column(Integer)
    lectures = Column(Integer)
    exercises = Column(Integer)
    program = Column(String(50))  # TODO SPOJITI FK SA PROGRAMI
    course_id = Column(String(50), ForeignKey("courses.id"))

    def __init__(
        self,
        espb: int,
        points: int,
        pre_exam_points: int,
        lectures: int,
        exercises: int,
        program: str,
        course_id: str,
    ):
        self.espb = espb
        self.points = points
        self.pre_exam_points = pre_exam_points
        self.lectures = lectures
        self.exercises = exercises
        self.program = program
        self.course_id = course_id

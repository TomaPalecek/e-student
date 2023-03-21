from typing import Type

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.courses.exceptions import CourseNotFoundException
from app.courses.models import CourseSpecification


class CourseSpecificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_course_specification(
        self,
        espb: int,
        points: int,
        pre_exam_points: int,
        lectures: int,
        exercises: int,
        program: str,
        course_id: str,
    ):
        try:
            course_specification = CourseSpecification(
                espb, points, pre_exam_points, lectures, exercises, program, course_id
            )
            self.db.add(course_specification)
            self.db.commit()
            self.db.refresh(course_specification)
            return course_specification
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_course_specifications(self):
        course_specification = self.db.query(CourseSpecification).all()
        return course_specification

    def read_course_specification_by_course_id(self, course_id: str) -> Type[CourseSpecification]:
        course_specification = (
            self.db.query(CourseSpecification).filter(CourseSpecification.course_id == course_id).first()
        )
        if course_specification is None:
            raise CourseNotFoundException(f"Course with provided ID: {course_id} not found.", 400)
        return course_specification

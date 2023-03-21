import pytest
from sqlalchemy.exc import IntegrityError

from app.courses.exceptions import CourseNotFoundException
from app.courses.repositories import CourseSpecificationRepository, CourseRepository
from app.tests import TestClass, TestingSessionLocal


class TestCourseSpecificationRepository(TestClass):

    def test_create_course_specs(self):
        with TestingSessionLocal() as db:
            course_repo = CourseRepository(db)
            course = course_repo.create_course("100", "name", "desc")
            course_spec_repository = CourseSpecificationRepository(db)
            course_spec = course_spec_repository.create_course_specification(espb=10, points=111, pre_exam_points=111,
                                                                             lectures=3, exercises=2, program="program",
                                                                             course_id=course.id)
            assert course_spec.espb == 10
            assert course_spec.points == 111
            assert course_spec.pre_exam_points == 111
            assert course_spec.lectures == 3
            assert course_spec.exercises == 2
            assert course_spec.program == "program"
            assert course_spec.course_id == course.id

    def test_create_course_specs_foreign_key_error(self):
        with TestingSessionLocal() as db:
            course_spec_repository = CourseSpecificationRepository(db)
            with pytest.raises(IntegrityError):
                course_spec_repository.create_course_specification(espb=10, points=111, pre_exam_points=111,
                                                                   lectures=3, exercises=2, program="program",
                                                                   course_id="dasdasd")

    def test_read_all_courses_specifications(self):
        with TestingSessionLocal() as db:
            course_repo = CourseRepository(db)
            course = course_repo.create_course("100", "name", "desc")
            course_spec_repository = CourseSpecificationRepository(db)
            course_spec_repository.create_course_specification(espb=10, points=111, pre_exam_points=111,
                                                               lectures=3, exercises=2, program="program",
                                                               course_id=course.id)
            course_spec_repository.create_course_specification(espb=10, points=111, pre_exam_points=111,
                                                               lectures=3, exercises=2, program="program",
                                                               course_id=course.id)
            course_spec_repository.create_course_specification(espb=10, points=111, pre_exam_points=111,
                                                               lectures=3, exercises=2, program="program",
                                                               course_id=course.id)
            list_of_course_specs = course_spec_repository.read_all_course_specifications()
            assert len(list_of_course_specs) == 3

    def test_read_course_specs_by_id(self):
        with TestingSessionLocal() as db:
            course_repo = CourseRepository(db)
            course = course_repo.create_course("100", "name", "desc")
            course_spec_repository = CourseSpecificationRepository(db)
            course_spec = course_spec_repository.create_course_specification(espb=10, points=111, pre_exam_points=111,
                                                                             lectures=3, exercises=2, program="program",
                                                                             course_id=course.id)
            c_spec = course_spec_repository.read_course_specification_by_course_id(course_id=course_spec.course_id)
            assert course_spec.course_id == c_spec.course_id

    def test_read_course_specs_by_id_err(self):
        with TestingSessionLocal() as db:
            course_spec_repository = CourseSpecificationRepository(db)
            with pytest.raises(CourseNotFoundException):
                course_spec_repository.read_course_specification_by_course_id(course_id="sdasdas")

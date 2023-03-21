import pytest
from sqlalchemy.exc import IntegrityError

from app.courses.exceptions import CourseNotFoundException
from app.courses.repositories import CourseRepository
from app.tests import TestClass, TestingSessionLocal


class TestCourseRepo(TestClass):

    # create course

    def test_create_course(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            course = course_repository.create_course("100", "name", "desc")
            assert course.code == "100"
            assert course.name == "name"
            assert course.description == "desc"

    def test_create_course_err(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            course_repository.create_course("100", "name1", "desc1")
            with pytest.raises(IntegrityError):
                course_repository.create_course("100", "name", "desc")

    # get courses

    def test_get_all_course(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            course_repository.create_course("100", "name", "desc")
            course_repository.create_course("101", "name", "desc")
            course_repository.create_course("102", "name", "desc")
            all_courses = course_repository.read_all_courses()
            assert len(all_courses) == 3

    def test_get_course_by_id(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            new_course = course_repository.create_course("100", "name", "desc")
            course_from_db = course_repository.read_course_by_id(new_course.id)
            assert new_course.id == course_from_db.id

    def test_get_course_by_id_not_found(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            with pytest.raises(CourseNotFoundException):
                course_repository.read_course_by_id("name")

    # delete course

    def test_delete_course_by_id(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            new_course = course_repository.create_course("100", "name", "desc")
            deleted = course_repository.delete_course(new_course.id)
            assert deleted is True

    def test_delete_course_by_id_not_found(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            course_repository.create_course("100", "name", "desc")
            with pytest.raises(CourseNotFoundException):
                course_repository.delete_course("dasdas")

    def test_read_course_by_code(self):
        with TestingSessionLocal() as db:
            course_repository = CourseRepository(db)
            course_repository.create_course("100", "name", "desc")
            db_course = course_repository.read_course_by_code("100")
            assert db_course.code == "100"

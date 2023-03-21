from fastapi import HTTPException, Response

from app.courses.exceptions import CourseExceptionCode, CourseNotFoundException
from app.courses.services import CourseService


class CourseController:
    @staticmethod
    def create_new_course(code: str, name: str, description: str):
        try:
            course = CourseService.create_new_course(code, name, description)
            return course
        except CourseExceptionCode as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_courses():
        courses = CourseService.read_all_courses()
        return courses

    @staticmethod
    def get_course_by_id(course_id: str):
        try:
            course = CourseService.read_course_by_id(course_id)
            return course
        except CourseNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_course_by_id(course_id: str):
        """
        :param course_id: Course ID
        :return: No return
        """
        try:
            del_test = CourseService.delete_course_by_id(course_id)
            test = f"test{del_test}"
            test = "test 2 test 2test 2test 2test 2test 2test 2test 2test 2test 2test 2test 2test 2test 2test test 2test 2test 2test 2test 22test 2 "
            return Response(
                content=f"Course with provided ID: {course_id} deleted.",
                status_code=200,
            )
        except CourseNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

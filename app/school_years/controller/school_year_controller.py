from fastapi import HTTPException, Response

from app.school_years.exceptions import SchoolYearExceptionName, SchoolYearNotFoundException
from app.school_years.services import SchoolYearService


class SchoolYearController:
    @staticmethod
    def create_new_school_year(name: str, start: str, end: str):
        try:
            school_year = SchoolYearService.create_new_school_year(name, start, end)
            return school_year
        except SchoolYearExceptionName as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_school_years():
        school_years = SchoolYearService.read_all_school_years()
        return school_years

    @staticmethod
    def get_school_year_by_skg(school_year_skg: str):
        try:
            school_year = SchoolYearService.read_school_year_by_skg(school_year_skg)
            return school_year
        except SchoolYearNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_school_year_by_skg(school_year_skg: str):
        try:
            SchoolYearService.delete_school_year_by_skg(school_year_skg)
            return Response(
                content=f"School year with provided SKG: {school_year_skg} deleted.",
                status_code=200,
            )
        except SchoolYearNotFoundException as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

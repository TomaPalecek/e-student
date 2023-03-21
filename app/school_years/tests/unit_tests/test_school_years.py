import datetime

import pytest
from sqlalchemy.exc import IntegrityError

from app.school_years.exceptions import SchoolYearNotFoundException
from app.school_years.repositories import SchoolYearRepository
from app.tests import TestClass, TestingSessionLocal


class TestSchoolYearsRepo(TestClass):

    def test_create_school_years_for_methods(self):
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            school_year = school_year_repository.create_school_year("2010/2011", "2010-10-01", "2011-09-30")
            school_year = school_year_repository.create_school_year("2011/2012", "2011-10-01", "2012-09-30")

    def test_create_school_year_for_methods(self):
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            school_year = school_year_repository.create_school_year("2010/2011", "2010-10-01", "2011-09-30")

    def test_create_school_year(self):
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            school_year = school_year_repository.create_school_year("2020/2021", "2020-10-01", "2021-09-30")
            assert school_year.name == "2020/2021"
            assert school_year.start == datetime.date(2020, 10, 1)
            assert school_year.end == datetime.date(2021, 9, 30)
            assert school_year.start < school_year.end
            # with pytest.raises(TypeError) as e:
            #     school_year = school_year_repository.create_school_year("2020/2021", "2020-10-01", 123)
            with pytest.raises(IntegrityError) as e:
                school_year = school_year_repository.create_school_year("2020/2021", "2020-10-01", "2021-09-30")
                school_year = school_year_repository.create_school_year("2020/2021", "2021-09-30", "2020-10-01")





    def test_get_all_school_years_if_none(self):
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            all_school_years = school_year_repository.read_all_school_years()
            assert all_school_years == []

    def test_get_all_school_years(self):
        self.test_create_school_years_for_methods()
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            all_school_years = school_year_repository.read_all_school_years()
            assert len(all_school_years) == 2

    def test_read_school_year_by_skg(self):
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            school_year = school_year_repository.create_school_year("2020/2021", "2020-10-01", "2021-09-30")
            school_year_skg = school_year_repository.read_school_year_by_skg(school_year.skg)
            assert school_year_skg is not None
            with pytest.raises(SchoolYearNotFoundException) as e:
                school_year_skg = school_year_repository.read_school_year_by_skg("school_year_false_skg")


    def test_read_school_year_by_name(self):
        self.test_create_school_year_for_methods()
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            school_year = school_year_repository.read_school_year_by_name("2010/2011")
            assert school_year.name == "2010/2011"

    def test_delete_school_year(self):
        self.test_create_school_year_for_methods()
        with TestingSessionLocal() as db:
            school_year_repository = SchoolYearRepository(db)
            school_year = school_year_repository.create_school_year("2020/2021", "2020-10-01", "2021-09-30")
            assert school_year is not None
            with pytest.raises(SchoolYearNotFoundException) as e:
                school_year = school_year_repository.read_school_year_by_skg("false_skg")
            school_year_delete = school_year_repository.delete_school_year(school_year.skg)
            assert school_year_delete is True


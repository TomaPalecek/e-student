import pytest
from sqlalchemy.exc import IntegrityError

from app.study_programmes.exceptions import YearOfStudyNotFoundException
from app.study_programmes.models import YearOfStudy
from app.tests import TestClass, TestingSessionLocal
from app.study_programmes.repository import YearOfStudyRepository, StudyProgrammeRepository
from typing import List


class TestStudyProgrammes(TestClass):
    @staticmethod
    def create_yos_for_methods():
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos_repository.create_year_of_study(3, spd.id)
            yos_repository.create_year_of_study(2, spd.id)
            yos_repository.create_year_of_study(4, spd.id)
            yos_repository.create_year_of_study(5, spd.id)

    def test_create_year_of_study(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos = yos_repository.create_year_of_study(3, spd.id)
            assert yos.year_of_study == 3
            assert yos.study_programme_id == spd.id

    def test_get_all_yos(self):
        self.create_yos_for_methods()
        with TestingSessionLocal() as db:
            spd = YearOfStudyRepository(db)
            all_spr = spd.get_all_years_of_study()
            assert len(all_spr) == 4

    def test_create_yos_fail(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos_repository.create_year_of_study(5, spd.id)
            with pytest.raises(IntegrityError) as e:
                yos_repository.create_year_of_study(5, spd.id)

    def test_get_yos_by_id(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos = yos_repository.create_year_of_study(5, spd.id)
            yos_id = yos.id
            yos = yos_repository.get_year_of_study_by_id(yos_id)
            assert isinstance(yos, YearOfStudy)

    def test_fail_get_yos_by_id(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos = yos_repository.create_year_of_study(5, spd.id)
            yos_id = "qwerty"
            yos = yos_repository.get_year_of_study_by_id(yos_id)
            assert not yos

    def test_delete_yos(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos = yos_repository.create_year_of_study(5, spd.id)
            sp_id = yos.id
            sp = yos_repository.delete_year_of_study_by_id(sp_id)
            assert sp

    def test_delete_study_program_fail(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos = yos_repository.create_year_of_study(5, spd.id)
            with pytest.raises(YearOfStudyNotFoundException) as e:
                sp_id = "qwerty"
                yos_repository.delete_year_of_study_by_id(sp_id)

    def test_get_yos_by_programme_id(self):
        with TestingSessionLocal() as db:
            yos_repository = YearOfStudyRepository(db)
            sp_repository = StudyProgrammeRepository(db)
            spd = sp_repository.create_study_programme("computer science1", "CS1", 4)
            yos = yos_repository.create_year_of_study(5, spd.id)
            yos_programme_id = yos.study_programme_id
            yos1 = yos_repository.get_year_of_study_by_study_programme_id(yos_programme_id)
            assert isinstance(yos1, YearOfStudy)

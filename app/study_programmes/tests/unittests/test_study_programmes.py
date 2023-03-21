import pytest
from sqlalchemy.exc import IntegrityError

from app.study_programmes.exceptions import StudyProgrammeNotFoundException
from app.study_programmes.models import StudyProgramme
from app.tests import TestClass, TestingSessionLocal
from app.study_programmes.repository import StudyProgrammeRepository


class TestStudyProgrammes(TestClass):

    def create_tds_for_methods(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spd = study_program_repository.create_study_programme("computer science1", "CS1", 4)
            spd = study_program_repository.create_study_programme("computer science2", "CS2", 4)
            spd = study_program_repository.create_study_programme("computer science3", "CS3", 4)
            spd = study_program_repository.create_study_programme("computer science4", "CS4", 4)

    def test_create_study_program(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            assert spr.full_name == "computer science5"
            assert spr.abbreviation == "CS"
            assert spr.duration == 4

    def test_get_all_study_programmes(self):
        self.create_tds_for_methods()
        with TestingSessionLocal() as db:
            spd = StudyProgrammeRepository(db)
            all_spr = spd.get_all_study_programmes()
            assert len(all_spr) == 4

    def test_create_study_program_fail(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            with pytest.raises(IntegrityError) as e:
                spr1 = study_program_repository.create_study_programme("computer science6", "CS", 4)

    def test_get_study_programmes_by_abbreviation(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            sp = study_program_repository.get_study_programme_by_abbreviation("CS")
            assert isinstance(sp, StudyProgramme)

    def test_delete_study_program(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            sp_id = spr.id
            sp = study_program_repository.delete_study_programme_by_id(sp_id)
            assert sp

    def test_delete_study_program_fail(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            with pytest.raises(StudyProgrammeNotFoundException) as e:
                sp_id = "qwerty"
                sp = study_program_repository.delete_study_programme_by_id(sp_id)

    def test_get_study_programmes_by_id(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            sp_id = spr.id
            sp = study_program_repository.get_study_programme_by_id(sp_id)
            assert isinstance(sp, StudyProgramme)

    def test_get_study_programmes_by_id_fail(self):
        with TestingSessionLocal() as db:
            study_program_repository = StudyProgrammeRepository(db)
            spr = study_program_repository.create_study_programme("computer science5", "CS", 4)
            sp = study_program_repository.get_study_programme_by_id("qwerty")
            assert not sp



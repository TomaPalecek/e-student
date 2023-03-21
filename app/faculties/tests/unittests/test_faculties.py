import pytest
from sqlalchemy.exc import OperationalError, IntegrityError, DataError

from app.faculties.repositories import FacultyRepository
from app.tests import TestClass, TestingSessionLocal


class TestFacultyRepo(TestClass):

    def create_initial_records(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            repository.create_faculty("1st Street", "Chicago", "Chicago Faculty", "CF")
            repository.create_faculty("1st Street", "London", "London Faculty", "LF")
            repository.create_faculty("1st Street", "Berlin", "Berlin Faculty", "BF")

    def test_create_faculty(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            assert faculty.name == "New York Faculty"
            assert faculty.address == "1st Street"
            assert faculty.acronym == "NYF"
            assert faculty.city == "New York"

    def test_get_all_faculties(self):
        self.create_initial_records()
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            all_faculties = repository.read_all_faculties()
        assert len(all_faculties) == 4

    def test_get_faculty_by_id(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            faculties = repository.read_all_faculties()
            obj_id = faculty.id
            assert obj_id == faculties[0].id
            assert faculties[0].name == "New York Faculty"
            assert faculties[0].address == "1st Street"
            assert faculties[0].acronym == "NYF"
            assert faculties[0].city == "New York"

    def test_get_faculty_by_city(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            obj = repository.read_faculty_by_city("New Y")
            assert faculty.city == obj[0].city
            assert faculty.city == "New York"
            assert faculty.name == "New York Faculty"
            assert faculty.acronym == "NYF"
            assert faculty.address == "1st Street"

    def test_get_faculty_by_name(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            obj = repository.read_faculty_by_name("New Y")
            assert faculty.name == obj[0].name
            assert faculty.name == "New York Faculty"
            assert faculty.city == "New York"
            assert faculty.acronym == "NYF"
            assert faculty.address == "1st Street"

    def test_get_faculty_by_name_or_city(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            obj = repository.read_faculty_by_name_or_city("New Y")
            assert obj[0].name == faculty.name
            assert obj[0].city == "New York"
            assert obj[0].name == "New York Faculty"
            assert obj[0].address == "1st Street"
            assert obj[0].acronym == "NYF"
            obj = repository.read_faculty_by_name_or_city("Faculty")
            assert obj[0].name == faculty.name
            assert obj[0].city == "New York"
            assert obj[0].name == "New York Faculty"
            assert obj[0].address == "1st Street"
            assert obj[0].acronym == "NYF"

    def test_get_faculty_by_acronym(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            obj = repository.read_faculty_by_acronym("NY")
            assert obj[0].name == "New York Faculty"
            assert obj[0].city == faculty.city
            assert obj[0].city == "New York"
            assert obj[0].name == "New York Faculty"
            assert obj[0].address == "1st Street"
            assert obj[0].acronym == "NYF"

    def test_delete_faculty(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            faculty = repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            flag = repository.delete_faculty(faculty.id)
            assert flag

    # OVAJ TEST NE RADI ISTO NA MAC-u/Linux-u i tupavom Windowsu. Zato je zakomentarisan. NE PIPAJ INACE CE DA TI PUKNE
    # TEST
    # def test_create_faculty_error_acronym_length(self):
    #     with TestingSessionLocal() as db:
    #         repository = FacultyRepository(db)
    #         with pytest.raises(DataError) as e:
    #             repository.create_faculty("1st Street", "New York", "New York Faculty", "GUUFFYWWWWWWTTTYFDURD")

    def test_create_faculty_error_acronym_unique(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            repository.create_faculty("1st Street", "New York", "New York Faculty", "NYF")
            with pytest.raises(IntegrityError) as e:
                repository.create_faculty("1st Street", "London", "London Faculty", "NYF")

    def test_create_faculty_error_city_not_null(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            with pytest.raises(IntegrityError) as e:
                repository.create_faculty("1st Street", None, "New York Faculty", "NYF")

    def test_create_faculty_error_name_not_null(self):
        with TestingSessionLocal() as db:
            repository = FacultyRepository(db)
            with pytest.raises(IntegrityError) as e:
                repository.create_faculty("1st Street", "New York", None, "NYF")

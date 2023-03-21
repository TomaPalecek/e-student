import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import EmployeeRepository, EmployeeTypeRepository


class TestEmployeeRepo(TestClass):
    def create_employees_for_methods(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            employee_type1 = employee_type_repository.create_employee_type("professor")
            employee1 = employee_repository.create_employee("name", "lastname", employee_type1.id)
            employee2 = employee_repository.create_employee("name", "lastname", employee_type1.id)
            employee3 = employee_repository.create_employee("name", "lastname", employee_type1.id)
            employee4 = employee_repository.create_employee("name", "lastname", employee_type1.id)

    def test_create_employee(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            employee_type1 = employee_type_repository.create_employee_type("professor")
            employee1 = employee_repository.create_employee("name", "lastname", employee_type1.id)

            assert employee1.employee_type_id == employee_type1.id
            assert employee1.name == "name"
            assert employee1.last_name == "lastname"

    def test_create_employee_error(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            employee_type1 = employee_type_repository.create_employee_type("professor")
            employee1 = employee_repository.create_employee("name", "lastname", employee_type1.id)

            assert not employee1.employee_type_id != employee_type1.id
            assert not employee1.name != "name"
            assert not employee1.last_name != "lastname"
            # with pytest.raises(IntegrityError) as e:
            #     employee2 = employee_repository.create_employee("name", "lastname", employee_type1.id)

    def test_get_employee_by_id(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            employee_type1 = employee_type_repository.create_employee_type("professor")
            employee1 = employee_repository.create_employee("name", "lastname", employee_type1.id)
            employee2 = employee_repository.get_employee_by_id(employee1.id)

            assert employee1 == employee2

    def test_get_employee_by_id_error(self):
        with TestingSessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee_type_repository = EmployeeTypeRepository(db)

            employee_type1 = employee_type_repository.create_employee_type("professor")
            employee1 = employee_repository.create_employee("name", "lastname", employee_type1.id)
            employee2 = employee_repository.get_employee_by_id(employee1.id)

            assert not employee1 != employee2

    def test_get_employees_by_characters(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)

            employees = employee_repository.get_employees_by_characters("name")

            assert len(employees) == 4

    def test_get_employees_by_characters_error(self):
        with TestingSessionLocal() as db:
            self.create_employees_for_methods()
            employee_repository = EmployeeRepository(db)

            employees = employee_repository.get_employees_by_characters("name")

            assert not len(employees) != 4

    # def test_get_employees_by_employee_type_id(self):
    #     with TestingSessionLocal() as db:
    #         self.create_employees_for_methods()
    #         employee_repository = EmployeeRepository(db)
    #         employee_type_repository = EmployeeTypeRepository(db)
    #
    #         employee_type1 = employee_type_repository.create_employee_type("professor")
    #         employees = employee_repository.get_employees_by_employee_type_id(employee_type1.id)
    #
    #         assert len(employees) == 4

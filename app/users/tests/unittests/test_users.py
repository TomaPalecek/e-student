import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import UserRepository


class TestUserRepo(TestClass):

    def create_users_for_methods(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo1@gmail.com", "sifra123")
            user = user_repository.create_user("mihajlo2@gmail.com", "sifra123")
            user = user_repository.create_user("mihajlo3@gmail.com", "sifra123")
            user = user_repository.create_user("mihajlo4@gmail.com", "sifra123")


    def test_create_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo@gmail.com", "sifra123")
            assert user.email == "mihajlo@gmail.com"
            assert user.is_superuser is False
            assert user.is_active is True

    def test_create_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("mihajlo@gmail.com", "sifra123")
            assert user.is_active is not False
            with pytest.raises(IntegrityError) as e:
                user1 = user_repository.create_user("mihajlo@gmail.com", "sifra123")

    def test_create_super_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user("velja@gmail.com", "sifra1253")
            assert super_user.email == "velja@gmail.com"
            assert super_user.is_superuser is True
            # assert super_user.is_active is True

    def test_create_super_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user("velja@gmail.com", "sifra1253")
            assert super_user.is_superuser is not False
            with pytest.raises(IntegrityError) as e:
                user1 = user_repository.create_super_user("velja@gmail.com", "sifra1253")


    def test_get_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "sifra1253")
            user1 = user_repository.get_user_by_id(user.id)
            assert user == user1

    def test_get_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "sifra1253")
            user1 = user_repository.get_user_by_id(user.id)
            assert not user != user1

    def test_get_all_users(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert len(all_users) == 4

    def test_get_all_users_error(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert not len(all_users) != 4

    def test_delete_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "1234")
            assert user_repository.delete_user_by_id(user.id) is True

    def test_delete_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "1234")
            assert user_repository.delete_user_by_id(user.id) is not False


    def test_update_user_is_active(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "1234")
            user = user_repository.update_user_is_active(user.id, False)
            assert user.is_active is False

    def test_update_user_is_active_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "1234")
            user = user_repository.update_user_is_active(user.id, False)
            assert user.is_active is not True

    def test_read_user_by_email(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "1234")
            assert user.email == "velja@gmail.com"

    def test_read_user_by_email_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("velja@gmail.com", "1234")
            assert not user.email != "velja@gmail.com"

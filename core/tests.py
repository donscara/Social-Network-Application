from django.test import TestCase, override_settings
from django.contrib.auth.models import User
import tempfile


class BaseTestCase(TestCase):
    def create_user(self):
        self.user1 = User(
            username="user1",
            email="user1@example.com",
            first_name="user",
            last_name="one",
            is_active=True,
        )
        self.user1.set_password("qwert.12345")
        self.user1.save()
        self.user2 = User(
            username="user2",
            email="user2@example.com",
            first_name="user",
            last_name="two",
            is_active=True,
        )
        self.user2.set_password("qwert.12345")
        self.user2.save()

    def setUp(self) -> None:
        res = super().setUp()
        self.create_user()

        return res

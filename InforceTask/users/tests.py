from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="TestUsername", email="test@gmail.com", password="testpassword")

    def test_user_default_vote_gor_value(self):
        user = User.objects.get(username='TestUsername')
        self.assertEqual(user.vote_for, None)


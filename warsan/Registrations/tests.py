from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from faker import Faker

class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Initialize Faker
        cls.fake = Faker()

        # Create a user for testing
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a UserProfile instance with fake data
        cls.user_profile = UserProfile.objects.create(
            user=cls.user,
            email=cls.fake.email(),
            first_name=cls.fake.first_name(),
            last_name=cls.fake.last_name()
        )

    def test_get_full_name(self):
        user_profile = UserProfile.objects.get(id=self.user_profile.id)
        full_name = user_profile.get_full_name()
        expected_full_name = f"{self.user_profile.first_name} {self.user_profile.last_name}"
        self.assertEqual(full_name, expected_full_name)

    def test_str_method(self):
        user_profile = UserProfile.objects.get(id=self.user_profile.id)
        expected_str = self.user_profile.user.username
        self.assertEqual(str(user_profile), expected_str)

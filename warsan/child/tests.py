from django.test import TestCase
from django.urls import reverse
from .models import Child, Guardian

class ChildModelTestCase(TestCase):
    def test_child_model_str_representation(self):
        guardian = Guardian.objects.create(
            first_name='Abdi',
            last_name='Ali',
            location='Mogadishu',
            phone_number='+252123456789'
        )
        child = Child.objects.create(
            first_name='Amina',
            last_name='Abdi',
            date_of_birth='2000-01-01',
            gender='F',
            guardian=guardian,
        )
        self.assertEqual(str(child), "Amina Abdi (Child of Abdi Ali)")

class GuardianModelTestCase(TestCase):
    def test_guardian_model_str_representation(self):
        guardian = Guardian.objects.create(
            first_name='Abdi',
            last_name='Ali',
            location='Mogadishu',
            phone_number='+252123456789'
        )
        self.assertEqual(str(guardian), "Abdi Ali")

class AdminPagesTestCase(TestCase):
    def test_child_admin_page_accessible(self):
        response = self.client.get(reverse('admin:child_child_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_guardian_admin_page_accessible(self):
        response = self.client.get(reverse('admin:child_guardian_changelist'))
        self.assertEqual(response.status_code, 200)

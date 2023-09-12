from django.test import TestCase
from rest_framework.test import APIClient  # Import APIClient
from child.models import Child, Guardian

class ChildModelTestCase(TestCase):
    def setUp(self):
        self.guardian = Guardian.objects.create(
            first_name='John',
            last_name='Doe',
            location='Test Location',
            phone_number='+1234567890'
        )
        self.child = Child.objects.create(
            first_name='Alice',
            last_name='Doe',
            date_of_birth='2022-01-01',
            gender='F',
            guardian=self.guardian
        )

    def test_child_creation(self):
        self.assertEqual(self.child.first_name, 'Alice')
        self.assertEqual(self.child.last_name, 'Doe')
        self.assertEqual(str(self.child), 'Alice Doe (Child of John Doe)')

class GuardianModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()  # Create an APIClient instance
        self.guardian_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'location': 'Test Location',
            'phone_number': '+1234567890'
        }
        self.guardian = Guardian.objects.create(**self.guardian_data)

    def test_guardian_creation(self):
        self.assertEqual(self.guardian.first_name, 'John')
        self.assertEqual(self.guardian.last_name, 'Doe')
        self.assertEqual(self.guardian.location, 'Test Location')
        self.assertEqual(str(self.guardian), 'John Doe')

    def test_register_child(self):
        child_data = {
            'first_name': 'Alice',
            'last_name': 'Doe',
            'date_of_birth': '2022-01-01',
            'gender': 'F',
            'guardian': self.guardian
        }
        response = self.client.post('/api/children/', child_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_children(self):
        child1 = Child.objects.create(
            first_name='Alice',
            last_name='Doe',
            date_of_birth='2022-01-01',
            gender='F',
            guardian=self.guardian
        )
        child2 = Child.objects.create(
            first_name='Bob',
            last_name='Doe',
            date_of_birth='2023-02-02',
            gender='M',
            guardian=self.guardian
        )
        children = self.guardian.children.all()
        self.assertEqual(children.count(), 2)
        self.assertIn(child1, children)
        self.assertIn(child2, children)

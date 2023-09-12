from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from child.models import Child, Guardian
from .serializers import ChildSerializer, GuardianSerializer

def test_create_guardian(self):
    serialized_guardian = GuardianSerializer(data=self.guardian_data)  # Create a serializer instance
    if serialized_guardian.is_valid():
        serialized_guardian.save()
        response = self.client.post('/api/guardians/', self.guardian_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    else:
        self.fail(f"Guardian data is not valid: {serialized_guardian.errors}")

    # Rest of your test methods...

class ChildAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.child_data = {'first_name': 'Child 1', 'age': 5}
        self.child = Child.objects.create(first_name='Child 2', age=7)

    # Rest of your test methods...

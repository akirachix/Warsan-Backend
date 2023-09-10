from django.test import TestCase
from psycopg2 import IntegrityError

# Create your tests here.
from .models import HealthWorker

class HealthWorkerTestCase(TestCase):
    def setUp(self):
        self.worker = HealthWorker(
            first_name="Hassan",
            middle_name="Mohamed",
            last_name="Ali",
            phone_number="+252123456789",
            location="Mogadishu",
            hospital="Hargeisa Hospital",
        )
        self.worker.save()

    def test_full_name(self):
        self.assertEqual(self.worker.full_name(), "Hassan Mohamed Ali")

    def test_str_method(self):
        self.assertEqual(str(self.worker), "Hassan Mohamed Ali")

    def test_unique_phone_number(self):
        # Attempt to create another HealthWorker with the same phone number
        duplicate_worker = HealthWorker(
            first_name="Amina",
            middle_name="Abdi",
            last_name="Hassan",
            phone_number="+252123456789",
            location="Borama",
            hospital="Mogadishu Hospital",
        )
        with self.assertRaises(IntegrityError):
            duplicate_worker.save()

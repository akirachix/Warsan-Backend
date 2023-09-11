from django.test import TestCase
from psycopg2 import IntegrityError
from .models import HealthWorker
from faker import Faker

class HealthWorkerTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_unique_phone_number(self):
        phone_number1 = self.fake.phone_number()
        phone_number2 = self.fake.phone_number()

        worker1 = HealthWorker(
            first_name="Abdullahi",
            last_name="Ali",
            phone_number=phone_number1,
            hospital="Digfeer Hospital",
        )
        worker1.save()

        worker2 = HealthWorker(
            first_name="Fatima",
            last_name="Hassan",
            phone_number=phone_number2,
            hospital="Medina Hospital",
        )
        worker2.save()

        self.assertNotEqual(phone_number1, phone_number2)

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from Healthcare.models import HealthWorker
from .serializers import HealthWorkerSerializer

class HealthWorkerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_health_worker(self):
        data = {
            "first_name": "Amina",
            "middle_name": "Hassan",
            "last_name": "Abdi",
            "location": "Mogadishu",
            "hospital": "Digfeer",
            "phone_number": "+2526189012231"
        }
        response = self.client.post(reverse("healthworker-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HealthWorker.objects.count(), 1)

    def test_list_health_workers(self):
        # Create some HealthWorker instances for testing
        HealthWorker.objects.create(first_name="Ali", middle_name="Mohamed", last_name="Ahmed", location="Bakool", hospital="Bakool Hospital", phone_number="+252617892345")
        HealthWorker.objects.create(first_name="Hassan", middle_name="Omar", last_name="Abdi", location="Mogadishu", hospital="Medina Hospital", phone_number="+252617892563")

        response = self.client.get(reverse("healthworker-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_health_workers(self):
        # Create some HealthWorker instances for testing
        HealthWorker.objects.create(first_name="Abdullahi", middle_name="Omar", last_name="Mohamed", location="Mogadishu", hospital="Medina Hospital", phone_number="+252617892345")
        HealthWorker.objects.create(first_name="Fatima", middle_name="Hassan", last_name="Ali", location="Hargeisa", hospital="Hargeisa Hospital", phone_number="+252617892563")

        # Search for health workers with "Abdullahi" in their name
        response = self.client.get(reverse("healthworker-search"), {"search": "Abdullahi"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "Abdullahi")

    def test_filter_health_workers(self):
        # Create some HealthWorker instances for testing
        HealthWorker.objects.create(first_name="Amina", middle_name="Mohamed", last_name="Hassan", location="Mogadishu", hospital="Digfeer Hospital", phone_number="+252617892345")
        HealthWorker.objects.create(first_name="Hassan", middle_name="Omar", last_name="Ali", location="Hargeisa", hospital="Hargeisa Hospital", phone_number="+252617892563")

        # Filter health workers by location
        response = self.client.get(reverse("healthworker-filter"), {"location": "Mogadishu"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["location"], "Mogadishu")

    def test_update_health_worker(self):
        # Create a HealthWorker instance for testing
        health_worker = HealthWorker.objects.create(
            first_name="Amina",
            middle_name="Hassan",
            last_name="Abdi",
            location="Mogadishu",
            hospital="Digfeer Hospital",
            phone_number="+252617892345"
        )

        updated_data = {
            "first_name": "Updated",
            "middle_name": "UpdatedMiddle",
            "last_name": "Name",
            "location": "Updated Hospital",
            "hospital": "Updated Location",
            "phone_number": "+2526189012231"
        }

        response = self.client.put(reverse("healthworker-detail", args=[health_worker.pk]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the health worker's data has been updated in the database
        updated_health_worker = HealthWorker.objects.get(pk=health_worker.pk)
        self.assertEqual(updated_health_worker.first_name, "Updated")
        self.assertEqual(updated_health_worker.middle_name, "UpdatedMiddle")
        self.assertEqual(updated_health_worker.last_name, "Name")
        self.assertEqual(updated_health_worker.location, "Updated Hospital")
        self.assertEqual(updated_health_worker.hospital, "Updated Location")
        self.assertEqual(updated_health_worker.phone_number, "+2526189012231")

    def test_delete_health_worker(self):
        # Create a HealthWorker instance for testing
        health_worker = HealthWorker.objects.create(
            first_name="Amina",
            middle_name="Hassan",
            last_name="Abdi",
            location="Mogadishu",
            hospital="Digfeer Hospital",
            phone_number="+252617892345"
        )

        response = self.client.delete(reverse("healthworker-detail", args=[health_worker.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HealthWorker.objects.count(), 0)

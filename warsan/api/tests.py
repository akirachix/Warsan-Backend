# from django.test import TestCase

# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from Immunization_Record.models import Immunization_Record

# class ImmunizationRecordAPITest(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_immunization_record(self):
#         data = {
        
    
#         "date_of_administaration": "2023-09-05T06:00:00Z",
#         "next_date_of_administration": "2023-09-06T18:00:00Z"

#         }
#         immunization_record = Immunization_Record.objects.create(**data)
#         response = self.client.post('/api/immunization-records/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_immunization_records(self):
#         response = self.client.get('/api/immunization-records/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_immunization_detail(self):
#         immunization_record = Immunization_Record.objects.create(
            
#         )
#         response = self.client.get(f'/api/immunization-records/{immunization_record.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_immunization_record(self):
#         # Create an immunization record instance for testing
#         immunization_record = Immunization_Record.objects.create(
#             # Initialize the record with some data
#         )
#         data = {
#             # Your data for updating the immunization record
#         }
#         response = self.client.put(f'/api/immunization-records/{immunization_record.id}/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_immunization_record(self):
#         # Create an immunization record instance for testing
#         immunization_record = Immunization_Record.objects.create(
#             # Initialize the record with some data
#         )
#         response = self.client.delete(f'/api/immunization-records/{immunization_record.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from Immunization_Record.models import Immunization_Record

class ImmunizationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse('immunization_record_list_view')  # Replace with your actual view name
        self.detail_url = reverse('immunization_record_detail_view', args=[1])  

    def test_get_immunization_record_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_immunization_record(self):
        data = {
            # Data for creating a new record
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_immunization_record_detail(self):
        response = self.client.get(self.detail_url)

    def test_update_immunization_record(self):
        data = {
            #data for updating the record
        }
        response = self.client.put(self.detail_url, data, format='json')

    def test_delete_immunization_record(self):
        response = self.client.delete(self.detail_url)
        # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

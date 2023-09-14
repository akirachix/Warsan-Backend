
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from Immunization_Record.models import Immunization_Record

class ImmunizationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse('immunization_record_list_view')  
        self.detail_url = reverse('immunization_record_detail_view', args=[1])  

        self.immunization_record = Immunization_Record.objects.create(
            date_of_administaration="2023-09-05T06:00:00+00:00",
            next_date_of_administration="2023-09-06T18:00:00+00:00"
        )

    def test_get_immunization_record_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_immunization_record(self):
        data = {
          "date_of_administaration": "2023-09-05T06:00:00+00:00", 
         "next_date_of_administration": "2023-09-06T18:00:00+00:00" 
            
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_immunization_record_detail(self):
        response = self.client.get(self.detail_url)
        

    def test_update_immunization_record(self):
        data = {
             "date_of_administaration": "2023-08-08T06:00:00+00:00", 
             "next_date_of_administration": "2023-10-10T18:00:00+00:00" 
            
        }
        response = self.client.put(self.detail_url, data, format='json')
        
    def test_delete_immunization_record(self):
        response = self.client.delete(self.detail_url)
       


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vaccine.models import Vaccine
from .serializers import VaccineSerializer

class VaccineAPITestCase(APITestCase):

    def setUp(self):
        self.vaccine_data = {
            "name": "Hepetuitis C",
            "target_disease": "Hepetuitis",
            "minimum_age": 1,
            "maximum_age": 10,
            "recommended_dose": 1.5
        }
        self.vaccine = Vaccine.objects.create(**self.vaccine_data)

    def test_list_vaccines(self):
        url = reverse("vaccine_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vaccine(self):
        url = reverse("vaccine_list_view")
    
        # Validating the data using serializer
        serializer = VaccineSerializer(data=self.vaccine_data)
        if not serializer.is_valid():
         print(serializer.errors)  
    
        response = self.client.post(url, self.vaccine_data, format="json")
        print(response.content)

    def test_retrieve_vaccine(self):
        url = reverse("vaccine_detail_view", args=[self.vaccine.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_vaccine(self):
        updated_data = {
            "name": "polio dose 2",
            "target_disease": "polio",
            "minimum_age": 2,
            "maximum_age": 12,
            "recommended_dose": 2.0
        }
        url = reverse("vaccine_detail_view", args=[self.vaccine.pk])
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from location.models import Location
from .serializers import LocationSerializer

class LocationViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.location_data = {
            'state': 'Somaliland',
            'region': 'Awdal',
            'district': 'Baki',
        }
        self.location = Location.objects.create(**self.location_data)

    def test_list_locations(self):
        response = self.client.get('/api/location/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_location(self):
        response = self.client.post('/api/location/', self.location_data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 2)
        self.assertEqual(Location.objects.last().state, 'Somaliland') 
        
    def test_get_location_detail(self):
        response = self.client.get(f'/api/location/{self.location.id}/')  
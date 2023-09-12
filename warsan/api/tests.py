from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from location.models import Location
from .serializers import LocationSerializer  
# Create your tests here.

class LocationViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()  # Create an API client
        self.location_data = {
            'state': 'Somaliland',
            'region': 'Awdal',
            'district': 'Baki',
           
        }
        self.location = Location.objects.create(**self.location_data)


def test_list_locations(self):
    response = self.client.get('http://127.0.0.1:8000/api/location/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)  

def test_create_location(self):
    response = self.client.post('http://127.0.0.1:8000/api/location/', self.location_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Location.objects.count(), 2)  # One from setUp and one created in the test
    self.assertEqual(Location.objects.last().state, 'Test State')

def test_get_location_detail(self):
    response = self.client.get(f'http://127.0.0.1:8000/api/location/4/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['state'], 'Test State')



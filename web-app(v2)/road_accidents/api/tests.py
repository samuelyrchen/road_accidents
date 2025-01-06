from django.test import TestCase
from rest_framework.test import APIClient
from .models import Accident

# Create your tests here.

class AccidentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.accident = Accident.objects.create(
            accident_index="ACCID573",
            accident_severity=3,
            number_of_vehicles=1,
            number_of_casualties=4,
            date="27/02/2005"
        )

    def test_get_accidents(self):
        response = self.client.get('/accidents/')
        self.assertEqual(response.status_code, 200)

    def test_create_accident(self):
        data = {
            "accident_index": "ACCID6515",
            "location_easting": 342324,
            "location_northing": 342523,
            "longitude": -1.232323,
            "latitude": 45.345345,
            "accident_severity": 3,
            "number_of_vehicles": 2,
            "number_of_casualties": 1,
            "date": "01/02/2023"
        }
        response = self.client.post('/accidents/', data)
        self.assertEqual(response.status_code, 201)
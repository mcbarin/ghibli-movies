from django.test import TestCase
from .utils import get_people_from_ghibli, get_movies_from_ghibli

class CoreViewsTestCase(TestCase):
    def test_movies(self):
        resp = self.client.get('/movies/')
        self.assertEqual(resp.status_code, 200)
    
    def test_ghibli_api(self):
        self.assertGreaterEqual(len(get_movies_from_ghibli()), 0)
    
    def test_ghibli_people(self):
        self.assertGreaterEqual(len(get_people_from_ghibli()), 0)

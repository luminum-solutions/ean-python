from django.test import TestCase
from tests.test_client import APIClientTestCase
from client import APIClient
from django.conf import settings

# Create your tests here.
class DjangoAPICLientTestCase(APIClientTestCase, TestCase):
    def test_with_django_settings_module(self):
        """Test that the API client correctly uses the settings"""
        client = APIClient()
        self.assertEqual(client.api_key, getattr(settings, "EAN_API_KEY"))
        self.assertEqual(client.shared_secret, getattr(settings, "EAN_SHARED_SECRET"))

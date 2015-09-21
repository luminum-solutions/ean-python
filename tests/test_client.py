from client import APIClient
from django.test import TestCase
from django.conf import settings
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"

class APIClientTestCase(TestCase):
    """
    A Test case for the API Client.
    """

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_with_django_settings_module(self):
        """
        Test that the API client correctly uses the settings
        :return:
        """
        client = APIClient()
        self.assertEqual(client.api_key, getattr(settings, "EAN_API_KEY"))
        self.assertEqual(client.shared_secret, getattr(settings, "EAN_SHARED_SECRET"))

    def test_do_request(self):
        """
        Test a request directly
        :return:
        """
        url = self.client.construct_url("hotel", action="list")
        print("Testing url: " + url)
        self.client.request(url)

    def test_resource_locator_creation(self):
        pass

    def test_request(self):
        """Test a request."""
        pass

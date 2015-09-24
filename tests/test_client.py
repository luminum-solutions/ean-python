from client import APIClient
from unittest import TestCase
from unittest.mock import Mock
from resources.abstract_base import AbstractResource


class APIClientTestCase(TestCase):
    """
    A Test case for the API Client.
    """

    def setUp(self):

        class TempHotel(AbstractResource):
            def __str__(self):
                return "hotel"

        self.client = APIClient()
        self.test_hotel = TempHotel()

    def tearDown(self):
        pass

    def test_do_request(self, manual_url=None):
        """Test a request directly"""
        url = self.client.construct_resource_url(self.test_hotel, action="list") or manual_url
        print(url)
        response = self.client.request(url)
        self.assertEqual(response.status, 200)

    def test_resource_locator_creation(self):
        """Test that URL construction works properly"""
        url = self.client.construct_resource_url(self.test_hotel, action="list")
        self.test_do_request(manual_url=url)

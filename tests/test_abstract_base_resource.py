from unittest import TestCase
from client import APIClient
from resources import Hotel
from resources.exceptions import ResourceMethodNotAllowed


class AbstractBaseResourceTestCase(TestCase):
    """
    A Test case for the Abstract Base Resource
    """

    def setUp(self):
        self.client = APIClient()
        self.hotel = Hotel()

    def tearDown(self):
        pass

    def test_not_implemented(self):
        """Test that when a Resource class has not implemented methods, the right exceptions are raised."""
        self.assertRaises(NotImplementedError, self.hotel.create)
        self.assertRaises(NotImplementedError, self.hotel.delete)
        self.assertRaises(NotImplementedError, self.hotel.update)

    def test_not_allowed(self):
        """Test that when a Resource class does not allow certain operations, proper Exceptions are raised."""
        hotel = Hotel()
        hotel.allow_create = False
        hotel.allow_delete = False
        hotel.allow_update = False

        self.assertRaises(ResourceMethodNotAllowed, hotel.create)
        self.assertRaises(ResourceMethodNotAllowed, hotel.delete)
        self.assertRaises(ResourceMethodNotAllowed, hotel.update)

    def test_construct_resource_request_url(self):
        url = self.hotel.construct_resource_request_url('list')
        response = self.client.request(url)
        self.assertEqual(response.status, 200)

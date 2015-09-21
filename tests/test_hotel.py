from unittest import TestCase
from client import APIClient
from resources import Hotel


class HotelResourceTestCase(TestCase):
    """
    A Test case for the Hotel Resource.
    """

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_manual_specified_client(self):
        hotel_with_specified_client = Hotel(client=self.client)
        self.assertEqual(hotel_with_specified_client.client, self.client,
                         "Client passed and the created client are not equal.")

    def test_manual_specified_client_kwargs(self):
        manual_client_args = {
            'protocol': 'https',
            'api_version': '3',
            'domain': 'api.ean.com',
            'shared_secret': 'e4t4bth2anoaj',
            'api_key': '6lrf8qinl5jpuh6a9iagmmiaop'
        }
        hotel_with_specified_client_kwargs = Hotel(client_args=manual_client_args)
        self.assertIsInstance(hotel_with_specified_client_kwargs.client, APIClient,
                              "Hotel client is not an instance of APICLient.")

    def test_get_single(self):
        """Test a request."""
        pass

    def test_list(self):
        """Test a request."""
        pass

from unittest import TestCase
from client import APIClient
from resources import Hotel


class HotelResourceTestCase(TestCase):
    """
    A Test case for the Hotel Resource.
    """

    def setUp(self):
        self.client = APIClient()
        self.hotel = Hotel()

    def tearDown(self):
        pass

    def test_manual_specified_client(self):
        """Test hotel Resource object creation with a manually specified APIClient instance"""
        hotel_with_specified_client = Hotel(manual_client=self.client)
        self.assertEqual(hotel_with_specified_client.client, self.client,
                         "Client passed and the created client are not equal.")

    def test_manual_specified_client_kwargs(self):
        """Test creation of the Hotel resource with manually specified settings through kwargs"""

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
        """Test getting a single hotel"""
        response = self.hotel.get(148505, "09/04/2016", "09/05/2016", (1,))
        self.assertEqual(response.status, 200, "Response was not OK (200)")
        print(response.data)

    def test_list(self):
        """Test getting a list of hotels"""
        response = self.hotel.list("Seattle", "WA", "US", "09/04/2016", "09/05/2016", (1,))
        self.assertEqual(response.status, 200, "Response was not OK (200)")
        print(response.data)

    def test_xml_construct(self):
        """Test the construction of XML for the hotel resource"""
        pass

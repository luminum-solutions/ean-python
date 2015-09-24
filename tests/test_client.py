from client import APIClient
from unittest import TestCase
from unittest.mock import Mock
from resources.abstract_base import AbstractResource


class APIClientTestCase(TestCase):
    """
    A Test case for the API Client.
    """

    def setUp(self):
        class TempHotel(AbstractResource, Mock):
            def __str__(self):
                return "hotel"

            def construct_xml(self, action):
                return "<HotelListRequest><city>Seattle<%2Fcity><stateProvinceCode>WA<%2FstateProvinceCode><countryCode>US<%2FcountryCode><arrivalDate>10%2F20%2F2015<%2FarrivalDate><departureDate>10%2F22%2F2015<%2FdepartureDate><RoomGroup><Room><numberOfAdults>2<%2FnumberOfAdults><%2FRoom><%2FRoomGroup><numberOfResults>25<%2FnumberOfResults><%2FHotelListRequest>"

        self.client = APIClient()
        self.test_hotel = TempHotel()

    def tearDown(self):
        pass

    def test_do_request(self, manual_url=None):
        """Test a request directly"""
        url = self.client.construct_url(self.test_hotel, action="list") or manual_url
        response = self.client.request(url)
        self.assertEqual(response.status, 200)

    def test_resource_locator_creation(self):
        """Test that URL construction works properly"""
        url = self.client.construct_url(self.test_hotel, action="list")
        self.test_do_request(manual_url=url)

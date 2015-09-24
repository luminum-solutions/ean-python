from .abstract_base import AbstractResource


class Hotel(AbstractResource):
    """
    Class that allows interacting with the Hotel resource.
    """

    def list(self, city, state_province_code, country_code, arrival_date, departure_date, rooms=()):
        extra_vars = {
            "city": city,
            "stateProvinceCode": state_province_code,
            "countryCode": country_code,
            "arrivalDate": arrival_date,
            "departureDate": departure_date
        }
        for index, room in enumerate(rooms):
            extra_vars["room%s" % index] = room

        url = self.construct_resource_request_url('list', extra_vars)

        return self.client.request(url)

    def get(self, hotel_id, arrival_date, departure_date, rooms=()):
        extra_vars = {
            "hotelIdList": hotel_id,
            "arrivalDate": arrival_date,
            "departureDate": departure_date
        }
        for index, room in enumerate(rooms):
            extra_vars["room%s" % index] = room

        url = self.construct_resource_request_url('list', extra_vars)

        return self.client.request(url)

    def __str__(self):
        return 'hotel'

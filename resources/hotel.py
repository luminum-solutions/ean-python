import client.client
from .abstract_base import AbstractResource
from lxml import etree


class Hotel(AbstractResource):
    """
    Class that allows interacting with the Hotel resource.
    """

    def __init__(self, manual_client=None, client_args=None):
        self.client = manual_client if manual_client else client.APIClient(**(client_args if client_args else {}))

    def construct_xml(self, action):
        root = etree.Element(self._lookup_action(action))
        root.append(etree.Element('child'))

    def __str__(self):
        return 'hotel'

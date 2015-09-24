from client import APIClient
from .abstract_base import AbstractResource
from lxml import etree


class Hotel(AbstractResource):
    """
    Class that allows interacting with the Hotel resource.
    """
    def __init__(self, client=None, client_args=None):
        self.client = client if client else APIClient(**(client_args if client_args else {}))

    def construct_xml(self, action):
        root = etree.Element('root')
        root.append(etree.Element('child'))


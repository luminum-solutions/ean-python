from abc import ABCMeta
from .exceptions import ResourceMethodNotAllowed
import inspect
import client.client


class AbstractResource(metaclass=ABCMeta):
    """
    An Abstract Base Class for all Resources.
    """

    def __init__(self, manual_client=None, client_args=None):
        self.client = manual_client if manual_client else client.APIClient(**(client_args if client_args else {}))

    allow_create = True
    allow_delete = True
    allow_update = True

    def create(self, *args, **kwargs):
        if not self.allow_create:
            raise ResourceMethodNotAllowed(
                "The %s Resource does not allow a call to %s!" % (str(self.__class__), str(inspect.stack()[0][3])))

    def delete(self, *args, **kwargs):
        if not self.allow_delete:
            raise ResourceMethodNotAllowed(
                "The %s Resource does not allow a call to %s!" % (str(self.__class__), str(inspect.stack()[0][3])))

    def update(self, *args, **kwargs):
        if not self.allow_update:
            raise ResourceMethodNotAllowed(
                "The %s Resource does not allow a call to %s!" % (str(self.__class__), str(inspect.stack()[0][3])))

    def list(self, *args, **kwargs):
        raise NotImplementedError("Every Resource should implement it's own all() method!")

    def get(self, *args, **kwargs):
        raise NotImplementedError("Every Resource should implement it's own get() method!")

    def construct_resource_request_url(self, action=None, extra_vars=None):
        return self.client.construct_resource_url(self, action, extra_vars)

    def __str__(self):
        raise NotImplementedError("All Resources should define a __str__ method for URL construction.")

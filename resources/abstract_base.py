from abc import ABCMeta
from .exceptions import ResourceMethodNotAllowed
import inspect


class AbstractResource(metaclass=ABCMeta):
    """
    An Abstract Base Class for all Resources.
    """

    allow_create = True
    allow_delete = True
    allow_update = True

    def create(self):
        if not self.allow_create:
            raise ResourceMethodNotAllowed(
                "The %s Resource does not allow a call to %s!" % (str(self.__class__), str(inspect.stack()[0][3])))

    def delete(self):
        if not self.allow_delete:
            raise ResourceMethodNotAllowed(
                "The %s Resource does not allow a call to %s!" % (str(self.__class__), str(inspect.stack()[0][3])))

    def update(self):
        if not self.allow_update:
            raise ResourceMethodNotAllowed(
                "The %s Resource does not allow a call to %s!" % (str(self.__class__), str(inspect.stack()[0][3])))

    def all(self):
        raise NotImplementedError("Every Resource should implement it's own all() method!")

    def get(self):
        raise NotImplementedError("Every Resource should implement it's own get() method!")

    def construct_xml(self, action):
        raise NotImplementedError("Every Resource should be able to construct its own XML structure!")

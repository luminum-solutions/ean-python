from client import APIClient


class Hotel(object):
    def __init__(self, client=None, client_args=None):
        self.client = client if client else APIClient(**(client_args if client_args else {}))

    def all(self):
        return self.client.request()

    def one(self):
        return self.client.request()

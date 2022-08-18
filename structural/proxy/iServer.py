""" Subject Interface """
from abc import ABC, abstractmethod


class Server(ABC):

    @abstractmethod
    def handle_request(self, url: str, method: str) -> dict:
        pass

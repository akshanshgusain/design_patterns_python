from abc import ABC, abstractmethod

"""
Command is behavioral design pattern that converts requests or simple operations into objects.
"""

"""
Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information 
about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s 
execution, and support undoable operations.
"""


#  Abstract base command

class Command(ABC):

    @abstractmethod
    def execute(self) -> bool:
        pass


class NoCommand(Command):
    def execute(self) -> bool:
        return True

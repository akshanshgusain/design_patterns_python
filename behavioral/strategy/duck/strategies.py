from abc import ABC, abstractmethod


# Strategies
class IFlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError


class IQuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError


class FlyWithWings(IFlyBehaviour):
    def fly(self):
        print("Flying with Wings")


class FlyNoWay(IFlyBehaviour):
    def fly(self):
        print("Can't Fly")


class Quack(IQuackBehaviour):
    def quack(self):
        print("Quack Quack!")


class Squeak(IQuackBehaviour):
    def quack(self):
        print("Squeak Squeak!")


class MuteDuck(IQuackBehaviour):
    def quack(self):
        print("...")

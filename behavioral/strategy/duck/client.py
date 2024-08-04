from behavioral.strategy.duck.strategies import *


class Duck(ABC):
    def __init__(self, flyBehaviour: IFlyBehaviour, quackBehaviour: IQuackBehaviour):
        self.flyBehaviour: IFlyBehaviour = flyBehaviour
        self.quackBehaviour: IQuackBehaviour = quackBehaviour

    def swim(self):
        print("Fluf Fluf,,, swims away")

    @abstractmethod
    def display(self):
        raise NotImplementedError

    def perform_quack(self):
        self.quackBehaviour.quack()

    def perform_fly(self):
        self.flyBehaviour.fly()

    def set_fly_behaviour(self, flyBehaviour: IFlyBehaviour):
        self.flyBehaviour = flyBehaviour

    def set_quack_behaviour(self, quackBehaviour: IQuackBehaviour):
        self.quackBehaviour = quackBehaviour


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("looks like a Mallard Duck")


class ReadHeadDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Squeak())

    def display(self):
        print("looks like a Read head Duck")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self):
        print("looks like a Rubber Duck")


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), MuteDuck())

    def display(self):
        print("looks like a Decoy Duck")

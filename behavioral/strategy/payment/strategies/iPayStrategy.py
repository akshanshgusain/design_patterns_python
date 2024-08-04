from abc import ABC, abstractmethod


class PayStrategy(ABC):
    @abstractmethod
    def pay(self, payment_amount: float) -> bool:
        pass

    @abstractmethod
    def collect_payment_details(self):
        pass

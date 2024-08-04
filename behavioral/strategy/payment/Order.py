""" """
from behavioral.strategy.payment.strategies.iPayStrategy import PayStrategy

"""
Order class. Doesn't know the concrete payment method (strategy) user has
picked. It uses common strategy interface to delegate collecting payment data
to strategy object.
"""


class Order:

    def __init__(self, total_cost: float = 0, is_close: bool = False):
        self.total_cost: float = total_cost
        self.is_close: bool = is_close

    # Here we could collect and store payment data from the strategy
    def process_order(self, payment_method: PayStrategy):
        payment_method.collect_payment_details()

    def set_total_cost(self, cost: float):
        self.total_cost = cost

    def get_total_cost(self) -> float:
        return self.total_cost

    def is_closed(self) -> bool:
        return self.is_close

    def set_close(self):
        self.is_close = True

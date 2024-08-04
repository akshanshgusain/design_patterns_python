from behavioral.strategy.payment.strategies.iPayStrategy import PayStrategy


class CreditCard:
    def __init__(self, number: str, date: str, cvv: str):
        self.amount: float = 100000
        self.number: str = number
        self.date: str = date
        self.cvv: str = cvv

    def set_amount(self, amount: float):
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount


class PayByCreditCard(PayStrategy):
    def __init__(self):
        self.card = None

    # Collect credit card data.
    def collect_payment_details(self):
        number: str = input("Enter the card number: ")
        date: str = input("Enter the card expiration date 'mm/yy': ")
        cvv: str = input("Enter the CVV code: ")
        self.card = CreditCard(number, date, cvv)

    def card_is_present(self) -> bool:
        return self.card is not None

    # After card validation we can charge customer's credit card.
    def pay(self, payment_amount: float) -> bool:
        if self.card_is_present():
            print(f"Paying {payment_amount} using Credit Card.")
            self.card.set_amount(self.card.get_amount() - payment_amount)
            return True
        else:
            return False

from behavioral.strategy.payment.strategies.iPayStrategy import PayStrategy


class PayByPayPal(PayStrategy):
    DATA_BASE: dict[str: str] = {"edison_brock": "eddie@ag.com", "cyrus_smith": "smith99@ag.com"}

    def __init__(self):
        self.email: str = ""
        self.password: str = ""
        self.signed_in: bool = False

    # Save customer data for future shopping attempts.
    def pay(self, payment_amount: float) -> bool:

        if self.signed_in:
            print(f"Paying {payment_amount} using PayPal")
            return True
        else:
            return False

    def collect_payment_details(self):
        while not self.signed_in:
            self.email = input("Enter the user's email")
            self.password = input("Enter the user's password")
            if self.verify():
                print("Data verification has been successful.")
            else:
                print("Wrong email or password!")

    def set_sign_in(self, signed_in: bool):
        self.signed_in = signed_in

    def verify(self) -> bool:
        if self.password in PayByPayPal.DATA_BASE:
            if PayByPayPal.DATA_BASE[self.password] == self.email:
                self.set_sign_in(True)
        return self.signed_in

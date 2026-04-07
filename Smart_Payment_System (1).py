from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self, original, final):
        print("User:", self.user)
        print("Original Amount:", original)
        print("Final Amount:", final)


class CreditCardPayment(Payment):
    def pay(self, amount):
        fee = amount * 0.02
        gst = fee * 0.18
        final = amount + fee + gst
        self.generate_receipt(amount, final)


class UPIPayment(Payment):
    def pay(self, amount):
        cashback = 50 if amount > 1000 else 0
        final = amount - cashback
        self.generate_receipt(amount, final)


class PayPalPayment(Payment):
    def pay(self, amount):
        fee = amount * 0.03 + 20
        final = amount + fee
        self.generate_receipt(amount, final)


class WalletPayment(Payment):
    def __init__(self, user, balance):
        super().__init__(user)
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            print("Transaction Failed")
        else:
            self.balance -= amount
            self.generate_receipt(amount, amount)


def process_payment(payment, amount):
    payment.pay(amount)


# Example usage
p1 = CreditCardPayment("Harshit")
p2 = UPIPayment("Harshit")
p3 = PayPalPayment("Harshit")
p4 = WalletPayment("Harshit", 500)

process_payment(p1, 1000)
process_payment(p2, 1200)
process_payment(p3, 800)
process_payment(p4, 300)
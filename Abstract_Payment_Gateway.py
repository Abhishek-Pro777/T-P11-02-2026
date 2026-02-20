from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        raise NotImplementedError('Subclasses must implement this method')

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f'Processing credit card payment of Rs.{amount}'
    
class PaypalPayment(PaymentMethod):
    def pay(self, amount):
        return f'Processing credit card payment of Rs.{amount}'

class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        return f'Processing credit card payment of Rs.{amount}'
    
def process_payment(payment_method,amount):
    print(payment_method.pay(amount))

payment=[CreditCardPayment(), PaypalPayment(), CryptoPayment()]
for method in payment:
    process_payment(method,500)
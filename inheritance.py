class Bankaccount:
    bank_name = 'Global Bank'
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited. New balance: {self.balance}')
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f'{amount} withdrawn. New balance: {self.balance}')


class SavingsAccount(Bankaccount):
    interest_rate = 0.05

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}")

class CurrentAccount(Bankaccount):
    overdraft_limit = 1000

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            print(f'{amount} withdrawn. Balance: {self.balance}')
        else:
            print('Overdraft limit exceeded!')

sa=SavingsAccount('James', 50000)
sa.add_interest()
ca=CurrentAccount('James', 50000)
ca.withdraw(1000)
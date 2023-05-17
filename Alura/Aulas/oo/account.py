
class Account:

    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit
        self.__bank_code = "001"

    def extract(self):
        print(f"Your balance is {self.__balance, self.__owner}")

    def deposit(self, value):
        self.__balance += value

    def __drawable(self, value_withdraw):
        amount_to_withdraw = (self.__balance + self.__limit)
        return value_withdraw <= amount_to_withdraw

    def withdraw(self, value):
        if self.__drawable(value):
            self.__balance -= value
        else:
            print("The amount you're trying to withdraw is bigger than you balance + you limit")

    def transfer(self, value, destination_account):
        self.withdraw(value)
        destination_account.deposit(value)
        print(f"transfer of {value} reals made from the account from {self.__owner} to {destination_account.__owner}")

    @property
    def balance(self):
        return self.__balance

    @property
    def number(self):
        return self.__number

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"


# account = Account(123, "Nico", 55.5, 1000)
# account2 = Account(456, "Marco", 100, 1000)
# account2.withdraw(1000)
# account2.transfer(10, account)
# print(account.balance)
# print(account2.balance)
# account.extract()
# account2.extract()
# account.limit = 1500
# account2.limit = 2000
# print(account.limit)
# print(account2.limit)
print(Account.bank_code())

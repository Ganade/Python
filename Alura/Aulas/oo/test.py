
def create_account(number, owner, balance, limit):
    account = {"number": number, "Owner": owner, "balance": balance, "limit": limit}
    return account


def deposit(account, amount):
    account["balance"] += amount


def withdraw(account, amount):
    account["balance"] -= amount


def extract(account):
    print(f"Your balance is {account['account']}")

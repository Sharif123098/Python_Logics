class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def get_balance(self):
        print(f"{self.name} — Account: {self.account_number} — Balance: NPR {self.balance}")


accounts_data = [
    ("Ramesh Thapa",  "A001", 5000),
    ("Sunita Karki",  "A002", 0),
    ("Bikash Rai",    "A003", 12000),
]

accounts = []
for name, acc_num, balance in accounts_data:
    accounts.append(BankAccount(name, acc_num, balance))

accounts[1].deposit(3000)
accounts[2].withdraw(15000)
accounts[0].withdraw(2000)

for acc in accounts:
    acc.get_balance()
class ATMSimulator:
    def __init__(self, initial_balance=1000.0):
        # Starting the user off with a default balance of $1000
        self.balance = initial_balance

    def check_balance(self):
        print(f"\n[BALANCE] Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n[SUCCESS] Successfully deposited ${amount:.2f}.")
            self.check_balance()
        else:
            print("\n[ERROR] Invalid amount. Please deposit a positive value.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\n[ERROR] Insufficient funds!")
        elif amount <= 0:
            print("\n[ERROR] Invalid amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"\n[SUCCESS] Successfully withdrew ${amount:.2f}.")
            self.check_balance()

def main():
    atm = ATMSimulator()
    print("=== Welcome to the Python ATM Simulator ===")
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("\nPlease select an option (1-4): ").strip()
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: $"))
                atm.deposit(amount)
            except ValueError:
                print("\n[ERROR] Invalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                atm.withdraw(amount)
            except ValueError:
                print("\n[ERROR] Invalid input. Please enter a valid number.")
        elif choice == '4':
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
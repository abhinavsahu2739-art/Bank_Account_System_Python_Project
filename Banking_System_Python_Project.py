class BankAccount:
    def __init__(self,balance:float=0.0) -> None:
        self.balance=balance

    def deposit(self,amount:float) ->None:
        if amount>0:
            self.balance+=amount # add the amount to the balance
            print(f"You have deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")
    def withdraw(self,amount:float) -> None:
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount # withdraw the amount from the balance
                print(f"You have withdrawn ${amount:.2f}.Your new balance is ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Your current balance is ${self.balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def check_balance(self) -> float:
        return self.balance

def main() -> None:
    account = BankAccount(1000.0)  # Create an instance of the BankAccount class
    while True:
        print("Welcome to the Banking System!")
        print("Please select an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice=="1":
            try:
                amount=float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input !!!!! . Please enter a valid number.")
        elif choice=="2":
            try:
                amount=float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input !!!!!!. Please enter a valid number.")
        elif choice=="3":
            print(f"Your balance is ${account.check_balance():.2f}.")
        elif choice=="4":
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__=="__main__":
    main()


    

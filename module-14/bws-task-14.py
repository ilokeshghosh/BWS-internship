class Bank:

    def __init__(self, initial_amt=0.00):
        self.bal = initial_amt

    def log_transaction(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tbal: {self.bal}\n")

    def withdrawal(self, amt):
        try:
            amt = float(amt)
        except ValueError:
            amt = 0
        if amt:
            self.bal = self.bal - amt
            self.log_transaction(f"Withdrew {amt}")

    def deposit(self, amt):
        try:
            amt = float(amt)
        except ValueError:
            amt = 0
        if amt:
            self.bal = self.bal + amt
            self.log_transaction(f"Deposited {amt}")

account = Bank(1000)
while True:
    try:
        action = input("Withdrawal(1) or Deposit(2) ? ")
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        break

    if action in ["1", "2"]:
        if action == "1":
            amt = input("How much do you want to take out? ")
            account.withdrawal(amt)
        else:
            amt = input("How much do you want to put in? ")
            account.deposit(amt)

        print("Your balance is", account.bal)
    else:
        print("That is not a valid action. Try again.")

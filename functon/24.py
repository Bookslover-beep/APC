#24.Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.

balance = 0
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append(f"Deposited: {amount}")

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient Balance"
    balance -= amount
    history.append(f"Withdrawn: {amount}")
    return f"Successfully withdrawn: {amount}"

def balance_enquiry():
    return balance

def transaction_history():
    return history

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Transaction History")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
        print(f"Deposited successfully. Current Balance: {balance}")
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        print(withdraw(amount))
    elif choice == '3':
        print(f"Current Balance: {balance_enquiry()}")
    elif choice == '4':
        print("--- Transaction History ---")
        hx = transaction_history()
        if hx:
            for record in hx:
                print(f" - {record}")
        else:
            print("No transactions yet.")
    elif choice == '5':
        print("Exiting Bank System.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
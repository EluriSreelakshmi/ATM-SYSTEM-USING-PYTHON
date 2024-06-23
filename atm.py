def check_balance(balance):
    """
    Displays the current balance of the user's account.

    """
    print("Your Current Balance is:", balance, "Rupees only")

def deposit(balance):
    """
    Allows the user to deposit money into their account and view their balance after deposit.

    """
    damount = int(input("Enter your Deposit amount: "))
    balance += damount
    print("Successfully Deposited :) . Your new balance is:", balance, "Rupees only")
    return balance

def withdraw(balance):
    """
    Allows the user to withdraw money from their account and view their balance after withdrawl.

    """
    amount = int(input("Enter the Withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction Successful :) . Your new balance is:", balance, "Rupees only")
    else:
        print(" Sorry Insufficient Balance :( . Your current balance is:", balance, "Rupees only")
    return balance

def change_pin(pin):
    """
    Allows the user to change their PIN.

    """
    new_pin = int(input("Enter the new PIN: "))
    confirm_pin = int(input("Confirm the new PIN: "))
    if new_pin == confirm_pin:
        print("PIN changed successfully!")
        return new_pin
    else:
        print("PIN mismatch. Please try again.")
        return pin

def transfer_funds(balance):
    """
    Allows the user to transfer funds to another account.

    """
    recipient_account = input("Enter the recipient's account number: ")
    transfer_amount = int(input("Enter the amount to transfer: "))
    if transfer_amount <= balance:
        balance -= transfer_amount
        print("Funds transferred successfully to", recipient_account, ". Your new balance is:", balance, "Rupees only")
    else:
        print("Insufficient Balance. Your current balance is:", balance, "Rupees only")
    return balance

def main():
    """
    The main function that handles the ATM operations.
    """
    pin = 1098
    balance = 50000
    
    print('INSERT YOUR CARD ')
    confirm_pin = int(input("Enter Your Pin: "))

    if pin == confirm_pin:
        print("Enter 1 for Balance Inquiry")
        print("Enter 2 for Money Withdrawal")
        print("Enter 3 for Money Deposit")
        print("Enter 4 to Change PIN")
        print("Enter 5 to Transfer Funds")
        
        option = int(input("Select an option (1/2/3/4/5): "))

        if option == 1:
            check_balance(balance)
        elif option == 2:
            balance = withdraw(balance)
        elif option == 3:
            balance = deposit(balance)
        elif option == 4:
            pin = change_pin(pin)
        elif option == 5:
            balance = transfer_funds(balance)
        else:
            print("Invalid Option")
    else:
        print("Invalid PIN")

    print("Thank You, Visit Again")


if __name__ == "__main__":
    main()

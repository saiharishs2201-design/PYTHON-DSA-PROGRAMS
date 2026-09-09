#chatgpt
balance = 5000
pin = 1234

print("===== ATM MACHINE =====")

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is ₹", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
                print("New balance: ₹", balance)
            else:
                print("Invalid amount.")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: ₹"))
            if amount > 0 and amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance: ₹", balance)
            elif amount > balance:
                print("Insufficient balance.")
            else:
                print("Invalid amount.")

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")
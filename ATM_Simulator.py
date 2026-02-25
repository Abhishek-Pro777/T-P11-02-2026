balance = 1000

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited")

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect cash")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")
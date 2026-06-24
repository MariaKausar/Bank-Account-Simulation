name = input("Enter account holder name = ")
balance = int(input("Enter initial balance = "))

while True:
    print("\n--- Bank Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    menu_option = input("Enter option = ")

    if menu_option == "1":
        print("Your balance is =", balance)

    elif menu_option == "2":
        amount = int(input("Enter deposit amount = "))
        balance += amount
        print("New balance =", balance)

    elif menu_option == "3":
        amount = int(input("Enter withdraw amount = "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. New balance =", balance)
        else:
            print("Insufficient balance")

    elif menu_option == "4":
        print("Thank you for using bank system")
        break

    else:
        print("Invalid option")
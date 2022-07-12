username = input("What is your username? \n")

allowed_users = ["xyluz", "xychromosomes", "ghost"]
saved_passwords = ["xyluzPassword", "xychromosomesPassword", "ghostPassword"]
account_balances = [10000, 500000, 2000]

if username in allowed_users:

    user_id = allowed_users.index(username)
    password = input("Your password? \n")

    if password == saved_passwords[user_id]:
        balance = account_balances[user_id]
        print(f"\nWelcome {username.title()}!")
        print(f"Your balance is ${balance:,.2f}\n")

        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Contact us")

        selected_option = input("Please select an option: ")

        if selected_option == "1":
            amount_to_withdraw = int(input("\nHow much do you want to withdraw? \n$"))
            if amount_to_withdraw > balance:
                print("Insufficient funds. Please try again.")
            elif amount_to_withdraw < 1000:
                print("Cannot withdraw less than $1,000. Please try again.")
            elif amount_to_withdraw > 50000:
                print("Cannot withdraw more than $50,000 at a time. Please try again.")
            else:
                balance -= amount_to_withdraw
                print(f"Take your cash: ${amount_to_withdraw:,.2f}")
                print(f"Your balance is ${balance:,.2f}")
                print("Have a great day!")

        elif selected_option == "2":
            amount_to_deposit = int(input("\nHow much you want to deposit? \n$"))

            if amount_to_deposit < 1000:
                print("Cannot deposit less than $1,000")
            else:
                balance += amount_to_deposit
                print(f"Successfully deposited ${amount_to_deposit:,.2f} into your account.")
                print(f"Your balance is ${balance:,.2f}")
                print("Have a great day!")

        elif selected_option == "3":
            complaint = input("\nWhat is your suggestion/enquiry/report? \n")
            print("Thank you for your time.")
            print("Have a great day!")

        else:
            print("Invalid option. Please try again.")      

    else:
        print("Password incorrect. Please try again.")

else:
    print("Name not found. Please try again.")

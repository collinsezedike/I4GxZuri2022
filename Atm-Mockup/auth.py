import random

database = {}


def init():
    print("\nWelcome to Blood Bank")
    print("...where your money bleeds.")

    valid_option = False
    while not valid_option:
        print("\nDo you have an account with us?\nNo: 0, Yes: 1")
        has_account = input(">")  
        valid_option = True # so that I don't have to do this in the if and elif individually 
        if has_account == "0":
            register()
        elif has_account == "1":
            login()
        else:
            valid_option = False
            print("Please enter a valid number!")


def register():
    print("\nCreating a new user account...\n")
    first_name = input("Enter your first name: \n>").title()
    last_name = input("Enter your last name: \n>").title()
    email = input("Enter your email address: \n>")
    password = input("Enter a password: \n>")
    confirm_password = input("Confirm entered password: \n>")

    while password != confirm_password:
        print("...\nPassword confirmation unsuccessful!")        
        password = input("Enter a password: \n>")
        confirm_password = input("Confirm entered password: \n>")
    else:
        account_number = generate_account_number()
        print("Account number generated!\n")
        database[account_number] = {
            "first name": first_name,
            "last name": last_name,
            "email": email,
            "password": password
        }
    print(f"Successfully created an account for {first_name} {last_name}")
    print(f"Your account number is {account_number}")
    login()


def login():
    print("This is the login function")
    bank_operations(database[0])


def generate_account_number():
    print("\nGenerating acoount number...")
    return random.randrange(1000000000,9999999999)


def bank_operations(user: dict):
    print(f"Welcome {user['first name']}")


init()

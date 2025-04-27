user_data = {}
balance = 500.00

# Function to register a new user
def register():
    print("\nRegistration Process:")
    while True:
        username = input("Enter a new username: ")
        if username in user_data:
            print("Username already exists. Please choose a different username.")
        else:
            password = input("Enter a new password: ")
            user_data[username] = password
            print(f"Registration successful! Welcome {username}.")
            break

# Function to handle the login process
def login():
    print("\nLogin Process:")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in user_data and user_data[username] == password:
            print(f"Login successful! Welcome {username}.")
            return username
        else:
            print("Invalid credentials, please try again.")

# Function to display the current balance
def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

# Function to handle money withdrawal
def withdraw_money():
    global balance
    withdraw_amount = float(input("Enter amount to withdraw: $"))

    if withdraw_amount > balance:
        print("Insufficient balance.")
    elif withdraw_amount <= 0:
        print("Invalid amount entered.")
    else:
        balance -= withdraw_amount
        print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")

# Function to display the ATM menu and process user choices
def atm_menu():
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option, please select 1, 2, or 3.")

# Main program starts here
def main():
    print("Welcome to the ATM!")

    # Ask user if they want to register or login
    while True:
        print("\n1. Register")
        print("2. Login")
        choice = input("Choose an option (1/2): ")

        if choice == "1":
            register()
        elif choice == "2":
            if not user_data:
                print("No users registered yet. Please register first.")
            else:
                username = login()
                atm_menu()
                break
        else:
            print("Invalid option, please select 1 or 2.")

if __name__ == "__main__":
    main()

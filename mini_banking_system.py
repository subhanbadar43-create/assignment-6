def check_balance(balance):
    print(f"\nYour current balance is: Rs. {balance}")
    return balance


def deposit(balance, amount):
    if amount > 0:
        balance = balance + amount
        print(f"\nDeposit successful! Rs. {amount} added.")
        print(f"New balance: Rs. {balance}")
    else:
        print("\nInvalid amount. Deposit must be greater than 0.")
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("\nInvalid amount. Withdrawal must be greater than 0.")
    elif amount > balance:
        print("\nTransaction rejected. Insufficient balance.")
    elif (balance - amount) < 1000:
        print("\nTransaction rejected. Balance cannot go below Rs. 1000.")
    else:
        balance = balance - amount
        print(f"\nWithdrawal successful! Rs. {amount} withdrawn.")
        print(f"New balance: Rs. {balance}")
    return balance


def calculate_loan_eligibility(age, salary, credit_score):
    print("\n----- Loan Eligibility Result -----")
    if age >= 21 and salary >= 50000 and credit_score >= 650:
        print("Congratulations! You are eligible for the loan.")
    else:
        print("Sorry, you are not eligible for the loan.")
        if age < 21:
            print("- Age must be 21 or above.")
        if salary < 50000:
            print("- Salary must be at least Rs. 50,000.")
        if credit_score < 650:
            print("- Credit score must be at least 650.")


def main():
    balance = 5000  # starting balance

    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Loan Eligibility")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)

        elif choice == "4":
            age = int(input("Enter your age: "))
            salary = float(input("Enter your salary: "))
            credit_score = int(input("Enter your credit score: "))
            calculate_loan_eligibility(age, salary, credit_score)

        elif choice == "5":
            print("\nThank you for using the Bank System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()

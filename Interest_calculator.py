def ask_name():
    name = input("What is your name? ").capitalize()
    return name

# Chatbot Functions
def calculate_expenses(expenses):
    sum_total = sum(expenses)
    return sum_total

def calculate_savings(income, expenses):
    total_savings = income - expenses
    return total_savings

def simple_interest(principal, rate, time):
    simple_interest = principal * (rate / 100) * time
    return simple_interest

def compound_interest(principal, rate, times_compounded, years):
    compound_interest = principal * ((1 + rate / (100 * times_compounded)) ** (times_compounded * years))
    return compound_interest

# Main Command Handling
command = input("Which command would you like to run? Options: expenses, ask_name, calculate_savings, simple_interest, compound_interest: ")

if command == "expenses":
    num_expenses = int(input("How many expenses do you have?"))
    expenses = []
    for i in range(num_expenses):
        expenses = float(input(f"expense {i+1}:"))
        expenses.append(expenses)
    print(f"Total Expenses: {calculate_expenses(expenses)}")

elif command == "ask_name":
    name = ask_name()
    print(f"Hello, {name}!")

elif command == "calculate_savings":
    income = float(input("Enter your income: "))
    expenses = float(input("Enter your total expenses: "))
    savings = calculate_savings(income, expenses)
    print(f"Your total savings are: {savings}")

elif command == "simple_interest":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))
    si = simple_interest(principal, rate, time)
    print(f"The simple interest is: {si}")

elif command == "compound_interest":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual rate of interest: "))
    times_compounded = int(input("Enter the number of times interest is compounded per year: "))
    years = float(input("Enter the number of years: "))
    ci = compound_interest(principal, rate, times_compounded, years)
    print(f"The compound interest is: {ci}")

else:
    print("Invalid command. Please try again.")

#Mini Expense Tracker
print("Welcome to mini expense tracker")
print("1. Add expense")
print("2. Total expenses")
print("3. Exit")

list_of_expenses = []

while True:
    choice = input("Enter your choice: ")
    if choice == "3":
        print("Bye Bye!")
        break

    if choice == "1":
        quantity = int(input("Enter your count of expenses: "))
        for i in range(1,quantity+1):
            expense = input("Enter your expense: ")
            amount = float(input("Enter your expense amount: "))
            dict_of_expenses = {
                "expense" : expense,
                "amount" : amount
            }
            list_of_expenses.append(dict_of_expenses)

    elif choice == "2":
        total = 0
        for i in list_of_expenses:
            total = total + i["amount"]
        print(total)
    

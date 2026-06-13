def calculate_summary(transactions):

    total_income = 0
    total_expense = 0

    for t in transactions:
        if t["type"] == "Income":
            total_income += t["amount"]
        elif t["type"] == "Expense":
            total_expense += t["amount"]

    balance = total_income - total_expense

    return total_income, total_expense, balance

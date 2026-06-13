from datetime import datetime


class Transaction:
    def __init__(self, amount, t_type, description="", date=None, transaction_id=None):
        self.id = transaction_id or int(datetime.now().timestamp())
        self.amount = float(amount)
        self.type = t_type  # "Income" or "Expense"
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "type": self.type,
            "description": self.description,
            "date": self.date
        }

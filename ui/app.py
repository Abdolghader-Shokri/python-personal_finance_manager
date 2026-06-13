import tkinter as tk
from tkinter import ttk, messagebox

from models.transaction import Transaction
from services import storage_service, finance_service


class FinanceApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")
        self.root.geometry("1000x500")

        self.transactions = storage_service.load_transactions()

        self.build_ui()
        self.refresh_table()
        self.update_summary()

    def build_ui(self):

        form_frame = ttk.LabelFrame(self.root, text="Add Transaction")
        form_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(form_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Type:").grid(row=0, column=2, padx=5, pady=5)

        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(
            form_frame,
            textvariable=self.type_var,
            values=["Income", "Expense"],
            state="readonly"
        )
        self.type_combo.grid(row=0, column=3, padx=5, pady=5)
        self.type_combo.current(0)

        ttk.Label(form_frame, text="Description:").grid(row=0, column=4, padx=5, pady=5)
        self.desc_entry = ttk.Entry(form_frame, width=25)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=5)

        add_btn = ttk.Button(form_frame, text="Add", command=self.add_transaction)
        add_btn.grid(row=0, column=6, padx=5, pady=5)

        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10)

        columns = ("Amount", "Type", "Description", "Date")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True)

        summary_frame = ttk.LabelFrame(self.root, text="Summary")
        summary_frame.pack(fill="x", padx=10, pady=10)

        self.income_label = ttk.Label(summary_frame, text="Total Income: 0")
        self.income_label.pack(side="left", padx=20)

        self.expense_label = ttk.Label(summary_frame, text="Total Expense: 0")
        self.expense_label.pack(side="left", padx=20)

        self.balance_label = ttk.Label(summary_frame, text="Balance: 0")
        self.balance_label.pack(side="left", padx=20)

    def add_transaction(self):

        amount = self.amount_entry.get().strip()
        t_type = self.type_var.get()
        description = self.desc_entry.get().strip()

        if not amount:
            messagebox.showwarning("Warning", "Amount is required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        transaction = Transaction(amount, t_type, description)

        self.transactions.append(transaction.to_dict())

        storage_service.save_transactions(self.transactions)

        self.clear_form()
        self.refresh_table()
        self.update_summary()

    def refresh_table(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        for t in self.transactions:
            self.tree.insert(
                "",
                tk.END,
                values=(t["amount"], t["type"], t["description"], t["date"])
            )

    def update_summary(self):

        income, expense, balance = finance_service.calculate_summary(self.transactions)

        self.income_label.config(text=f"Total Income: {income}")
        self.expense_label.config(text=f"Total Expense: {expense}")
        self.balance_label.config(text=f"Balance: {balance}")

    def clear_form(self):
        self.amount_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.type_combo.current(0)

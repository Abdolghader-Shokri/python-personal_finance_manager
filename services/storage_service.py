import json
import os


FILE_PATH = "data/transactions.json"


def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")


def load_transactions():
    ensure_data_dir()

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_transactions(transactions):
    ensure_data_dir()

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(transactions, f, indent=4)

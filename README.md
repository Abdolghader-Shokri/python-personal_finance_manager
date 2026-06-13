```markdown
# Personal Finance Manager (Python Desktop App)

A simple but well‑structured **Personal Finance Manager** built with Python and Tkinter.  
This project demonstrates clean project architecture, separation of concerns, and GUI application development practices such as modular design, service layers, data modeling, and JSON‑based data persistence.

The application allows users to **record income and expenses, view transaction history, and calculate financial summaries** through a graphical interface while storing the data locally in a JSON file.

This project was designed as a learning exercise to practice building maintainable Python desktop applications using a modular structure similar to real software projects.

---

## Features

- Add income and expense transactions
- View a list of financial transactions
- Display transaction history in a table
- Calculate total income
- Calculate total expenses
- Calculate current balance
- Persistent data storage using JSON
- Simple and clean graphical interface with Tkinter
- Modular architecture (UI, models, services)
- Separation of UI logic and financial calculation logic

---

## Technologies

- Python 3
- Tkinter for GUI development
- JSON for local data storage
- Standard Python libraries (datetime, json, os)

---

## Project Structure

```
personal_finance_manager/
│
├── main.py
│
├── models/
│   └── transaction.py
│
├── services/
│   ├── storage_service.py
│   └── finance_service.py
│
└── ui/
    └── app.py
```

*(Note: The `data/transactions.json` file is generated automatically within the project directory upon the first save.)*

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/personal-finance-manager.git
cd personal-finance-manager
```

Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate
```

---

## Running the Application

Run the program using:

```
python main.py
```

The graphical interface will open, allowing you to record and manage financial transactions.

---

## Data Storage

All transactions are stored locally in `data/transactions.json` (created automatically).  
Each transaction is serialized as a JSON object containing:

- id
- amount
- type
- description
- date

---

## Learning Goals

This project was built to practice:

- Building desktop applications with Tkinter
- Designing modular Python project structures
- Separating UI logic from business logic
- Implementing service layers for financial calculations
- Managing application data with JSON storage
- Applying object‑oriented programming principles
- Writing maintainable and scalable Python code

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
```
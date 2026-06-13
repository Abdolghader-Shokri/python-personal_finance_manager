import tkinter as tk
from ui.app import FinanceApp


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()

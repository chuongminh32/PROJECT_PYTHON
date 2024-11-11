
from tkinter import Tk
from gui.login_page import LoginPage  # Import lớp LoginPage từ file login_page.py

if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()

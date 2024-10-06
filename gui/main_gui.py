import tkinter as tk
from tkinter import messagebox

def run_gui():
    root = tk.Tk()
    root.title("Quản lý điểm thi THPT")

    label = tk.Label(root, text="Chào mừng đến với ứng dụng quản lý điểm thi THPT!")
    label.pack(pady=20)

    def on_exit():
        if messagebox.askokcancel("Thoát", "Bạn có chắc chắn muốn thoát?"):
            root.quit()

    exit_button = tk.Button(root, text="Thoát", command=on_exit)
    exit_button.pack(pady=20)

    root.mainloop()
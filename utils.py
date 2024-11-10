import os
import subprocess
from tkinter import messagebox, Toplevel, Button, Label, StringVar, Entry, Frame, Canvas, Scrollbar, LEFT, RIGHT, VERTICAL, BOTH, Y
from PIL import Image, ImageTk
import pandas as pd
from modules.data_crud import read_data, create_data

def setup_window(title, size, bg_color="white"):
    """Thiết lập cửa sổ với tiêu đề và kích thước."""
    window = Toplevel()
    window.title(title)
    window.geometry(size)
    window.configure(background=bg_color)
    return window

def load_image(path, size=(40, 40)):
    """Tải và thay đổi kích thước hình ảnh."""
    if os.path.exists(path):
        image = Image.open(path).resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    else:
        messagebox.showerror("Error", f"File not found: {path}")
        return None

def create_button(parent, text, command, y_position):
    """Tạo nút trong khung menu."""
    button = Button(parent, text=text, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
    button.place(x=0, y=y_position, width=200, height=50)
    button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
    button.bind("<Leave>", lambda e: button.config(bg="#242533"))
    return button

def display_data(data):
    """Hiển thị dữ liệu trong cửa sổ mới dưới dạng bảng."""
    display_window = setup_window("Dữ liệu sinh viên", "800x400")

    frame = Frame(display_window)
    frame.pack(fill="both", expand=True)

    v_scrollbar = Scrollbar(frame, orient="vertical")
    h_scrollbar = Scrollbar(frame, orient="horizontal")

    columns = data[0]  # Lấy hàng đầu tiên làm tên cột
    tree = ttk.Treeview(frame, columns=columns, show="headings",
                        yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    v_scrollbar.config(command=tree.yview)
    h_scrollbar.config(command=tree.xview)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center', width=150)

    for row in data[1:]:
        tree.insert("", "end", values=row)

    tree.grid(row=0, column=0, sticky="nsew")
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

def validate_entries(entries, fields):
    """Kiểm tra xem tất cả các trường đã được nhập."""
    for i, (label_text, placeholder) in enumerate(fields):
        if entries[label_text].get() == placeholder or entries[label_text].get() == "":
            return False, label_text
    return True, None

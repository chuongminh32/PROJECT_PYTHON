import os
# from tkinter import messagebox, Tk, Label, Button, LabelFrame, LEFT
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import csv
from pathlib import Path
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_visualization import plot_grade  
from modules.data_cleaning import handle_missing_value, remove_duplicates, correct_formatting, save_to_cleaned_data_file
from modules.data_crud import read_data, create_data, update_data, delete_data  # Cập nhật đường dẫn import nếu cần


def open_view_page():
    """Hàm để mở trang quản lý sinh viên."""
    global view_root
    view_root = Tk()
    view_root.title("Quản lý sinh viên")
    view_root.geometry("1000x550+300+200")
    view_root.configure(background="white")

    # === Icon === 
    logo_path = os.path.join("images", "logo.png")
    logo_image = Image.open(logo_path).resize((20, 20))
    logo_dash = ImageTk.PhotoImage(logo_image)

    # === Title ===
    title = Label(view_root, text="Students View", image=logo_dash, padx=10, compound=LEFT,
                  bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
    title.place(x=0, y=0, relwidth=1, height=80)

    # === Back button ===
    back_button = Button(view_root, text="Back", border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
                         command=lambda: return_to_home(view_root))
    back_button.place(x=20, y=100, width=90, height=30)

    # === Menu === 
    M_Frame = LabelFrame(view_root, text="Menu", bg="white", font=("Arial", 12, "bold"))
    M_Frame.place(x=0, y=150, width=200, relheight=1)

    # Thêm các nút vào khung menu
    create_menu_button(M_Frame, "Visualization", Visualization, 0)
    create_menu_button(M_Frame, "Cleaning", Cleaning, 70)
    create_menu_button(M_Frame, "Update", update, 140)
    create_menu_button(M_Frame, "Read", read, 210)

    # === BACKGROUND ===
    bg_path = os.path.join("images", "bg_manage.png")
    bg_image = Image.open(bg_path).resize((1150, 700))
    bg_manage = ImageTk.PhotoImage(bg_image)
    background_label = Label(view_root, image=bg_manage)
    background_label.place(x=200, y=80, relwidth=1, relheight=1)

    view_root.mainloop() # Chạy chương trình

def return_to_home(view_root):
    """Hàm để quay lại trang chính."""
    view_root.destroy()
    subprocess.run(["python", "gui/home_page.py"])

def create_menu_button(parent, text, command, y_position):
    """Hàm để tạo nút trong khung menu."""
    button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
    button.place(x=0, y=y_position, width=200, height=50)
    button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
    button.bind("<Leave>", lambda e: button.config(bg="#242533"))
    return button

def Visualization():
    """Hàm trực quan hóa dữ liệu."""
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "data_demo.csv"
    df = pd.read_csv(file_path)
    plot_grade(df)

def Cleaning():
    """Hàm làm sạch dữ liệu."""
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "data_demo.csv"
    result_path = project_root / "data" / "data_clean.csv"
    if (remove_duplicates(file_path) and handle_missing_value(result_path) and correct_formatting(result_path)):
        messagebox.showinfo("Success", "Data cleaned successfully!")
    else:
        messagebox.showinfo("Error", "Data cleaning failed!")

def read():

    """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra một cửa sổ mới dưới dạng bảng."""
    try:
        data = read_data()  # Gọi hàm để lấy dữ liệu từ file CSV
        if data is None:
            messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
            return

        # Tạo một cửa sổ mới để hiển thị bảng dữ liệu
        display_window = Toplevel()
        display_window.title("Dữ liệu sinh viên")
        display_window.geometry("700x550+300+200")

        # Tạo khung chứa Treeview và thanh cuộn
        frame = ttk.Frame(display_window)
        frame.pack(fill="both", expand=True)

        # Tạo thanh cuộn dọc và ngang
        v_scrollbar = ttk.Scrollbar(frame, orient="vertical")
        h_scrollbar = ttk.Scrollbar(frame, orient="horizontal")

        # Tạo Treeview để hiển thị bảng dữ liệu
        columns = data[0]  # Lấy hàng đầu tiên làm tên cột
        tree = ttk.Treeview(frame, columns=columns, show="headings",
                             yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Đặt thanh cuộn cho Treeview
        v_scrollbar.config(command=tree.yview)
        h_scrollbar.config(command=tree.xview)

        # Đặt tiêu đề cho mỗi cột và tùy chỉnh độ rộng
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Đặt độ rộng cột 150

        # Thêm dữ liệu vào bảng với đường kẻ
        for index, row in enumerate(data[1:]):
            if index % 2 == 0:
                tree.insert("", "end", values=row, tags=("evenrow",))
            else:
                tree.insert("", "end", values=row, tags=("oddrow",))

        # Thiết lập màu sắc cho các hàng
        tree.tag_configure("evenrow", background="#f9f9f9")  # Màu nền cho hàng chẵn
        tree.tag_configure("oddrow", background="white")      # Màu nền cho hàng lẻ

        # Đặt Treeview và thanh cuộn vào khung
        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Thiết lập tỷ lệ mở rộng cho Treeview
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    
    

def update():
    """Hàm để tạo sinh viên mới."""
    messagebox.showinfo("Create", "Chức năng đang được phát triển")

def delete():
    """Hàm để tạo sinh viên mới."""
    messagebox.showinfo("Create", "Chức năng đang được phát triển")

if __name__ == "__main__":
    open_view_page()

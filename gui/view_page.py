import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sys
import pandas as pd
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_visualization import plot_grade, plot_grade_btn, plot_age, plot_age_btn, plot_country, plot_country_btn, plot_gender, plot_gender_btn, plot_point_rating, plot_point_rating_btn, plot_personal, plot_personal_btn, plot_point_old, plot_point_old_btn
"""
Mô tả:
    Đây là một trang hiển thị dữ liệu và biểu đồ được xây dựng bằng thư viện Tkinter trong Python.
    Trang này cho phép người dùng xem dữ liệu và các biểu đồ phân tích liên quan đến sinh viên.
Thư viện sử dụng:
    - tkinter: Thư viện GUI tiêu chuẩn của Python.
    - tkinter.messagebox: Thư viện con của tkinter để hiển thị các hộp thoại thông báo.
    - tkinter.ttk: Thư viện con của tkinter để tạo các widget nâng cao.
    - subprocess: Thư viện để chạy các tiến trình con.
    - os: Thư viện cung cấp nhiều chức năng liên quan đến hệ điều hành.
    - PIL (Pillow): Thư viện xử lý hình ảnh.
    - pandas: Thư viện để xử lý và phân tích dữ liệu.
    - matplotlib: Thư viện để vẽ biểu đồ.
    - numpy: Thư viện hỗ trợ tính toán khoa học.
Lớp:
    - ViewPage: Lớp đại diện cho trang hiển thị dữ liệu và biểu đồ.
Phương thức của lớp ViewPage:
    - __init__(self, root): Khởi tạo đối tượng ViewPage.
    - setup_window(self): Thiết lập cửa sổ chính của ứng dụng.
    - create_logo(self): Tạo logo cho ứng dụng.
    - create_menu(self): Tạo menu cho ứng dụng.
    - create_content_frame(self): Tạo vùng hiển thị nội dung.
    - create_menu_button(self, parent, text, command, y_position): Tạo nút menu.
    - clear_content_frame(self): Xóa nội dung trong khung hiển thị nội dung.
    - plot_grade_btn(self, filepath): Vẽ biểu đồ phân bố điểm số dựa trên cột trong dữ liệu.
    - read(self): Hiển thị dữ liệu trong file ra bảng trong cửa sổ hiện tại.
    - plot_grade_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ điểm học tập trung bình.
    - plot_conuntry_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ quốc gia.
    - plot_age_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ độ tuổi.
    - plot_gender_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ giới tính.
    - plot_point_old_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ điểm vs tuổi.
    - plot_personal_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ cá nhân.
    - plot_point_rating_detail(self, FILE_PATH): Hiển thị chi tiết biểu đồ điểm vs năng lực.
    - plot_grade(self): Vẽ biểu đồ điểm học tập trung bình.
    - plot_country(self): Vẽ biểu đồ quốc gia.
    - plot_age(self): Vẽ biểu đồ độ tuổi.
    - plot_gender(self): Vẽ biểu đồ giới tính.
    - plot_point_old(self): Vẽ biểu đồ điểm vs tuổi.
    - plot_personal(self): Vẽ biểu đồ cá nhân.
    - plot_point_rating(self): Vẽ biểu đồ điểm vs năng lực.
    - exit_program(self): Thoát chương trình.
Hàm:
    - main(): Hàm chính để khởi chạy ứng dụng.
"""


class ViewPage:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()
        self.create_content_frame()
        self.canvas = None
        root.resizable(False, False)  # Cho phép cửa sổ thay đổi kích thước

    def setup_window(self):
        """Thiết lập cửa sổ chính."""
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")

    def create_logo(self):
        """Tạo logo cho ứng dụng."""
        logo_path = os.path.join("images", "logo_fit.png")
        logo_image = Image.open(logo_path).resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo_image)

        Label(self.root, text="Trực Quan", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        """Tạo menu cho ứng dụng."""
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=170, relheight=1)

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Độ tuổi", self.plot_age, 0)
        self.create_menu_button(M_Frame, "Quốc gia", self.plot_country, 50)
        self.create_menu_button(M_Frame, "Điểm số", self.plot_grade, 100)
        self.create_menu_button(M_Frame, "Giới tính", self.plot_gender, 150)
        self.create_menu_button(
            M_Frame, "Điểm vs Năng lực", self.plot_point_rating, 200)
        self.create_menu_button(M_Frame, "Cá nhân", self.plot_personal, 250)
        self.create_menu_button(M_Frame, "Điểm vs Tuổi",
                                self.plot_point_old, 300)
        self.create_menu_button(M_Frame, "Quay về", self.exit_program, 350)

    def create_content_frame(self):
        """Tạo vùng hiển thị nội dung."""
        self.content_frame = Frame(self.root, bg="lightgrey")
        # Dùng relwidth và relheight để mở rộng theo kích thước cửa sổ
        # self.content_frame.place(x=200, y=80, relwidth=1, relheight=1)
        self.content_frame.place(x=170, y=80, width=830, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        """Tạo nút menu."""
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
                        command=command)
        button.place(x=0, y=y_position, width=170, height=40)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def clear_content_frame(self):
        """Xóa nội dung trong khung hiển thị nội dung."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def plot_grade_btn(self, filepath):
        """Vẽ biểu đồ phân bố điểm số dựa trên cột trong dữ liệu."""
        plot_grade_btn(filepath)

    def read(self):
        """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra bảng trong cửa sổ hiện tại."""
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        try:
            file_path = "data/data_clean.csv"  # Đường dẫn đến file CSV
            data = read_data(file_path)  # Lấy dữ liệu từ file CSV

            if not data:
                messagebox.showinfo(
                    "Thông báo", "Không có dữ liệu để hiển thị.")
                return

            # Tạo thanh cuộn dọc và ngang cho Treeview
            v_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical")
            h_scrollbar = ttk.Scrollbar(
                self.content_frame, orient="horizontal")

            # Tạo Treeview để hiển thị bảng dữ liệu
            columns = data[0]  # Lấy hàng đầu tiên làm tên cột
            tree = ttk.Treeview(self.content_frame, columns=columns, show="headings",
                                yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

            # Đặt tiêu đề cho mỗi cột và tùy chỉnh độ rộng
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center', width=150)  # Độ rộng cố định

            # Thêm dữ liệu vào bảng
            for row in data[1:]:
                tree.insert("", "end", values=row)

            # Đặt Treeview và thanh cuộn vào content_frame
            tree.grid(row=0, column=0, sticky="nsew")
            # Cần thêm cột này để thanh cuộn dọc hoạt động
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            # Cần thêm hàng này để thanh cuộn ngang hoạt động
            h_scrollbar.grid(row=1, column=0, sticky="ew")

            # Kết nối thanh cuộn với Treeview
            v_scrollbar.config(command=tree.yview)  # Cuộn dọc
            h_scrollbar.config(command=tree.xview)  # Cuộn ngang

            # Thiết lập tỷ lệ mở rộng cho Treeview
            self.content_frame.grid_rowconfigure(0, weight=1)  # Cột 0
            self.content_frame.grid_columnconfigure(0, weight=1)  # Hàng 0

        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def plot_grade_detail(self, FILE_PATH):
        plot_grade_btn(FILE_PATH)

    def plot_conuntry_detail(self, FILE_PATH):
        plot_country_btn(FILE_PATH)

    def plot_age_detail(self, FILE_PATH):
        plot_age_btn(FILE_PATH)

    def plot_gender_detail(self, FILE_PATH):
        plot_gender_btn(FILE_PATH)


    def plot_point_old_detail(self, FILE_PATH):
        plot_point_old_btn(FILE_PATH)

    def plot_personal_detail(self, FILE_PATH):
        plot_personal_btn(FILE_PATH)

    def plot_point_rating_detail(self, FILE_PATH):
        plot_point_rating_btn(FILE_PATH)

    def plot_grade(self):
        """Vẽ biểu đồ điểm học tập trung bình"""
        self.clear_content_frame()  # Xóa tất cả widget trong content_frame
        FILE_PATH = 'data/data_clean.csv'  # Đường dẫn tới file CSV
        plot_grade(FILE_PATH, self.content_frame)

        # lambda: hàm vô danh, không tên, không cần khai báo trước, chỉ sử dụng 1 lần
        # Tạo các nút động
        Button(self.content_frame, text="Detail", command=lambda: self.plot_grade_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def plot_country(self):
        self.clear_content_frame()
        FILE_PATH = 'data/data_clean.csv'  # Đường dẫn tới file CSV
        plot_country(FILE_PATH, self.content_frame)
        Button(self.content_frame, text="Detail", command=lambda: self.plot_conuntry_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def plot_age(self):
        self.clear_content_frame()
        FILE_PATH = 'data/data_clean.csv'  # Đường dẫn tới file CSV
        plot_age(FILE_PATH, self.content_frame)
        Button(self.content_frame, text="Detail", command=lambda: self.plot_age_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def plot_gender(self):
        self.clear_content_frame()
        FILE_PATH = 'data/data_clean.csv'  # Đường dẫn tới file CSV
        plot_gender(FILE_PATH, self.content_frame)
        Button(self.content_frame, text="Detail", command=lambda: self.plot_gender_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def plot_point_old(self):
        self.clear_content_frame()
        FILE_PATH = 'data/data_clean.csv'
        plot_point_old(FILE_PATH, self.content_frame)
        Button(self.content_frame, text="Detail", command=lambda: self.plot_point_old_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def plot_personal(self):
        self.clear_content_frame()
        FILE_PATH = 'data/data_clean.csv'
        plot_personal(FILE_PATH, self.content_frame)
        Button(self.content_frame, text="Detail", command=lambda: self.plot_personal_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def plot_point_rating(self):
        self.clear_content_frame()
        FILE_PATH = 'data/data_clean.csv'
        plot_point_rating(FILE_PATH, self.content_frame)
        Button(self.content_frame, text="Detail", command=lambda: self.plot_point_rating_detail("data/data_clean.csv"),
               width=15).place(x=90, y=4, height=30, width=100)

    def exit_program(self):
        """Hàm cho chức năng Exit - Thoát chương trình."""
        self.root.destroy()
        subprocess.run(["python", "gui/home_page.py"])


def main():
    root = Tk()
    app = ViewPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()

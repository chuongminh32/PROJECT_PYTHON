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

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data
from modules.student_function import stu_filter, stu_top, stu_find, read_students_from_csv

"""
Chương trình quản lý sinh viên sử dụng giao diện Tkinter.
Các thư viện sử dụng:
- tkinter: Thư viện tiêu chuẩn của Python để tạo giao diện đồ họa.
- os: Thư viện cung cấp các chức năng để tương tác với hệ điều hành.
- tkinter.messagebox: Thư viện con của tkinter để hiển thị các hộp thoại thông báo.
- tkinter.ttk: Thư viện con của tkinter cung cấp các widget nâng cao.
- PIL (Pillow): Thư viện xử lý hình ảnh.
- sys: Thư viện cung cấp các chức năng để tương tác với trình thông dịch Python.
- pandas: Thư viện phân tích dữ liệu mạnh mẽ.
- subprocess: Thư viện để chạy các tiến trình con.
- matplotlib.backends.backend_tkagg: Thư viện con của matplotlib để tích hợp với Tkinter.
- matplotlib.pyplot: Thư viện vẽ đồ thị.
Các module tự định nghĩa:
- modules.data_crud: Module chứa các hàm để đọc dữ liệu.
- modules.student_comparison: Module chứa các hàm để lọc, tìm kiếm và so sánh sinh viên.
Lớp Student:
- __init__(self, root): Khởi tạo đối tượng Student với cửa sổ gốc.
- setup_window(self): Thiết lập cửa sổ chính của ứng dụng.
- create_logo(self): Tạo logo cho ứng dụng.
- create_menu(self): Tạo menu cho ứng dụng.
- create_content_frame(self): Tạo vùng hiển thị nội dung.
- create_menu_button(self, parent, text, command, y_position): Tạo nút menu.
- clear_content_frame(self): Xóa nội dung trong khung hiển thị nội dung.
- read(self): Hiển thị dữ liệu từ file CSV ra bảng trong cửa sổ hiện tại.
- stu_filter(self): Lọc sinh viên dựa trên trường và giá trị nhập vào.
- stu_find(self): Tìm sinh viên có điểm cao nhất cho từng môn.
- stu_top(self): Hiển thị top 10 sinh viên có tổng điểm cao nhất.
- exit_program(self): Thoát chương trình và quay về trang chủ.
Hàm main():
- Khởi tạo cửa sổ Tkinter và chạy ứng dụng.
"""

class Student:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()
        self.create_content_frame()
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

        Label(self.root, text="Sinh Viên", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        """Tạo menu cho ứng dụng."""
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Điểm cao nhất", self.stu_find, 0)
        self.create_menu_button(M_Frame, "Lọc sinh viên", self.stu_filter, 75)
        self.create_menu_button(M_Frame, "Top sinh viên", self.stu_top, 150)
        self.create_menu_button(M_Frame, "Đọc data", self.read, 220)
        self.create_menu_button(M_Frame, "Quay về", self.exit_program, 290)

    def create_content_frame(self):
        """Tạo vùng hiển thị nội dung."""
        self.content_frame = Frame(self.root, bg="lightgrey")
        # Dùng relwidth và relheight để mở rộng theo kích thước cửa sổ
        # self.content_frame.place(x=200, y=80, relwidth=1, relheight=1)
        self.content_frame.place(x=200, y=80, width=800, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        """Tạo nút menu."""
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
                        command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def clear_content_frame(self):
        """Xóa nội dung trong khung hiển thị nội dung."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        return True

    def read(self):
        """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra bảng trong cửa sổ hiện tại."""
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        try:
            file_path = "data/data_clean.csv"  # Đường dẫn đến file CSV
            data = pd.read_csv(file_path)  # Đọc dữ liệu từ file CSV

            if data.empty:
                messagebox.showinfo(
                    "Thông báo", "Không có dữ liệu để hiển thị.")
                return

            # Tạo thanh cuộn dọc và ngang cho Treeview
            v_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical")
            h_scrollbar = ttk.Scrollbar(
                self.content_frame, orient="horizontal")

            # Tạo Treeview để hiển thị bảng dữ liệu
            columns = list(data.columns)  # Lấy tên cột từ DataFrame
            tree = ttk.Treeview(self.content_frame, columns=columns, show="headings",
                                yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

            # Đặt tiêu đề cho mỗi cột và tùy chỉnh độ rộng
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center', width=150)  # Độ rộng cố định

            # Thêm dữ liệu vào bảng
            for _, row in data.iterrows():
                tree.insert("", "end", values=list(row))

            # Đặt Treeview và thanh cuộn vào content_frame
            tree.grid(row=0, column=0, sticky="nsew")
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            h_scrollbar.grid(row=1, column=0, sticky="ew")

            # Kết nối thanh cuộn với Treeview
            v_scrollbar.config(command=tree.yview)  # Cuộn dọc
            h_scrollbar.config(command=tree.xview)  # Cuộn ngang

            # Thiết lập tỷ lệ mở rộng cho Treeview
            self.content_frame.grid_rowconfigure(0, weight=1)
            self.content_frame.grid_columnconfigure(0, weight=1)

        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")
        
    def stu_filter(self):
        self.clear_content_frame()
        global df
        df = pd.read_csv("data/data_clean.csv")

        # Khung nhập tên trường và giá trị cần tìm
        field_name_label = tk.Label(
            self.content_frame, text="Nhập tên trường cần lọc:")
        field_name_label.pack(padx=5, pady=5)

        self.field_name_entry = tk.Entry(self.content_frame, width=30)
        self.field_name_entry.pack(padx=5, pady=5)

        field_value_label = tk.Label(
            self.content_frame, text="Nhập giá trị cần tìm:")
        field_value_label.pack(padx=5, pady=5)

        self.field_value_entry = tk.Entry(self.content_frame, width=30)
        self.field_value_entry.pack(padx=5, pady=5)

        # Hàm tìm kiếm dữ liệu dựa trên trường và giá trị nhập vào
        def search_by_field():
            # Trường cần lọc (ví dụ: 'nationality')
            field_name = self.field_name_entry.get()
            field_value = self.field_value_entry.get()  # Giá trị lọc (ví dụ: 'China')

            if field_name not in df.columns:
                messagebox.showerror("Error", f"Trường '{
                                     field_name}' không tồn tại trong dữ liệu.")
                return False

            # Lọc dữ liệu dựa trên trường và giá trị nhập vào
            result_data = df[df[field_name].astype(
                str).str.lower() == field_value.lower()]

            if result_data.empty:
                messagebox.showerror("Error", f"Không tìm thấy dữ liệu với {
                                     field_name} = '{field_value}'")

                # Xóa bảng kết quả cũ nếu không có dữ liệu mới
                for item in self.tree.get_children():
                    self.tree.delete(item)

                return False  # Trả về False nếu không tìm thấy dữ liệu

            # Hiển thị tất cả các dòng có kết quả phù hợp trong bảng Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)  # Xóa kết quả cũ

            # Hiển thị tất cả các dòng có kết quả phù hợp trong bảng Treeview
            for _, row in result_data.iterrows():
                # Chuyển dữ liệu từ DataFrame thành list để hiển thị trên Treeview
                self.tree.insert("", tk.END, values=list(row))

           # Nút tìm kiếm
        search_button = tk.Button(
            self.content_frame, text="Tìm kiếm", command=lambda: search_by_field())
        search_button.pack(pady=5)

        # Tạo bảng Treeview để hiển thị kết quả
        columns = list(df.columns)  # Lấy tên cột từ file CSV
        self.tree = ttk.Treeview(
            self.content_frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)  # Đặt tiêu đề cho từng cột
            # Đặt kích thước cột tự động
            self.tree.column(col, width=150, anchor="center")

        # Tạo thanh cuộn cho Treeview
        v_scrollbar = tk.Scrollbar(
            self.content_frame, orient="vertical", command=self.tree.yview)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar = tk.Scrollbar(
            self.content_frame, orient="horizontal", command=self.tree.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        self.tree.configure(yscrollcommand=v_scrollbar.set,
                            xscrollcommand=h_scrollbar.set)

        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def stu_find(self):
        self.clear_content_frame()
        global df
        df = pd.read_csv("data/data_clean.csv")

        # Tìm sinh viên có điểm cao nhất cho từng môn
        subjects = ['math.grade', 'english.grade', 'sciences.grade']
        top_students = {subject: df.loc[df[subject].idxmax()]
                        for subject in subjects}

        for subject, student in top_students.items():
            # Lấy tên môn học từ tên cột
            subject_name = subject.split('.')[0].capitalize()
            info_label = tk.Label(self.content_frame, text=f"Sinh viên có điểm {
                                  subject_name} cao nhất:", font=("Arial", 12, "bold"), bg="lightgrey")
            info_label.pack(pady=5)

            student_info = f"ID: {student['id']}\n" \
                f"Tên: {student['name']}\n" \
                f"Quốc tịch: {student['nationality']}\n" \
                f"Điểm {subject_name}: {student[subject]}\n" \
                f"Tuổi: {student['age']}\n" \


            student_info_label = tk.Label(
                self.content_frame, text=student_info, font=("Arial", 12), bg="lightgrey")
            student_info_label.pack(pady=5)

    def stu_top(self):
        self.clear_content_frame()
        global df
        df = pd.read_csv("data/data_clean.csv")

        field_name_label = tk.Label(self.content_frame, text="TOP 10 STUDENTS BEST SCORE", font=(
            "Arial", 17, "bold"), bg="lightgrey")
        field_name_label.pack(padx=5, pady=5)

        # Tính tổng điểm cho mỗi sinh viên
        df['total_score'] = df[['math.grade',
                                'english.grade', 'sciences.grade']].sum(axis=1)

        # Sắp xếp sinh viên theo tổng điểm giảm dần và lấy top 10
        top_students = df.nlargest(10, 'total_score')

        # Tạo bảng Treeview để hiển thị kết quả
        columns = list(top_students.columns)  # Lấy tên cột từ DataFrame
        tree = ttk.Treeview(self.content_frame,
                            columns=columns, show="headings", height=10)

        for col in columns:
            tree.heading(col, text=col)  # Đặt tiêu đề cho từng cột
            # Đặt kích thước cột tự động
            tree.column(col, width=150, anchor="center")

        # Thêm dữ liệu vào bảng
        for _, row in top_students.iterrows():
            tree.insert("", tk.END, values=list(row), tags=("red",))

        # Tạo thanh cuộn cho Treeview
        v_scrollbar = tk.Scrollbar(
            self.content_frame, orient="vertical", command=tree.yview)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar = tk.Scrollbar(
            self.content_frame, orient="horizontal", command=tree.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=v_scrollbar.set,
                       xscrollcommand=h_scrollbar.set)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

    def exit_program(self):
        """Hàm cho chức năng Exit - Thoát chương trình."""
        self.root.destroy()
        subprocess.run(["python", "gui/home_page.py"])


def main():
    root = Tk()
    app = Student(root)
    root.mainloop()


if __name__ == "__main__":
    main()

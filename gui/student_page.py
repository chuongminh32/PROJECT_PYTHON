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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data
from modules.student_function import sort_desc_gpa, sort_increase_age, plot_distribution, plot_correlation, show_top_students
"""
Mô tả:
    Đây là một trang quản lý sinh viên được xây dựng bằng thư viện Tkinter trong Python. 
    Trang này cho phép người dùng xem, lọc, sắp xếp và hiển thị biểu đồ dữ liệu sinh viên.
Thư viện sử dụng:
    - tkinter: Thư viện GUI tiêu chuẩn của Python.
    - tkinter.messagebox: Thư viện con của tkinter để hiển thị các hộp thoại thông báo.
    - tkinter.ttk: Thư viện con của tkinter để tạo các widget nâng cao.
    - subprocess: Thư viện để chạy các tiến trình con.
    - os: Thư viện cung cấp nhiều chức năng liên quan đến hệ điều hành.
    - PIL (Pillow): Thư viện xử lý hình ảnh.
    - pandas: Thư viện để xử lý dữ liệu.
    - matplotlib: Thư viện để vẽ biểu đồ.
Lớp:
    - Student: Lớp đại diện cho trang quản lý sinh viên.
Phương thức của lớp Student:
    - __init__(self, root): Khởi tạo đối tượng Student.
    - setup_window(self): Thiết lập cửa sổ chính của ứng dụng.
    - create_logo(self): Thêm logo vào cửa sổ chính.
    - create_menu(self): Tạo menu chức năng cho ứng dụng.
    - create_content_frame(self): Tạo khung nội dung để hiển thị dữ liệu.
    - create_menu_button(self, parent, text, command, y_position): Tạo các nút trong menu.
    - clear_content_frame(self): Xóa nội dung hiện tại trong khung nội dung.
    - read(self, file_path="data/data_clean.csv", title="DANH SÁCH SINH VIÊN"): Đọc và hiển thị dữ liệu từ file CSV.
    - create_treeview(self, parent_frame, dataframe, title): Tạo bảng hiển thị dữ liệu.
    - plot_distribution(self, filepath, column_name): Vẽ biểu đồ phân bố điểm số dựa trên cột trong dữ liệu.
    - chart(self): Hiển thị giao diện các biểu đồ.
    - stu_filter(self): Hiển thị giao diện lọc sinh viên.
    - search_by_field(self): Tìm kiếm sinh viên theo trường và giá trị nhập vào.
    - show_top_total(self): Hiển thị giao diện top sinh viên có tổng điểm cao nhất.
    - top_rating(self): Hiển thị top sinh viên có tổng điểm đánh giá cao nhất.
    - top_grade(self): Hiển thị top sinh viên có tổng điểm các môn cao nhất.
    - top_grade_rating(self): Hiển thị top sinh viên có tổng điểm đánh giá và môn học cao nhất.
    - show_top_students_by_column(self, columns, new_column, title): Hiển thị top sinh viên theo cột chỉ định.
    - show_top_students(self): Hiển thị giao diện top sinh viên điểm cao.
    - top_10_math(self): Hiển thị top 10 sinh viên điểm toán cao nhất.
    - top_10_science(self): Hiển thị top 10 sinh viên điểm khoa học cao nhất.
    - top_10_english(self): Hiển thị top 10 sinh viên điểm tiếng anh cao nhất.
    - top_10_language(self): Hiển thị top 10 sinh viên điểm ngôn ngữ cao nhất.
    - top_10_portfolio(self): Hiển thị top 10 sinh viên điểm đánh giá hồ sơ cao nhất.
    - top_10_coverletter(self): Hiển thị top 10 sinh viên điểm đánh giá thư xin việc cao nhất.
    - top_10_refletter(self): Hiển thị top 10 sinh viên điểm đánh giá thư giới thiệu cao nhất.
    - sort_stu(self): Hiển thị giao diện sắp xếp sinh viên.
    - sort_by_age(self): Sắp xếp sinh viên theo tuổi.
    - sort_by_avg(self): Sắp xếp sinh viên theo GPA.
    - sort_and_display(self, file_path, title, sort_function): Sắp xếp và hiển thị dữ liệu sinh viên.
    - exit_program(self): Thoát khỏi chương trình và quay về trang chủ.
Hàm:
    - main(): Hàm chính để khởi chạy ứng dụng.
"""


class Student:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()
        self.create_content_frame()
        root.resizable(False, False)

    def setup_window(self):
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")

    def create_logo(self):
        logo_path = os.path.join("images", "logo_fit.png")
        logo_image = Image.open(logo_path).resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo_image)
        Label(self.root, text="Thống kê", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        M_Frame = LabelFrame(self.root, text="Menu", bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)
        menu_items = [
            ("Điểm cao nhất", self.show_top_total, 0),
            ("Lọc sinh viên", self.stu_filter, 75),
            ("Top sinh viên", self.show_top_students, 150),
            ("Sắp xếp", self.sort_stu, 220),
            ("Biểu đồ", self.chart, 290),
            ("Quay về", self.exit_program, 360)
        ]
        for text, command, y_position in menu_items:
            self.create_menu_button(M_Frame, text, command, y_position)

    def create_content_frame(self):
        self.content_frame = Frame(self.root, bg="lightgrey")
        self.content_frame.place(x=200, y=80, width=800, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", cursor="hand2", font=("Arial", 12, "bold"),
                        command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))
    
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        return True

    def read(self, file_path="data/data_clean.csv", title="DANH SÁCH SINH VIÊN"):
        self.clear_content_frame()
        try:
            data = pd.read_csv(file_path)
            if data.empty:
                messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
                return
            self.create_treeview(self.content_frame, data, title)
        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def create_treeview(self, parent_frame, dataframe, title):
        # Clear any previous widgets
        for widget in parent_frame.winfo_children():
            widget.destroy()

        # Create the title label
        title_label = tk.Label(parent_frame, text=title, font=("Arial", 17, "bold"), bg="lightgrey")
        title_label.pack(padx=5, pady=5)
            
        # Create the back button based on the title
        if "TỔNG" in title:
            back_btn = tk.Button(parent_frame, text="Quay lại", command=self.show_top_total)
            back_btn.place(x=10, y=10)
        elif title == "DANH SÁCH SINH VIÊN SẮP XẾP THEO TUỔI" or title == "DANH SÁCH SINH VIÊN SẮP XẾP THEO GPA":
            back_btn = tk.Button(parent_frame, text="Quay lại", command=self.sort_stu)
            back_btn.place(x=10, y=10)
        else:
            back_btn = tk.Button(parent_frame, text="Quay lại", command=self.show_top_students)
            back_btn.place(x=10, y=10)
                
       
        columns = list(dataframe.columns)  # columns = ['name', 'age', 'math.grade', ...]
          # Tạo treeview để hiển thị dữ liệu sinh viên sau khi lọc 
        tree = ttk.Treeview(parent_frame, columns=columns, show = "headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")
        for _, row in dataframe.iterrows(): # Duyệt qua từng dòng dữ liệu
            tree.insert("", tk.END, values=list(row)) #
        y = tk.Scrollbar(parent_frame, orient="vertical", command=tree.yview) # Tạo thanh cuộn dọc(vertical)
        # command=tree.yview: Liên kết thanh cuộn với phương thức yview của Treeview, cho phép thanh cuộn điều khiển việc cuộn dọc của Treeview.
        y.pack(side="right", fill="y") # Đặt thanh cuộn vào khung 
        x = tk.Scrollbar(parent_frame, orient="horizontal", command=tree.xview) # Tạo thanh cuộn ngang(horizontal)
        x.pack(side="bottom", fill="x") # Đặt thanh cuộn vào khung
        # Cấu hình treeview để có thanh cuộn dọc và ngang
        # yscrollcommand=y.set: Liên kết thanh cuộn dọc với Treeview, cho phép thanh cuộn dọc cập nhật khi nội dung Treeview thay đổi.
        tree.configure(yscrollcommand=y.set, xscrollcommand=x.set)
        tree.pack(padx=10, pady=10,fill="both", expand=True) # fill = "both": Treeview sẽ mở rộng theo cả chiều ngang và chiều cao 



    def plot_distribution(self, filepath, column_name):
        """Vẽ biểu đồ phân bố điểm số dựa trên cột trong dữ liệu."""
        plot_distribution(filepath, column_name)

    def chart(self):
        """Hiển thị giao diện các biểu đồ."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="BIỂU ĐỒ PHÂN BỐ ĐIỂM SỐ", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)

        # Danh sách các nút và cột tương ứng
        buttons = [
            ("TOÁN", lambda: self.plot_distribution("data/data_clean.csv", "math.grade")),
            ("KHOA HỌC", lambda: self.plot_distribution("data/data_clean.csv", "sciences.grade")),
            ("ANH", lambda: self.plot_distribution("data/data_clean.csv", "english.grade")),
            ("NGÔN NGỮ", lambda: self.plot_distribution("data/data_clean.csv", "language.grade")),
            ("TƯƠNG QUAN", lambda: plot_correlation("data/data_clean.csv"))
        ]

        # Tạo các nút động
        for text, command in buttons:
            Button(self.content_frame, text=text, cursor="hand2", command=command, width=15).pack(padx=5, pady=10)

    def stu_filter(self):
        self.clear_content_frame()  # Xóa nội dung cũ
        global df # df là biến toàn cục chứa dữ liệu sinh viên
        df = pd.read_csv("data/data_clean.csv") # Đọc dữ liệu từ file CSV
        
        # Combobox chọn trường cần lọc
        field_name_label = tk.Label(self.content_frame, text="Chọn tên trường cần lọc:")
        field_name_label.pack(padx=5, pady=5)

        options = list(df.columns)  # Lấy danh sách các cột
        self.field_name_combobox = ttk.Combobox(self.content_frame, values=options, state="readonly", width=27)
        self.field_name_combobox.pack(padx=5, pady=5)

        # Gắn sự kiện thay đổi lựa chọn
        self.field_name_combobox.bind("<<ComboboxSelected>>", lambda event: self.update_field_values(df))

        # Combobox nhập giá trị cần tìm
        field_value_label = tk.Label(self.content_frame, text="Nhập giá trị cần tìm:")
        field_value_label.pack(padx=5, pady=5)

        self.field_value_combobox = ttk.Combobox(self.content_frame, values=[], state="readonly", width=27)
        self.field_value_combobox.pack(padx=5, pady=5)

        # nut xoa du lieu
        button_clear = Button(self.content_frame, text="Clear", command=self.clear_data_treeview, cursor="hand2").place(x=10, y=120, width=70, height=40)
        columns = list(df.columns) # Lấy danh sách các cột trong dữ liệu, ví dụ ['name', 'age', 'math.grade', ...]

        # nút search
        search_button = tk.Button(self.content_frame, text="Tìm kiếm",cursor="hand2", command=self.search_by_field).pack(pady=5)

        # Tạo treeview để hiển thị dữ liệu sinh viên sau khi lọc 
        self.tree = ttk.Treeview(self.content_frame, columns=columns, show = "headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
            
        y = tk.Scrollbar(self.content_frame, orient="vertical", command=self.tree.yview) # Tạo thanh cuộn dọc(vertical)
        # command=self.tree.yview: Liên kết thanh cuộn với phương thức yview của Treeview, cho phép thanh cuộn điều khiển việc cuộn dọc của Treeview.
        y.pack(side="right", fill="y") # Đặt thanh cuộn vào khung 
        x = tk.Scrollbar(self.content_frame, orient="horizontal", command=self.tree.xview) # Tạo thanh cuộn ngang(horizontal)
        x.pack(side="bottom", fill="x") # Đặt thanh cuộn vào khung
        # Cấu hình treeview để có thanh cuộn dọc và ngang
        # yscrollcommand=y.set: Liên kết thanh cuộn dọc với Treeview, cho phép thanh cuộn dọc cập nhật khi nội dung Treeview thay đổi.
        self.tree.configure(yscrollcommand=y.set, xscrollcommand=x.set)
        self.tree.pack(padx=10, pady=10,fill="both", expand=True) # fill = "both": Treeview sẽ mở rộng theo cả chiều ngang và chiều cao 
        
    def update_field_values(self, df):
        """
        Cập nhật các giá trị tùy chọn cho combobox 'field_value_combobox' dựa trên trường đã chọn.
        :param df: DataFrame chứa dữ liệu.
        """
        selected_field = self.field_name_combobox.get()
        options_value = []

        # Tùy chỉnh giá trị gợi ý cho từng cột
        if selected_field == "age":
            options_value = ["< 20", "20-25", "25-30", "> 30"]
        elif selected_field == "gender":
            options_value = df[selected_field].dropna().unique().tolist()
        elif selected_field == "score":
            options_value = ["< 50", "50-70", "70-90", "> 90"]
        else:
            options_value = df[selected_field].dropna().unique().tolist()  # Lấy các giá trị duy nhất của cột

        # Cập nhật giá trị cho combobox
        self.field_value_combobox["values"] = options_value
        self.field_value_combobox.set("")  # Reset giá trị đang hiển thị
    def clear_data_treeview(self):
            # Xóa dữ liệu cũ
            for item in self.tree.get_children():
                self.tree.delete(item)

    def search_by_field(self):
        data = pd.read_csv("data/data_clean.csv")
        field_name = self.field_name_combobox.get()
        field_value = self.field_value_combobox.get()
        if field_name not in df.columns:
            messagebox.showerror("Error", f"Trường '{field_name}' không tồn tại trong dữ liệu.")
            return False
        if field_name == 'age' and field_value == "20-25":
            result_data = data[(data["age"] >= 20) & (data["age"] <= 25)]
        elif field_name == 'age' and field_value == "25-30":
            result_data = data[(data["age"] > 25) & (data["age"] <= 30)]
        elif field_name == 'age' and field_value == "> 30":
            result_data = data[(data["age"] > 30)]
        elif field_name == 'age' and field_value == "< 20":
            result_data = data[(data["age"] < 20)]
        else:
            #  tìm kiếm các giá trị trong DataFrame df mà không phân biệt chữ hoa và chữ thường (case-insensitive) trong cột field_name so với giá trị field_value
            result_data = df[df[field_name].astype(str).str.lower() == field_value.lower()] # Tìm kiếm không phân biệt chữ hoa, thường
        if result_data.empty:
            messagebox.showerror("Error", f"Không tìm thấy dữ liệu với {field_name} = '{field_value}'")
        # Hiển thị dữ liệu mới
        for _, row in result_data.iterrows(): # Duyệt qua từng dòng dữ liệu
            self.tree.insert("", tk.END, values=list(row)) # thêm dòng dữ liệu vào treeview 

    def show_top_total(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="TOP SINH VIÊN CÓ TỔNG ĐIỂM CAO NHẤT", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)
        buttons = [
            ("Top sinh viên có tổng điểm đáng giá cao nhất", self.top_rating),
            ("Top sinh viên có tổng điểm các môn cao nhất", self.top_grade),
            ("Top sinh viên có tổng điểm đánh giá và môn học cao nhất", self.top_grade_rating)
        ]
        for text, command in buttons:
            tk.Button(self.content_frame, text=text, cursor="hand2", command=command).pack(padx=5, pady=15)

    def top_rating(self):
        self.show_top_students_by_column(['portfolio.rating', 'coverletter.rating', 'refletter.rating'], 'total_rating', "TOP 10 SINH VIÊN CÓ TỔNG ĐIỂM ĐÁNH GIÁ CAO NHẤT")

    def top_grade(self):
        self.show_top_students_by_column(['sciences.grade', 'math.grade', 'language.grade', 'english.grade'], 'total_grade', "TOP 10 SINH VIÊN CÓ TỔNG ĐIỂM MÔN HỌC CAO NHẤT")

    def top_grade_rating(self):
        self.show_top_students_by_column(['sciences.grade', 'math.grade', 'language.grade', 'english.grade', 'portfolio.rating', 'coverletter.rating', 'refletter.rating'], 'total_grade_rating', "TOP 10 SINH VIÊN CÓ TỔNG ĐIỂM CAO NHẤT")

    def show_top_students_by_column(self, columns, new_column, title):
        self.clear_content_frame()
        df = pd.read_csv("data/data_clean.csv")
        if df.empty:
            messagebox.showerror("Lỗi", "Không có dữ liệu để hiển thị.")
            return
        df[new_column] = df[columns].sum(axis=1)
        top_students = show_top_students(df, new_column)
        self.create_treeview(self.content_frame, top_students, title)

    def show_top_students(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="TOP SINH VIÊN ĐIỂM CAO", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)
        buttons = [
            ("Top 10 sinh viên điểm toán cao nhất", self.top_10_math),
            ("Top 10 sinh viên điểm khoa học cao nhất", self.top_10_science),
            ("Top 10 sinh viên điểm tiếng anh cao nhất", self.top_10_english),
            ("Top 10 sinh viên điểm ngôn ngữ cao nhất", self.top_10_language),
            ("Top 10 sinh viên điểm đánh giá hồ sơ cao nhất", self.top_10_portfolio),
            ("Top 10 sinh viên điểm đánh giá thư xin việc cao nhất", self.top_10_coverletter),
            ("Top 10 sinh viên điểm đánh giá thư giới thiệu cao nhất", self.top_10_refletter)
        ]
        for text, command in buttons:
            tk.Button(self.content_frame, text=text, cursor="hand2", command=command).pack(padx=5, pady=15)

    def top_10_math(self):
        self.show_top_students_by_column(['math.grade'], 'math.grade', "TOP 10 SINH VIÊN ĐIỂM CAO MÔN TOÁN")

    def top_10_science(self):
        self.show_top_students_by_column(['sciences.grade'], 'sciences.grade', "TOP 10 SINH VIÊN ĐIỂM CAO MÔN KHOA HỌC")

    def top_10_english(self):
        self.show_top_students_by_column(['english.grade'], 'english.grade', "TOP 10 SINH VIÊN ĐIỂM CAO MÔN ANH")

    def top_10_language(self):
        self.show_top_students_by_column(['language.grade'], 'language.grade', "TOP 10 SINH VIÊN ĐIỂM CAO MÔN NGÔN NGỮ")

    def top_10_portfolio(self):
        self.show_top_students_by_column(['portfolio.rating'], 'portfolio.rating', "TOP 10 SINH VIÊN CÓ ĐIỂM CAO ĐÁNH GIÁ HỒ SƠ CÁ NHÂN")

    def top_10_coverletter(self):
        self.show_top_students_by_column(['coverletter.rating'], 'coverletter.rating', "TOP 10 SINH VIÊN CÓ ĐIỂM CAO ĐÁNH GIÁ  THƯ XIN VIỆC")

    def top_10_refletter(self):
        self.show_top_students_by_column(['refletter.rating'], 'refletter.rating', "TOP 10 SINH VIÊN CÓ ĐIỂM CAO ĐÁNH GIÁ THƯ GIỚI THIỆU")

    def sort_stu(self):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="SẮP XẾP SINH VIÊN", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)
        buttons = [
            ("Sắp xếp theo Tuổi", self.sort_by_age),
            ("Sắp xếp theo GPA", self.sort_by_avg)
        ]
        for text, command in buttons:
            tk.Button(self.content_frame, text=text, cursor="hand2", command=command).pack(padx=5, pady=30)

    def sort_by_age(self):
        self.sort_and_display("data/sorted_by_age.csv", "DANH SÁCH SINH VIÊN SẮP XẾP THEO TUỔI", sort_increase_age)

    def sort_by_avg(self):
        self.sort_and_display("data/sorted_by_gpa.csv", "DANH SÁCH SINH VIÊN SẮP XẾP THEO GPA", sort_desc_gpa)

    def sort_and_display(self, file_path, title, sort_function):
        self.clear_content_frame()
        sort_function()
        self.read(file_path, title)

    def exit_program(self):
        self.root.destroy()
        subprocess.run(["python", "gui/home_page.py"])

def main():
    root = Tk()
    app = Student(root)
    root.mainloop()

if __name__ == "__main__":
    main()

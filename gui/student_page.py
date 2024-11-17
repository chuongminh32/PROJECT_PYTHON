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
from modules.student_function import sort_increase_point, sort_increase_age
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
        self.create_menu_button(M_Frame, "Top sinh viên", self.show_top_students, 150)
        self.create_menu_button(M_Frame, "Sắp xếp", self.sort_stu, 220)
        self.create_menu_button(M_Frame, "Đọc data", self.read, 290)
        self.create_menu_button(M_Frame, "Quay về", self.exit_program, 360)

    def create_content_frame(self):
        """Tạo vùng hiển thị nội dung."""
        self.content_frame = Frame(self.root, bg="lightgrey")
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

    def read(self, file_path="data/data_clean.csv", title = "DANH SÁCH SINH VIÊN"):
        """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra bảng trong cửa sổ hiện tại."""
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        try:
            data = pd.read_csv(file_path)  # Đọc dữ liệu từ file CSV

            if data.empty:
                messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
                return

           # Thêm tiêu đề cho bảng dữ liệu và căn giữa
            title_label = tk.Label(self.content_frame, text=title, font=("Arial", 14, "bold"), bg="lightgrey")
            title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")  # Căn giữa tiêu đề

            if title == "DANH SÁCH SINH VIÊN SẮP XẾP THEO TUỔI" or title == "DANH SÁCH SINH VIÊN SẮP XẾP THEO ĐIỂM":
                # back btn 
                back_btn = tk.Button(self.content_frame, text="Quay lại", command=self.sort_stu)
                back_btn.place(x=10, y=10)

            # Tạo thanh cuộn dọc và ngang cho Treeview
            v_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical")
            h_scrollbar = ttk.Scrollbar(self.content_frame, orient="horizontal")

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
            tree.grid(row=1, column=0, sticky="nsew")
            v_scrollbar.grid(row=1, column=1, sticky="ns")
            h_scrollbar.grid(row=2, column=0, sticky="ew")

            # Kết nối thanh cuộn với Treeview
            v_scrollbar.config(command=tree.yview)  # Cuộn dọc
            h_scrollbar.config(command=tree.xview)  # Cuộn ngang

            # Thiết lập tỷ lệ mở rộng cho Treeview
            self.content_frame.grid_rowconfigure(0, weight=0)  # Dòng tiêu đề không thay đổi
            self.content_frame.grid_rowconfigure(1, weight=1)  # Dòng cho Treeview mở rộng
            self.content_frame.grid_columnconfigure(0, weight=1)  # Cột Treeview mở rộng
            self.content_frame.grid_columnconfigure(1, weight=0)  # Cột thanh cuộn dọc cố định
            self.content_frame.grid_columnconfigure(2, weight=0)  # Cột thanh cuộn ngang cố định

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
            self.content_frame, text="Nhập tên trường cần lọc:") # Label
        field_name_label.pack(padx=5, pady=5) # Hiển thị label

        self.field_name_entry = tk.Entry(self.content_frame, width=30) # Entry
        self.field_name_entry.pack(padx=5, pady=5)  # Hiển thị entry

        field_value_label = tk.Label(
            self.content_frame, text="Nhập giá trị cần tìm:")
        field_value_label.pack(padx=5, pady=5)

        self.field_value_entry = tk.Entry(self.content_frame, width=30)
        self.field_value_entry.pack(padx=5, pady=5)

        # Hàm tìm kiếm dữ liệu dựa trên trường và giá trị nhập vào
        def search_by_field():
            # Trường cần lọc (ví dụ: 'nationality')
            field_name = self.field_name_entry.get()
            field_value = self.field_value_entry.get()  # Giá trị lọc (ví dụ: 'vietnam')

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


    #  top stu point and rating
    def stu_find(self):
        self.clear_content_frame()
        df = pd.read_csv("data/data_clean.csv")

        tk.Label(self.content_frame, text="TOP STUDENT TOTAL SCORE AND RATING", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)

        top_stu_math = tk.Button(
            self.content_frame, text="Top sinh viên có tổng điểm đáng giá cao nhất", command=self.top_rating)
        top_stu_math.pack(padx=5, pady=15)

        top_stu_sci = tk.Button(
            self.content_frame, text="Top sinh viên có tổng điểm các môn cao nhất", command=self.top_grade)
        top_stu_sci.pack(padx=5, pady=15)

        top_stu_eng = tk.Button(
            self.content_frame, text="Top sinh viên có tổng điểm đánh giá và môn học cao nhất", command=self.top_grade_rating)
        top_stu_eng.pack(padx=5, pady=15)
    def top_rating(self):
        self.clear_content_frame()
        df = pd.read_csv("data/data_clean.csv")
        if df.empty:
            messagebox.showerror("Lỗi", "Không có dữ liệu để hiển thị.")
            return
        df['total_rating'] = df[[ 'portfolio.rating', 'coverletter.rating', 'refletter.rating']].sum(axis=1)
        top_total_rating_students = df.nlargest(10, 'total_rating')
        self.create_treeview(self.content_frame, top_total_rating_students, "TOP 10 STUDENTS - TOTAL RATING")

    def top_grade(self):
        self.clear_content_frame()
        df = pd.read_csv("data/data_clean.csv")
        if df.empty:
            messagebox.showerror("Lỗi", "Không có dữ liệu để hiển thị.")
            return
        df['total_grade'] = df[[ 'sciences.grade', 'math.grade', 'language.grade','english.grade']].sum(axis=1)
        top_total_grade_students = df.nlargest(10, 'total_grade')
        self.create_treeview(self.content_frame, top_total_grade_students, "TOP 10 STUDENTS - TOTAL GRADE")
    
    def top_grade_rating(self):
        self.clear_content_frame()
        df = pd.read_csv("data/data_clean.csv")
        if df.empty:
            messagebox.showerror("Lỗi", "Không có dữ liệu để hiển thị.")
            return
        df['total_grade_rating'] = df[[ 'sciences.grade', 'math.grade', 'language.grade','english.grade','portfolio.rating', 'coverletter.rating', 'refletter.rating']].sum(axis=1)
        top_total_grade_students = df.nlargest(10, 'total_grade_rating')
        self.create_treeview(self.content_frame, top_total_grade_students, "TOP 10 STUDENTS - TOTAL POINT AND RATING")
    

    # top 10 sinh viên có điểm cao nhất
    def show_top_students(self):
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        tk.Label(self.content_frame, text="TOP STUDENT BEST SCORE", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)
        
        top_stu_math = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm toán cao nhất", command=self.top_10_math)
        top_stu_math.pack(padx=5, pady=15)

        top_stu_sci = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm khoa học cao nhất", command=self.top_10_science)
        top_stu_sci.pack(padx=5, pady=15)

        top_stu_eng = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm tiếng anh cao nhất", command=self.top_10_english)
        top_stu_eng.pack(padx=5, pady=15)

        top_stu_eng = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm ngôn ngữ cao nhất", command=self.top_10_language)
        top_stu_eng.pack(padx=5, pady=15)

        top_stu_eng = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm đánh giá hồ sơ cao nhất", command=self.top_10_portfolio)
        top_stu_eng.pack(padx=5, pady=15)
        
        top_stu_eng = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm đánh giá thư xin việc cao nhất", command=self.top_10_coverletter)
        top_stu_eng.pack(padx=5, pady=15)

        top_stu_eng = tk.Button(
            self.content_frame, text="Top 10 sinh viên điểm đánh giá thư giới thiệu cao nhất", command=self.top_10_refletter)
        top_stu_eng.pack(padx=5, pady=15)
    
    def create_treeview(self, parent_frame, dataframe, title):
        """
        Hàm tạo bảng Treeview để hiển thị dữ liệu.
        :param parent_frame: Frame chứa Treeview.
        :param dataframe: DataFrame dữ liệu để hiển thị.
        :param title: Tiêu đề cho bảng.
        """
        # Xóa nội dung cũ của frame
        for widget in parent_frame.winfo_children():
            widget.destroy()

        # Thêm tiêu đề
        title_label = tk.Label(parent_frame, text=title, font=("Arial", 17, "bold"), bg="lightgrey")
        title_label.pack(padx=5, pady=5)

        if title == "TOP 10 STUDENTS - TOTAL POINT AND RATING" or title == "TOP 10 STUDENTS - TOTAL GRADE" or title == "TOP 10 STUDENTS - TOTAL RATING":
            # back btn 
            back_btn = tk.Button(self.content_frame, text="Quay lại", command=self.stu_find)
            back_btn.place(x=10, y=10)
        else:
            # back btn 
            back_btn = tk.Button(self.content_frame, text="Quay lại", command=self.show_top_students)
            back_btn.place(x=10, y=10)

        # Tạo Treeview
        columns = list(dataframe.columns)  # Lấy tên cột từ DataFrame
        tree = ttk.Treeview(parent_frame, columns=columns, show="headings", height=10)

        # Đặt tiêu đề và cấu hình cột
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")

        # Thêm dữ liệu vào Treeview
        for index, row in dataframe.iterrows():
            tree.insert("", "end", values=list(row))

        # Tạo thanh cuộn cho Treeview
        v_scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        h_scrollbar = tk.Scrollbar(parent_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Đặt Treeview và thanh cuộn vào Frame
        tree.pack(padx=10, pady=10, fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")

    def top_10_math(self):
        """Hiển thị bảng top 10 sinh viên có điểm toán cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu
        if df.empty:
            messagebox.showerror("Lỗi", "Không có dữ liệu để hiển thị.")
            return


        # Kiểm tra cột 'math.grade' có tồn tại không
        if 'math.grade' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm Toán trong dữ liệu.")
            return

        # Lấy top 10 sinh viên có điểm toán cao nhất
        top_math_students = df.nlargest(10, 'math.grade')
        # Gọi hàm tạo Treeview để hiển thị bảng
        self.create_treeview(self.content_frame, top_math_students, "TOP 10 STUDENTS - MATH GRADE")

    def top_10_science(self):
        """Hiển thị bảng top 10 sinh viên có điểm khoa học cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu

        if 'sciences.grade' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm Khoa học trong dữ liệu.")
            return

        top_science_students = df.nlargest(10, 'sciences.grade')
        self.create_treeview(self.content_frame, top_science_students, "TOP 10 STUDENTS - SCIENCE GRADE")

    def top_10_english(self):
        """Hiển thị bảng top 10 sinh viên có điểm ngoại ngữ cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu

        if 'english.grade' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm Ngoại ngữ trong dữ liệu.")
            return

        top_english_students = df.nlargest(10, 'english.grade')

         # Gọi hàm tạo Treeview để hiển thị bảng
        self.create_treeview(self.content_frame, top_english_students, "TOP 10 STUDENTS - ENGLISH GRADE")
    
    def top_10_language(self):
        """Hiển thị bảng top 10 sinh viên có điểm ngôn ngữ cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu

        # Kiểm tra cột 'math.grade' có tồn tại không
        if 'english.grade' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm Ngôn ngữ trong dữ liệu.")
            return

        top_student_language = df.nlargest(10, 'language.grade')

         # Gọi hàm tạo Treeview để hiển thị bảng
        self.create_treeview(self.content_frame, top_student_language, "TOP 10 STUDENTS - LANGUAGE GRADE")
    
    def top_10_portfolio(self):
        """Hiển thị bảng top 10 sinh viên có điểm đánh giá hồ sơ cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu

        if 'portfolio.rating' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm Ngoại ngữ trong dữ liệu.")
            return

        top_portfolio_students = df.nlargest(10, 'portfolio.rating')

        self.create_treeview(self.content_frame, top_portfolio_students, "TOP 10 STUDENTS - PORTFOLIO RATING")
    
    def top_10_coverletter(self):
        """Hiển thị bảng top 10 sinh viên có điểm đánh giá thư xin việc cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu

        if 'coverletter.rating' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm thư xin việc trong dữ liệu.")
            return

        top_coverletter_students = df.nlargest(10, 'coverletter.rating')

         # Gọi hàm tạo Treeview để hiển thị bảng
        self.create_treeview(self.content_frame, top_coverletter_students, "TOP 10 STUDENTS - COVERLETTER RATING")
    
    def top_10_refletter(self):
        """Hiển thị bảng top 10 sinh viên có điểm  cao nhất."""
        self.clear_content_frame()  # Xóa nội dung cũ
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu

        if 'refletter.rating' not in df.columns:
            messagebox.showerror("Lỗi", "Không tìm thấy cột điểm thư giới thiệu trong dữ liệu.")
            return

        top_refletter_students = df.nlargest(10, 'refletter.rating')

        self.create_treeview(self.content_frame, top_refletter_students, "TOP 10 STUDENTS - REFLETTER RATING")
    


    # sort student age, point 
    def sort_stu(self):
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        tk.Label(self.content_frame, text="SẮP XẾP SINH VIÊN", font=("Arial", 17, "bold"), bg="lightgrey").pack(pady=10)
        # Nút sắp xếp theo tuổi
        sort_age_button = tk.Button(
            self.content_frame, text="Sắp xếp theo Tuổi", command=self.sort_by_age)
        sort_age_button.pack(padx=5, pady=30)

        # Nút sắp xếp theo điểm trung bình
        sort_avg_button = tk.Button(
            self.content_frame, text="Sắp xếp theo Điểm Trung Bình", command=self.sort_by_avg)
        sort_avg_button.pack(padx=5, pady=10)

    def sort_by_age(self):
        """Hàm cho chức năng Sắp xếp - Sắp xếp sinh viên theo tuổi tăng dần."""
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung
        result = sort_increase_age()
        self.read("data/sorted_by_age.csv","DANH SÁCH SINH VIÊN SẮP XẾP THEO TUỔI")

    def sort_by_avg(self):
        """Hàm cho chức năng Sắp xếp - Sắp xếp sinh viên theo điểm trung bình tăng dần."""
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung
        result = sort_increase_point()
        self.read("data/sorted_by_point.csv","DANH SÁCH SINH VIÊN SẮP XẾP THEO ĐIỂM")


    # exit 
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

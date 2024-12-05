import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sys
import pandas as pd
import subprocess

# Thêm đường dẫn của thư mục cha vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_cleaning import handle_missing_value, remove_duplicates, correct_formatting, save_to_cleaned_data_file
from modules.data_crud import read_data, create_data, update_data, delete_data

"""Mô tả:
    Đây là một trang quản lý sinh viên được xây dựng bằng thư viện Tkinter trong Python.
    Trang quản lý này cho phép người dùng thực hiện các chức năng như đọc, thêm, cập nhật, xóa và làm sạch dữ liệu sinh viên từ file CSV.
Thư viện sử dụng:
    - tkinter: Thư viện GUI tiêu chuẩn của Python.
    - tkinter.messagebox: Thư viện con của tkinter để hiển thị các hộp thoại thông báo.
    - tkinter.ttk: Thư viện con của tkinter để tạo các widget nâng cao.
    - subprocess: Thư viện để chạy các tiến trình con.
    - os: Thư viện cung cấp nhiều chức năng liên quan đến hệ điều hành.
    - pandas: Thư viện để xử lý và phân tích dữ liệu.
    - PIL (Pillow): Thư viện xử lý hình ảnh.
Lớp:
    - StudentManagementApp: Lớp đại diện cho trang quản lý sinh viên.
Phương thức của lớp StudentManagementApp:
    - __init__(self, root): Khởi tạo đối tượng StudentManagementApp.
    - setup_window(self): Thiết lập cửa sổ chính của ứng dụng.
    - create_logo(self): Thêm logo cho trang quản lý.
    - create_menu(self): Tạo menu chức năng cho trang quản lý.
    - create_content_frame(self): Tạo khung nội dung để hiển thị dữ liệu và các form nhập liệu.
    - create_menu_button(self, parent, text, command, y_position): Tạo các nút trong menu.
    - clear_content_frame(self): Xóa nội dung trong khung nội dung.
    - read(self, file_path="data/data_clean.csv", title="DANH SÁCH SINH VIÊN"): Đọc và hiển thị dữ liệu sinh viên từ file CSV.
    - display_data_table(self, data, title): Hiển thị dữ liệu trong DataFrame dưới dạng bảng.
    - create(self): Tạo form nhập liệu để thêm sinh viên mới.
    - create_form(self, fields, title): Tạo form nhập liệu cho các chức năng thêm, cập nhật và xóa sinh viên.
    - create_sample_button(self, entries, fields): Tạo nút thêm dữ liệu mẫu vào form nhập liệu.
    - fill_sample_data(self, entries, fields): Điền dữ liệu mẫu vào các ô nhập liệu.
    - create_confirm_button(self, entries, fields, confirm_command, title): Tạo nút xác nhận cho các chức năng thêm, cập nhật và xóa sinh viên.
    - confirm_create(self, entries, fields): Xác nhận và thêm dữ liệu sinh viên mới vào file CSV.
    - update(self): Tạo form nhập liệu để cập nhật thông tin sinh viên.
    - create_search_button(self, entries, fields, search_command): Tạo nút tìm kiếm sinh viên theo ID.
    - search_student_for_update(self, entries, fields): Tìm kiếm và hiển thị thông tin sinh viên cần cập nhật.
    - confirm_update(self, entries, fields): Xác nhận và cập nhật thông tin sinh viên trong file CSV.
    - delete(self): Tạo form nhập liệu để xóa sinh viên.
    - search_student_for_delete(self, entries, fields): Tìm kiếm và hiển thị thông tin sinh viên cần xóa.
    - confirm_delete(self, entries, fields): Xác nhận và xóa sinh viên khỏi file CSV.
    - cleaning(self): Làm sạch dữ liệu sinh viên trong file CSV.
    - exit_program(self): Thoát khỏi ứng dụng và quay lại trang chính.
Hàm:
    - main(): Hàm chính để khởi chạy ứng dụng."""


class StudentManagementApp():
    def __init__(self, root):
        self.root = root  # root: Cửa sổ chính của ứng dụng
        self.setup_window()  # Thiết lập cửa sổ chính
        self.create_logo()  # Thêm logo cho trang quản lý
        self.create_menu()  # Tạo menu chức năng cho trang quản lý
        # Tạo khung nội dung để hiển thị dữ liệu và các form nhập liệu
        self.create_content_frame()
        root.resizable(False, False)

        self.current_page = 1
        self.rows_per_page = 15  # Hiển thị 15 dòng mỗi trang

    def setup_window(self):
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")

    def create_logo(self):
        logo_path = os.path.join("images", "logo_fit.png")
        logo_image = Image.open(logo_path).resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo_image)
        Label(self.root, text="Quản lí", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)
        menu_items = [("Đọc", self.read), ("Thêm", self.create), ("Sửa", self.update),
                      ("Xóa", self.delete), ("Làm sạch", self.cleaning), ("Quay lại", self.exit_program)]
        for i, (text, command) in enumerate(menu_items):  # Tạo các nút trong menu
            self.create_menu_button(M_Frame, text, command, i * 75)

    def create_content_frame(self):
        self.content_frame = Frame(self.root, bg="lightgrey")
        self.content_frame.place(x=200, y=80, width=800, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        button = Button(parent, text=text, border=0, bg="#242533", fg="white",
                        cursor="hand2", font=("Arial", 12, "bold"), command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def read(self, file_path="data/data_clean.csv", title="DANH SÁCH SINH VIÊN"):
        self.clear_content_frame()
        try:
            # data là DataFrame chứa dữ liệu sinh viên
            data = read_data(file_path)
            if data.empty:
                messagebox.showinfo(
                    "Thông báo", "Không có dữ liệu để hiển thị.")
                return
            self.display_data_table(data, title)
        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def display_data_table(self, data, title):
        """
        Hiển thị dữ liệu trong DataFrame dưới dạng bảng với phân trang và thanh cuộn ngang.
        """
        self.data = data  # Lưu dữ liệu vào thuộc tính để quản lý
        self.total_pages = (len(data) + self.rows_per_page - 1) // self.rows_per_page  # Tính tổng số trang

        # Tiêu đề bảng
        title_label = tk.Label(self.content_frame, text=title, font=("Arial", 17, "bold"), bg="lightgrey")
        title_label.pack(padx=5, pady=5)

        # Treeview
        columns = list(data.columns)  # Lấy tên các cột
        self.tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=self.rows_per_page)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        # Thanh cuộn dọc
        y_scroll = ttk.Scrollbar(self.content_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=y_scroll.set)
        y_scroll.pack(side="right", fill="y")

        # Thanh cuộn ngang
        x_scroll = ttk.Scrollbar(self.content_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=x_scroll.set)
        x_scroll.pack(side="bottom", fill="x")

        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Khung điều hướng
        nav_frame = tk.Frame(self.content_frame)
        nav_frame.pack(pady=10)

        self.prev_button = ttk.Button(nav_frame, text="Previous", command=self.prev_page)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.page_label = tk.Label(nav_frame, text=f"Page {self.current_page}/{self.total_pages}")
        self.page_label.grid(row=0, column=1, padx=5)

        self.next_button = ttk.Button(nav_frame, text="Next", command=self.next_page)
        self.next_button.grid(row=0, column=2, padx=5)

        # Hiển thị dữ liệu trang đầu tiên
        self.display_page()


    def display_page(self):
        """Hiển thị dữ liệu cho trang hiện tại."""
        start_idx = (self.current_page - 1) * self.rows_per_page
        end_idx = start_idx + self.rows_per_page
        current_data = self.data.iloc[start_idx:end_idx]  # Lấy dữ liệu của trang hiện tại

        # Xóa dữ liệu cũ trong Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Thêm dữ liệu mới vào Treeview
        for _, row in current_data.iterrows():
            self.tree.insert("", tk.END, values=list(row))

        # Cập nhật nhãn trang
        self.page_label.config(text=f"Page {self.current_page}/{self.total_pages}")

    def next_page(self):
        """Chuyển đến trang tiếp theo."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.display_page()

    def prev_page(self):
        """Quay lại trang trước."""
        if self.current_page > 1:
            self.current_page -= 1
            self.display_page()

    # Create
    def create(self):
        self.clear_content_frame()
        # fields: List chứa các trường thông tin sinh viên, mỗi phần tử là một tuple (tên trường, placeholder)
        fields = [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ("Nationality", "e.g., United States of America"),
                  ("City", "e.g., Oakland"), ("Latitude (vĩ dộ)",
                                              "e.g., 37.8"), ("Longitude (kinh độ)", "e.g., -122.27"),
                  ("Gender", "e.g., M/F"), ("Ethnic Group", "e.g., NA"), ("Age",
                                                                          "e.g., 22"), ("English Grade", "e.g., 3.5"),
                  ("Math Grade", "e.g., 3.7"), ("Sciences Grade",
                                                "e.g., 3.2"), ("Language Grade", "e.g., 5"),
                  ("Portfolio Rating", "e.g., 4"), ("Cover Letter Rating", "e.g., 5"), ("Reference Letter Rating", "e.g., 4")]
        fields_ui = [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ("Nationality", "e.g., United States of America"),
                     ("City", "e.g., Oakland"), ("Latitude (vĩ dộ)",
                                                 "e.g., 37.8"), ("Longitude (kinh độ)", "e.g., -122.27"),
                     ("Gender", "e.g., M/F"), ("Ethnic Group", "e.g., NA"), ("Age",
                                                                             "e.g., 22"), ("English Grade", "e.g., 3.5"),
                     ("Math Grade", "e.g., 3.7"), ("Sciences Grade",
                                                   "e.g., 3.2"), ("Language Grade", "e.g., 5"),
                     ("Portfolio Rating", "e.g., 4"), ("Cover Letter Rating", "e.g., 5"), ("Reference Letter Rating", "e.g., 4")]
        entries = self.create_form(
            fields, "THÊM SINH VIÊN")  # Tạo form nhập liệu
        self.create_sample_button(entries, fields)  # Tạo nút thêm dữ liệu mẫu
        # Tạo nút xác nhận THÊM SINH VIÊN
        self.create_confirm_button(
            entries, fields, fields_ui, self.confirm_create, "Tạo")

    # fields: List chứa các trường thông tin sinh viên , Ex: [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ...]
    # entries: Dictionary chứa các entry widget, Ex: {"ID": Entry, "Name": Entry, ...}
    def create_form(self, fields, title):
        """ 
        Tạo form nhập liệu để THÊM SINH VIÊN.
        :param fields: Danh sách các trường thông tin sinh viên.
        :param title: Tiêu đề của form.
        * logic: đặt 8 dòng (1 -> 8), bỏ qua dòng đầu (tiêu đề), 4 col (col 0 , 2 : label, 1, 2: entry) 
        -> lấy phần dư chỉ số x 2 -> vị trí label, x2 + 1 -> vị trí entry (ô nhập liệu)
        """
        entries = {}  # Dictionary chứa các entry widget
        title_label = Label(self.content_frame, text=title,
                            font=("Arial", 14, "bold"), bg="lightgrey")
        title_label.pack(pady=10)
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)
        # enumerate(fields): Trả về một đối tượng liệt kê, mỗi phần tử của đối tượng liệt kê là một bộ gồm chỉ số và
        #  giá trị của phần tử tương ứng trong iterable.
        for i, (label_text, placeholder) in enumerate(fields):  # Tạo các label và entry widget
            col = i % 2  # Tính toán cột
            # Tính toán vị trí hàng và cột, +1 để bỏ qua hàng đầu tiên
            row = (i // 2) + 1

            # Tạo label cho mỗi trường, col*2 -> bỏ qua col entry widget
            Label(field_frame, text=label_text, font=("Arial", 11)).grid(
                row=row, column=col*2, padx=15, pady=5, sticky="w")
            # Stringvar là 1 lớp trong thư viện tkinter để quản lí chuỗi, giúp lấy giá trị từ entry widget
            # Tạo biến var để lưu giá trị nhập vào
            var = StringVar(value=placeholder)
            entry = Entry(field_frame, textvariable=var, fg="grey",
                          font=("Arial", 11))  # Tạo ô nhập liệu
            # Đặt ô nhập liệu vào frame, col*2 + 1 -> kề label(ví dụ label col 0 -> entry col 1)
            entry.grid(row=row, column=col * 2 + 1,
                       padx=15, pady=5, ipadx=7, ipady=5)

            # chỉ cho nhập id đồi với các form chỉnh sửa và xóa
            if title == "CẬP NHẬT SINH VIÊN" or title == "XÓA SINH VIÊN":
                # Nếu là trường 'id', để người dùng nhập bình thường; ngược lại thì vô hiệu hóa
                if label_text != "ID":
                    # Vô hiệu hóa các trường không phải 'id'
                    entry.config(state="disabled")

            # Xử lý sự kiện để làm placeholder
            """ entry.bind("<FocusIn>", ...): Liên kết sự kiện FocusIn với Entry widget.
            lambda e, var=var, placeholder=placeholder: ...: Định nghĩa một hàm lambda để xử lý sự kiện. e là đối tượng sự kiện, var và placeholder là các biến được truyền vào hàm lambda.
            var.set("") if var.get() == placeholder else None: Nếu giá trị hiện tại của var bằng placeholder, thì đặt giá trị của var thành chuỗi rỗng. Nếu không, không làm gì cả.
            Mục đích của đoạn mã này là xóa giá trị mặc định (placeholder) trong Entry widget khi người dùng nhấp vào nó, để họ có thể nhập giá trị mới."""
            entry.bind("<FocusIn>", lambda e, var=var, placeholder=placeholder: var.set(
                "") if var.get() == placeholder else None)
            entry.bind("<FocusOut>", lambda e, var=var, placeholder=placeholder: var.set(
                placeholder) if var.get() == "" else None)

            # Thêm placeholder vào entry widget, lấy placeholder trong fields truyền cho var -> liên kết với entry widget
            # Thêm entry widget vào dictionary entries
            entries[label_text] = entry

        # Tạo nút clear -> refresh lại form
        if title == "THÊM SINH VIÊN":
            Button(self.content_frame, text="Clear", width=15, height=2, cursor="hand2",
                   command=self.create).pack(side=LEFT, padx=0, pady=10, expand=True)
        elif title == "CẬP NHẬT SINH VIÊN":
            Button(self.content_frame, text="Clear", width=15, height=2, cursor="hand2",
                   command=self.update).pack(side=LEFT, padx=0, pady=10, expand=True)
        elif title == "XÓA SINH VIÊN":
            Button(self.content_frame, text="Clear", width=15, height=2, cursor="hand2",
                   command=self.delete).pack(side=LEFT, padx=0, pady=10, expand=True)

        return entries  # Trả về dictionary chứa các entry widget
    # Sử dụng lambda khi bạn cần một hàm ngắn gọn cho các tác vụ đơn giản hoặc khi bạn muốn tránh phải định nghĩa một hàm riêng biệt cho một hành động tạm thời.

    def create_sample_button(self, entries, fields):
        sample_button = Button(self.content_frame, text="Thêm dữ liệu mẫu", width=15,
                               height=2, cursor="hand2", command=lambda: self.fill_sample_data(entries, fields))
        sample_button.pack(side=LEFT, padx=0, pady=10, expand=True)

    def fill_sample_data(self, entries, fields):
        """
        Điền dữ liệu mẫu vào các ô nhập liệu.
        :param entries: Dictionary chứa các entry widget.
        :param fields: Danh sách các trường thông tin sinh viên.
        """
        sample_data = {"ID": "9999", "Name": "Project Python", "Nationality": "Vietnam", "City": "Ho Chi Minh",
                       "Latitude (vĩ dộ)": "37.8", "Longitude (kinh độ)": "-122.27", "Gender": "F", "Ethnic Group": "NA",
                       "Age": "22", "English Grade": "4.0", "Math Grade": "3.9", "Sciences Grade": "3.8", "Language Grade": "5",
                       "Portfolio Rating": "4", "Cover Letter Rating": "5", "Reference Letter Rating": "4"}
        # entries: Dictionary chứa các entry widget (label + entry)
        for label_text, sample_value in sample_data.items():
            entries[label_text].delete(0, END)  # Xóa dữ liệu cũ trong entry
            # Điền dữ liệu mẫu vào entry
            entries[label_text].insert(0, sample_value)
            entries[label_text].config(fg="black")  # Đổi màu chữ

    def confirm_create(self, entries, fields, fields_ui):
        #  list comprehension
        # Lấy thông tin sinh viên từ các ô nhập liệu
        student_data = [entries[label_text].get() for label_text, _ in fields]
        for i, (field, placeholder) in enumerate(fields):  # Kiểm tra thông tin nhập vào
            df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file
            # Kiểm tra ID đã tồn tại chưa
            if student_data[0] in df['id'].astype(str).values:
                messagebox.showwarning(
                    "Cảnh báo", "ID đã tồn tại. Vui lòng nhập ID khác.")
                return
            if student_data[i] == placeholder or student_data[i] == "":
                messagebox.showwarning(
                    "Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
                return
        create_data(student_data, "data/data_clean.csv")
        messagebox.showinfo("Thành công", "Dữ liệu đã được thêm vào!")

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def create_confirm_button(self, entries, fields, fields_ui, confirm_command, title):
        confirm_button = Button(self.content_frame, text=title, width=15, height=2,
                                cursor="hand2", command=lambda: confirm_command(entries, fields, fields_ui))
        confirm_button.pack(side=LEFT, padx=0, pady=10, expand=True)

    def update(self):
        self.clear_content_frame()
        fields = [("id", "e.g., 0, 1, 2..."), ("name", "e.g., Kiana Lor"), ("nationality", "e.g., United States of America"),
                  ("city", "e.g., Oakland"), ("latitude", "e.g., 37.8"), ("longitude",
                                                                          "e.g., -122.27"), ("gender", "e.g., M/F"),
                  ("ethnic.group", "e.g., NA"), ("age", "e.g., 22"), ("english.grade",
                                                                      "e.g., 3.5"), ("math.grade", "e.g., 3.7"),
                  ("sciences.grade", "e.g., 3.2"), ("language.grade",
                                                    "e.g., 5"), ("portfolio.rating", "e.g., 4"),
                  ("coverletter.rating", "e.g., 5"), ("refletter.rating", "e.g., 4")]

        fields_ui = [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ("Nationality", "e.g., United States of America"),
                     ("City", "e.g., Oakland"), ("Latitude (vĩ dộ)",
                                                 "e.g., 37.8"), ("Longitude (kinh độ)", "e.g., -122.27"),
                     ("Gender", "e.g., M/F"), ("Ethnic Group", "e.g., NA"), ("Age",
                                                                             "e.g., 22"), ("English Grade", "e.g., 3.5"),
                     ("Math Grade", "e.g., 3.7"), ("Sciences Grade",
                                                   "e.g., 3.2"), ("Language Grade", "e.g., 5"),
                     ("Portfolio Rating", "e.g., 4"), ("Cover Letter Rating", "e.g., 5"), ("Reference Letter Rating", "e.g., 4")]

        entries = self.create_form(fields_ui, "CẬP NHẬT SINH VIÊN")
        self.create_search_button(
            entries, fields, fields_ui, self.search_student_for_update)
        self.create_confirm_button(
            entries, fields, fields_ui, self.confirm_update, "Cập nhật")

    def create_search_button(self, entries, fields, fields_ui, search_command):
        search_button = Button(self.content_frame, text="Tìm", width=15, height=2,
                               cursor="hand2", command=lambda: search_command(entries, fields, fields_ui))
        search_button.pack(side=LEFT, padx=0, pady=10, expand=True)

    def search_student_for_update(self, entries, fields, fields_ui):
        # bỏ di disable các trường
        for label_text, entry in entries.items():
            if label_text != "ID":
                entry.config(state="normal")

        # Lấy ID sinh viên
        student_id = entries["ID"].get()
        # df là DataFrame chứa dữ liệu sinh viên
        df = pd.read_csv("data/data_clean.csv")
        student_data = df[df['id'].astype(str) == student_id]  # Tìm sinh viên

        if student_data.empty:
            messagebox.showerror(
                "Error", f"Không tìm thấy sinh viên có ID: {student_id}")
            self.update()  # Hiển thị lại form xóa
            return False

        # Lấy thông tin sinh viên từ DataFrame dòng đầu tiên
        student_data = student_data.iloc[0]

        # chèn data tìm thấy vào entry widget
        # Điền thông tin sinh viên vào các ô nhập liệu
        for i, ((label_text, _), (label_text_ui, _)) in enumerate(zip(fields, fields_ui)):
            # Lấy entry widget cua field_ui de hien thi labeltext va du lieu
            entry = entries[label_text_ui]
            entry.delete(0, END)  # Xóa dữ liệu cũ
            # Điền dữ liệu sinh viên
            entry.insert(0, str(student_data[label_text]))
            # Đổi màu chữ và chỉ đọc
            entry.config(fg="black", font=("Arial", 11))
            # Đặt ô nhập liệu vào frame, entry -> col = 1 or 3, label = 0 or 2
            entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 +
                       1, padx=15, pady=5, ipadx=7, ipady=5)
        return True

    def confirm_update(self, entries, fields, fields_ui):
        student_id = str(entries["ID"].get())
        # Lấy thông tin sinh viên từ các ô nhập liệu: duyệt từng labeltext và placeholder trong fields, lấy giá trị từ entry widget tương ứng
        new_data = []
        for label_text, _ in fields_ui:
            value = entries[label_text].get()
            if label_text in ["ID", "Age", "Portfolio Rating", "Cover Letter Rating", "Reference Letter Rating"]:
                try:
                    value = int(value)  # Chuyển đổi về kiểu int
                except ValueError:
                    messagebox.showwarning("Cảnh báo", f"Trường '{
                                           label_text}' phải là số nguyên.")
                    return
            elif label_text in ["Latitude (vĩ dộ)", "Longitude (kinh độ)", "English Grade", "Math Grade", "Sciences Grade", "Language Grade"]:
                try:
                    value = float(value)
                except ValueError:
                    messagebox.showwarning("Cảnh báo", f"Trường '{
                                           label_text}' phải là số thực.")
                    return
            new_data.append(value)
        for i, (field, _) in enumerate(fields_ui):  # Kiểm tra thông tin nhập vào
            if new_data[i] == "":  # Nếu ô nhập liệu trống
                messagebox.showwarning(
                    "Cảnh báo", f"Hãy điền đầy đủ các trường '{field}'")
                return
        # Cập nhật thông tin sinh viên
        if update_data("data/data_clean.csv", student_id, new_data):
            messagebox.showinfo(
                "Thành công!", "Đã cập nhật thông tin sinh viên.")
        else:
            messagebox.showerror(
                "Cập nhật thất bại.", f"Không tìm thấy sinh viên với ID: {student_id}")

    # Delete
    def delete(self):
        self.clear_content_frame()
        fields = [("id", "e.g., 0, 1, 2..."), ("name", "e.g., Kiana Lor"), ("nationality", "e.g., United States of America"),
                  ("city", "e.g., Oakland"), ("latitude", "e.g., 37.8"), ("longitude",
                                                                          "e.g., -122.27"), ("gender", "e.g., M/F"),
                  ("ethnic.group", "e.g., NaN/Asia/.."), ("age",
                                                          "e.g., 22"), ("english.grade", "e.g., 3.5"), ("math.grade", "e.g., 3.7"),
                  ("sciences.grade", "e.g., 3.2"), ("language.grade",
                                                    "e.g., 5"), ("portfolio.rating", "e.g., 4"),
                  ("coverletter.rating", "e.g., 5"), ("refletter.rating", "e.g., 4")]

        fields_ui = [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ("Nationality", "e.g., United States of America"),
                     ("City", "e.g., Oakland"), ("Latitude (vĩ dộ)",
                                                 "e.g., 37.8"), ("Longitude (kinh độ)", "e.g., -122.27"),
                     ("Gender", "e.g., M/F"), ("Ethnic Group", "e.g., NA"), ("Age",
                                                                             "e.g., 22"), ("English Grade", "e.g., 3.5"),
                     ("Math Grade", "e.g., 3.7"), ("Sciences Grade",
                                                   "e.g., 3.2"), ("Language Grade", "e.g., 5"),
                     ("Portfolio Rating", "e.g., 4"), ("Cover Letter Rating", "e.g., 5"), ("Reference Letter Rating", "e.g., 4")]

        entries = self.create_form(fields_ui, "XÓA SINH VIÊN")
        self.create_search_button(
            entries, fields, fields_ui, self.search_student_for_delete)
        self.create_confirm_button(
            entries, fields, fields_ui, self.confirm_delete, "Xóa")

    def search_student_for_delete(self, entries, fields, fields_ui):
        # Kích hoạt tất cả các trường
        for label_text, entry in entries.items():
            if label_text != "ID":
                entry.config(state="normal")
        # Lấy ID sinh viên
        student_id = entries["ID"].get()
        df = pd.read_csv("data/data_clean.csv")
        student_data = df[df['id'].astype(str) == student_id]  # Tìm sinh viên
        if student_data.empty:  # Nếu không tìm thấy sinh viên
            messagebox.showerror(
                "Error", f"Không tìm thấy sinh viên có ID: {student_id}")
            self.delete()  # Hiển thị lại form xóa
            return False
        student_data = student_data.iloc[0]  # Lấy thông tin sinh viên
        for i, ((label_text, _), (label_text_ui, _)) in enumerate(zip(fields, fields_ui)):
            entry = entries[label_text_ui]  # Lấy entry widget
            entry.delete(0, END)  # Xóa dữ liệu cũ
            # Điền dữ liệu sinh viên
            entry.insert(0, str(student_data[label_text]))
            entry.config(fg="black", state="readonly", font=(
                "Arial", 11))  # Đổi màu chữ và chỉ đọc
            entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 + 1, padx=15,
                       pady=5, ipadx=7, ipady=5)  # Đặt ô nhập liệu vào frame
        return True

    def confirm_delete(self, entries, fields, fields_ui):
        student_id = entries["ID"].get()  # Lấy ID sinh viên
        if not student_id:
            messagebox.showwarning(
                "Cảnh báo", "Vui lòng nhập ID sinh viên cần xóa.")
            return

        # Xóa sinh viên
        file_path = "data/data_clean.csv"
        success = delete_data(file_path, student_id)

        if not success:
            messagebox.showerror(
                "Lỗi", f"Không tìm thấy sinh viên với ID: {student_id}.")
        else:
            messagebox.showinfo(
                "Thành công", f"Đã XÓA SINH VIÊN có ID {student_id}")

    # Cleaning
    def cleaning(self):
        self.clear_content_frame()
        file_path = "data/student-dataset.csv"
        data = pd.read_csv(file_path)
        data = handle_missing_value(data)  # Xử lý giá trị thiếu
        data = remove_duplicates(data)  # Xóa bản ghi trùng
        data = correct_formatting(data)  # Định dạng dữ liệu
        cleaned_file_path = "data/data_clean.csv"
        save_to_cleaned_data_file(cleaned_file_path, data)
        messagebox.showinfo("Thông báo", "Làm sạch thành công.")
        self.read()

    def exit_program(self):
        self.root.destroy()
        subprocess.run(["python", "gui/home_page.py"])


if __name__ == "__main__":
    root = Tk()  # Tạo cửa sổ chính
    app = StudentManagementApp(root)  # Tạo đối tượng ứng dụng
    root.mainloop()  # Chạy ứng dụng

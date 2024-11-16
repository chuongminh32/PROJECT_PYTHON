import os
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sys
import pandas as pd
import subprocess

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data, create_data, update_data, delete_data
from modules.data_cleaning import handle_missing_value, remove_duplicates, correct_formatting, save_to_cleaned_data_file
"""
Các thư viện được sử dụng:
- os: Thư viện cung cấp các hàm để tương tác với hệ điều hành.
- tkinter: Thư viện GUI tiêu chuẩn của Python.
    - *: Import tất cả các module con của tkinter.
    - messagebox: Module con của tkinter để hiển thị các hộp thoại thông báo.
    - ttk: Module con của tkinter cung cấp các widget nâng cao.
- PIL: Thư viện Python Imaging Library để xử lý hình ảnh.
    - Image: Module con của PIL để mở và xử lý hình ảnh.
    - ImageTk: Module con của PIL để sử dụng hình ảnh trong tkinter.
- sys: Thư viện cung cấp các hàm và biến để thao tác với trình thông dịch Python.
- pandas: Thư viện cung cấp các cấu trúc dữ liệu và công cụ phân tích dữ liệu.
- subprocess: Thư viện để chạy các tiến trình con và giao tiếp với chúng.
Các module tự định nghĩa:
- modules.data_crud: Module chứa các hàm để đọc, tạo, cập nhật và xóa dữ liệu.
    - read_data: Hàm để đọc dữ liệu từ file.
    - create_data: Hàm để tạo dữ liệu mới.
    - update_data: Hàm để cập nhật dữ liệu.
    - delete_data: Hàm để xóa dữ liệu.
- modules.data_cleaning: Module chứa các hàm để làm sạch dữ liệu.
    - handle_missing_value: Hàm để xử lý các giá trị thiếu.
    - remove_duplicates: Hàm để loại bỏ các bản ghi trùng lặp.
    - correct_formatting: Hàm để sửa định dạng dữ liệu.
    - save_to_cleaned_data_file: Hàm để lưu dữ liệu đã làm sạch vào file.
"""


class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()
        self.create_content_frame()
        root.resizable(False, False)

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

        Label(self.root, text="Quản lí", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        """Tạo menu cho ứng dụng."""
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)
        self.create_menu_button(M_Frame, "Đọc", self.read, 0)
        self.create_menu_button(M_Frame, "Thêm", self.create, 75)
        self.create_menu_button(M_Frame, "Sửa", self.update, 150)
        self.create_menu_button(M_Frame, "Xóa", self.delete, 220)
        self.create_menu_button(M_Frame, "Làm sạch", self.cleaning, 290)
        self.create_menu_button(M_Frame, "Back", self.exit_program, 360)

    def create_content_frame(self):
        """Tạo vùng hiển thị nội dung."""
        self.content_frame = Frame(self.root, bg="lightgrey")
        self.content_frame.place(x=200, y=80, width=800, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        """Tạo nút menu."""
        button = Button(parent, text=text, border=0, bg="#242533",
                        fg="white", font=("Arial", 12, "bold"), command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def clear_content_frame(self):
        """Xóa nội dung trong khung hiển thị nội dung."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def read(self):
        """Hiển thị dữ liệu trong file ra bảng."""
        self.clear_content_frame()  # Xóa nội dung cũ
        try:
            file_path = "data/data_clean.csv"
            data = read_data(file_path)
            if not data:
                messagebox.showinfo(
                    "Thông báo", "Không có dữ liệu để hiển thị.")
                return
            v_scrollbar = ttk.Scrollbar(
                self.content_frame, orient="vertical")  # Tạo thanh cuộn dọc
            h_scrollbar = ttk.Scrollbar(
                self.content_frame, orient="horizontal")  # Tạo thanh cuộn ngang
            columns = data[0]  # Lấy tên cột
            tree = ttk.Treeview(self.content_frame, columns=columns, show="headings",  # Tạo bảng hiển thị dữ liệu
                                yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
            for col in columns:  # Đặt tên cột
                tree.heading(col, text=col)
                # Đặt chiều rộng cột
                tree.column(col, anchor='center', width=150)
            for row in data[1:]:  # Thêm dữ liệu vào bảng
                tree.insert("", "end", values=row)
            tree.grid(row=0, column=0, sticky="nsew")  # Hiển thị bảng
            # Hiển thị thanh cuộn dọc
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            # Hiển thị thanh cuộn ngang
            h_scrollbar.grid(row=1, column=0, sticky="ew")
            # Kết nối thanh cuộn dọc với bảng
            v_scrollbar.config(command=tree.yview)
            # Kết nối thanh cuộn ngang với bảng
            h_scrollbar.config(command=tree.xview)
            self.content_frame.grid_rowconfigure(
                0, weight=1)  # Đặt trọng số cho hàng
            self.content_frame.grid_columnconfigure(
                0, weight=1)  # Đặt trọng số cho cột
        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def create(self):
        """Tạo bảng nhập dữ liệu sinh viên."""
        self.clear_content_frame()
        fields = [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ("Nationality", "e.g., United States of America"),
                  ("City", "e.g., Oakland"), ("Latitude (vĩ dộ)",
                                              "e.g., 37.8"), ("Longitude (kinh độ)", "e.g., -122.27"),
                  ("Gender", "e.g., M/F"), ("Ethnic Group", "e.g., NA"), ("Age",
                                                                          "e.g., 22"), ("English Grade", "e.g., 3.5"),
                  ("Math Grade", "e.g., 3.7"), ("Sciences Grade",
                                                "e.g., 3.2"), ("Language Grade", "e.g., 5"),
                  ("Portfolio Rating", "e.g., 4"), ("Cover Letter Rating", "e.g., 5"), ("Reference Letter Rating", "e.g., 4")]
        entries = {}
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)
        Label(field_frame, text="Thêm sinh viên", font=("Arial", 12, "bold")).grid(
            row=0, column=1, columnspan=2, pady=5)
        for i, (label_text, placeholder) in enumerate(fields):  # Tạo các trường nhập dữ liệu
            col = i % 2
            row = (i // 2) + 1
            Label(field_frame, text=label_text, font=("Arial", 11)).grid(
                row=row, column=col * 2, padx=15, pady=5, sticky="w")
            # Tạo biến lưu trữ dữ liệu nhập vào
            var = StringVar(value=placeholder)
            entry = Entry(field_frame, textvariable=var, fg="grey",
                          font=("Arial", 11))  # Tạo trường nhập dữ liệu
            entry.grid(row=row, column=col * 2 + 1, padx=15,
                       pady=5)  # Hiển thị trường nhập dữ liệu
            # Lưu trường nhập dữ liệu vào dictionary
            entries[label_text] = entry
            entry.bind("<FocusIn>", lambda e, var=var, placeholder=placeholder: var.set(
                # Xử lý khi focus vào trường nhập dữ liệu
                "") if var.get() == placeholder else None)
            entry.bind("<FocusOut>", lambda e, var=var, placeholder=placeholder: var.set(
                # Xử lý khi focus ra khỏi trường nhập dữ liệu
                placeholder) if var.get() == "" else None)
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)

        def fill_sample_data():
            sample_data = {"ID": "1", "Name": "Chuong", "Nationality": "Vietnam", "City": "Ho Chi Minh",
                           "Latitude (vĩ dộ)": "37.8", "Longitude (kinh độ)": "-122.27", "Gender": "F", "Ethnic Group": "NA",
                           "Age": "22", "English Grade": "4.0", "Math Grade": "3.9", "Sciences Grade": "3.8", "Language Grade": "5",
                           "Portfolio Rating": "4", "Cover Letter Rating": "5", "Reference Letter Rating": "4"}
            for label_text, sample_value in sample_data.items():
                entries[label_text].delete(0, END)  # Xóa dữ liệu cũ
                entries[label_text].insert(0, sample_value)  # Thêm dữ liệu mẫu
                # Đổi màu chữ thành màu đen
                entries[label_text].config(fg="black")
        sample_button = Button(
            button_frame, text="Thêm dữ liệu mẫu", command=fill_sample_data)
        sample_button.pack(side=LEFT, padx=20, pady=10)

        def confirm():
            student_data = [entries[label_text].get()
                            # Lấy dữ liệu nhập vào
                            for label_text, _ in fields]
            for i, (field, placeholder) in enumerate(fields):  # Kiểm tra dữ liệu nhập vào
                # Check if ID already exists
                df = pd.read_csv("data/data_clean.csv")
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

        confirm_button = Button(button_frame, text="Create", command=confirm)
        confirm_button.pack(side=RIGHT, padx=20, pady=10)

    def update(self):
        """Tìm kiếm và cập nhật thông tin sinh viên dựa trên ID."""
        self.clear_content_frame()
        fields = [("id", "e.g., 0, 1, 2..."), ("name", "e.g., Kiana Lor"), ("nationality", "e.g., United States of America"),
                  ("city", "e.g., Oakland"), ("latitude", "e.g., 37.8"), ("longitude",
                                                                          "e.g., -122.27"), ("gender", "e.g., M/F"),
                  ("ethnic.group", "e.g., NA"), ("age", "e.g., 22"), ("english.grade",
                                                                      "e.g., 3.5"), ("math.grade", "e.g., 3.7"),
                  ("sciences.grade", "e.g., 3.2"), ("language.grade",
                                                    "e.g., 5"), ("portfolio.rating", "e.g., 4"),
                  ("coverletter.rating", "e.g., 5"), ("refletter.rating", "e.g., 4")]
        entries = {}
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)
        inner_frame = Frame(field_frame)
        inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        Label(inner_frame, text="Nhập ID Sinh Viên:", font=(
            "Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
        student_id_entry = Entry(inner_frame, justify="center")
        student_id_entry.grid(row=0, column=2, columnspan=2, padx=10, pady=5)

        def search_student():
            student_id = student_id_entry.get()
            df = pd.read_csv("data/data_clean.csv")
            # Tìm sinh viên dựa trên ID
            student_data = df[df['id'].astype(str) == student_id]
            if student_data.empty:
                messagebox.showerror(
                    "Error", f"Không tìm thấy sinh viên có ID: {student_id}")
                for entry in entries.values():  # Xóa dữ liệu cũ
                    entry.grid_forget()
                return False  # Trả về False nếu không tìm thấy sinh viên
            # Lấy dữ liệu của sinh viên đầu tiên
            student_data = student_data.iloc[0]
            for i, (label_text, _) in enumerate(fields):  # Hiển thị dữ liệu của sinh viên
                # Lấy entry widget tương ứng với trường dữ liệu
                entry = entries[label_text]
                entry.delete(0, END)  # Xóa dữ liệu cũ
                # Hiển thị dữ liệu mới
                entry.insert(0, str(student_data[label_text]))
                entry.config(fg="black", font=("Arial", 11))
                entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 +
                           1, padx=15, pady=5, ipadx=7, ipady=5)
            return True
        for i, (label_text, placeholder) in enumerate(fields):  # Tạo các trường nhập dữ liệu
            col = i % 2
            row = (i // 2) + 1
            Label(inner_frame, text=label_text, font=10).grid(
                row=row, column=col * 2, padx=15, pady=5, sticky="w")
            entry = Entry(inner_frame, justify="center")
            entry.grid_forget()
            entries[label_text] = entry
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)
        search_button = Button(
            button_frame, text="Search", command=search_student)
        search_button.pack(side=LEFT, padx=20, pady=10)

        def confirm_update():
            student_id = str(student_id_entry.get())
            new_data = [entries[label_text].get() for label_text, _ in fields]
            for i, (field, placeholder) in enumerate(fields):
                if new_data[i] == "":
                    messagebox.showwarning(
                        "Cảnh báo", f"Hãy điền đầy đủ các trường '{field}'")
                    return
            if update_data(student_id, new_data):
                messagebox.showinfo(
                    "Thành công!", "Đã cập nhật thông tin sinh viên.")
                return
            else:
                messagebox.showerror(
                    "Cập nhật thất bại.", f"Không tìm thấy sinh viên với ID: {student_id}")
        confirm_button = Button(
            button_frame, text="Update", command=confirm_update)
        confirm_button.pack(side=RIGHT, padx=20, pady=10)

    def delete(self):
        """Xóa sinh viên."""
        self.clear_content_frame()
        fields = [("id", "e.g., 0, 1, 2..."), ("name", "e.g., Kiana Lor"), ("nationality", "e.g., United States of America"),
                  ("city", "e.g., Oakland"), ("latitude", "e.g., 37.8"), ("longitude",
                                                                          "e.g., -122.27"), ("gender", "e.g., M/F"),
                  ("ethnic.group", "e.g., NaN/Asia/.."), ("age", "e.g., 22"), ("english.grade",
                                                                      "e.g., 3.5"), ("math.grade", "e.g., 3.7"),
                  ("sciences.grade", "e.g., 3.2"), ("language.grade",
                                                    "e.g., 5"), ("portfolio.rating", "e.g., 4"),
                  ("coverletter.rating", "e.g., 5"), ("refletter.rating", "e.g., 4")]
        entries = {}
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)
        inner_frame = Frame(field_frame)
        inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        Label(inner_frame, text="Nhập ID Sinh Viên:", font=(
            "Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
        student_id_entry = Entry(inner_frame, justify="center")
        student_id_entry.grid(row=0, column=2, columnspan=2, padx=10, pady=5)

        def search_student():
            student_id = student_id_entry.get()
            df = pd.read_csv("data/data_clean.csv")
            student_data = df[df['id'].astype(str) == student_id]
            if student_data.empty:
                messagebox.showerror(
                    "Error", f"Không tìm thấy sinh viên có ID: {student_id}")
                for entry in entries.values():
                    entry.grid_forget()
                return False
            student_data = student_data.iloc[0]
            for i, (label_text, _) in enumerate(fields):
                entry = entries[label_text]
                entry.delete(0, END)
                entry.insert(0, str(student_data[label_text]))
                entry.config(fg="black", state="readonly", font=("Arial", 11))
                entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 +
                           1, padx=15, pady=5, ipadx=7, ipady=5)
            return True
        for i, (label_text, placeholder) in enumerate(fields):
            col = i % 2
            row = (i // 2) + 1
            Label(inner_frame, text=label_text, font=10).grid(
                row=row, column=col * 2, padx=15, pady=5, sticky="w")
            entry = Entry(inner_frame, justify="center")
            entry.grid_forget()
            entries[label_text] = entry
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)
        search_button = Button(
            button_frame, text="Search", command=search_student)
        search_button.pack(side=LEFT, padx=20, pady=10)

        def confirm_delete():
            student_id = student_id_entry.get()
            if not student_id:
                messagebox.showwarning(
                    "Cảnh báo", "Vui lòng nhập ID sinh viên cần xóa.")
                return
            df = pd.read_csv("data/data_clean.csv")
            updated_df = delete_data(df, student_id)
            if updated_df is None:
                messagebox.showerror(
                    "Lỗi", f"Không tìm thấy sinh viên với ID: {student_id}.")
            else:
                updated_df.to_csv("data/data_clean.csv", index=False)
                messagebox.showinfo(
                    "Thành công", f"Đã xóa sinh viên có ID {student_id}")
        confirm_button = Button(
            button_frame, text="Delete", command=confirm_delete)
        confirm_button.pack(side=LEFT, padx=20, pady=10)

    def cleaning(self):
        """Hàm làm sạch dữ liệu."""
        self.clear_content_frame()
        file_path = "data/student-dataset.csv"
        data = pd.read_csv(file_path)
        # Xử lí dữ liệu
        data = handle_missing_value(data)

        # Loại bỏ trùng
        data = remove_duplicates(data)

        # Sửa định dạng
        data = correct_formatting(data)

        # Lưu dữ liệu
        cleaned_file_path = "data/data_clean.csv"
        save_to_cleaned_data_file(cleaned_file_path, data)

        # Thông báo
        messagebox.showinfo(
            "Thông báo", "Làm sạch thành công.")
        self.read()

    def exit_program(self):
        """Thoát chương trình."""
        self.root.destroy()
        subprocess.run(["python", "gui/home_page.py"])


# Khởi chạy ứng dụng
if __name__ == "__main__":
    root = Tk()
    app = StudentManagementApp(root)
    root.mainloop()

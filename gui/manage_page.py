import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sys
import pandas as pd
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data, create_data, update_data, delete_data
from modules.data_cleaning import handle_missing_value, remove_duplicates, correct_formatting, save_to_cleaned_data_file

class StudentManagementApp():
    def __init__(self, root):
        super().__init__()
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
        Label(self.root, text="Quản lí", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        M_Frame = LabelFrame(self.root, text="Menu", bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)
        menu_items = [("Đọc", self.read), ("Thêm", self.create), ("Sửa", self.update),
                      ("Xóa", self.delete), ("Làm sạch", self.cleaning), ("Quay lại", self.exit_program)]
        for i, (text, command) in enumerate(menu_items): # Tạo các nút trong menu
            self.create_menu_button(M_Frame, text, command, i * 75)

    def create_content_frame(self):
        self.content_frame = Frame(self.root, bg="lightgrey")
        self.content_frame.place(x=200, y=80, width=800, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def read(self, file_path="data/data_clean.csv", title="DANH SÁCH SINH VIÊN"):
        self.clear_content_frame()
        try:
            data = pd.read_csv(file_path)
            if data.empty:
                messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
                return
            self.display_data_table(data, title)
        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def display_data_table(self, data, title):
        """
        Hiển thị dữ liệu trong DataFrame dưới dạng bảng.
        :param data: DataFrame chứa dữ liệu cần hiển thị.
        :param title: Tiêu đề của bảng dữ liệu.
        """
        title_label = tk.Label(self.content_frame, text=title, font=("Arial", 14, "bold"), bg="lightgrey")
        title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew") # columnspan=3 để căn giữa tiêu đề
        # Tạo bảng dữ liệu
        v_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical")
        h_scrollbar = ttk.Scrollbar(self.content_frame, orient="horizontal")
        columns = list(data.columns)    # Lấy tên các cột
        tree = ttk.Treeview(self.content_frame, columns=columns, show="headings",
                            yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        for col in columns: # Đặt tên cột
            tree.heading(col, text=col) # Đặt tên cột
            tree.column(col, anchor='center', width=150) # Đặt chiều rộng cột
        for _, row in data.iterrows(): # Thêm dữ liệu vào bảng
            tree.insert("", "end", values=list(row)) # Thêm hàng vào bảng
        tree.grid(row=1, column=0, sticky="nsew") # Đặt bảng vào frame
        v_scrollbar.grid(row=1, column=1, sticky="ns") # Đặt thanh cuộn dọc
        h_scrollbar.grid(row=2, column=0, sticky="ew") # Đặt thanh cuộn ngang
        v_scrollbar.config(command=tree.yview) # Đặt thanh cuộn dọc cho bảng
        h_scrollbar.config(command=tree.xview) # Đặt thanh cuộn ngang cho bảng
        self.content_frame.grid_rowconfigure(1, weight=1) # Đặt trọng số cho hàng 1
        self.content_frame.grid_columnconfigure(0, weight=1) # Đặt trọng số cho cột 0

    def create(self):
        self.clear_content_frame()
        fields = [("ID", "e.g., 0, 1, 2..."), ("Name", "e.g., Kiana Lor"), ("Nationality", "e.g., United States of America"),
                  ("City", "e.g., Oakland"), ("Latitude (vĩ dộ)", "e.g., 37.8"), ("Longitude (kinh độ)", "e.g., -122.27"),
                  ("Gender", "e.g., M/F"), ("Ethnic Group", "e.g., NA"), ("Age", "e.g., 22"), ("English Grade", "e.g., 3.5"),
                  ("Math Grade", "e.g., 3.7"), ("Sciences Grade", "e.g., 3.2"), ("Language Grade", "e.g., 5"),
                  ("Portfolio Rating", "e.g., 4"), ("Cover Letter Rating", "e.g., 5"), ("Reference Letter Rating", "e.g., 4")]
        entries = self.create_form(fields, "THÊM SINH VIÊN") # Tạo form nhập liệu
        self.create_sample_button(entries, fields) # Tạo nút thêm dữ liệu mẫu
        self.create_confirm_button(entries, fields, self.confirm_create,"Create") # Tạo nút xác nhận THÊM SINH VIÊN
 
    def create_form(self, fields, title):
        """ 
        Tạo form nhập liệu để THÊM SINH VIÊN.
        :param fields: Danh sách các trường thông tin sinh viên.
        :param title: Tiêu đề của form.
        """ 
        entries = {}
        title_label = Label(self.content_frame, text=title, font=("Arial", 14, "bold"), bg="lightgrey")
        title_label.pack(pady=10)
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)
       
        for i, (label_text, placeholder) in enumerate(fields):  # Tạo các label và entry widget
            col = i % 2  # Tính toán cột
            row = (i // 2) + 1  # Tính toán vị trí hàng và cột
            
            # Tạo label cho mỗi trường
            Label(field_frame, text=label_text, font=("Arial", 11)).grid(row=row, column=col * 2, padx=15, pady=5, sticky="w")
            
            # Tạo biến lưu giá trị nhập vào
            var = StringVar(value=placeholder)
            entry = Entry(field_frame, textvariable=var, fg="grey", font=("Arial", 11))  # Tạo ô nhập liệu
            entry.grid(row=row, column=col * 2 + 1, padx=15, pady=5)  # Đặt ô nhập liệu vào frame
            
            if title == "CẬP NHẬT SINH VIÊN" or title == "XÓA SINH VIÊN":
            # Nếu là trường 'id', để người dùng nhập bình thường; ngược lại thì vô hiệu hóa
                if label_text != "id":
                     entry.config(state="disabled")  # Vô hiệu hóa các trường không phải 'id'

            # Xử lý sự kiện để làm placeholder
            entry.bind("<FocusIn>", lambda e, var=var, placeholder=placeholder: var.set("") if var.get() == placeholder else None)
            entry.bind("<FocusOut>", lambda e, var=var, placeholder=placeholder: var.set(placeholder) if var.get() == "" else None)
            
            # Thêm entry widget vào dictionary
            entries[label_text] = entry

            


        # Tạo nút xóa dữ liệu nhập vào
        if title == "THÊM SINH VIÊN":
            Button(self.content_frame, text="Clear",width=15, height=2, command=self.create).pack(side=LEFT, padx=0, pady=10, expand=True)
        elif title == "CẬP NHẬT SINH VIÊN":
            Button(self.content_frame, text="Clear",width=15, height=2, command=self.update).pack(side=LEFT, padx=0, pady=10, expand=True)
        elif title == "XÓA SINH VIÊN":
            Button(self.content_frame, text="Clear",width=15, height=2, command=self.delete).pack(side=LEFT, padx=0, pady=10, expand=True)

        return entries
    # Sử dụng lambda khi bạn cần một hàm ngắn gọn cho các tác vụ đơn giản hoặc khi bạn muốn tránh phải định nghĩa một hàm riêng biệt cho một hành động tạm thời.
    def create_sample_button(self, entries, fields):
        sample_button = Button(self.content_frame, text="Thêm dữ liệu mẫu",width=15, height=2, command=lambda: self.fill_sample_data(entries, fields))
        sample_button.pack(side=LEFT, padx=0, pady=10,expand=True)


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
        for label_text, sample_value in sample_data.items():
            entries[label_text].delete(0, END) # Xóa dữ liệu cũ
            entries[label_text].insert(0, sample_value) # Điền dữ liệu mẫu
            entries[label_text].config(fg="black") # Đổi màu chữ

    def create_confirm_button(self, entries, fields, confirm_command,title):
        confirm_button = Button(self.content_frame, text=title,width=15, height=2, command=lambda: confirm_command(entries, fields))
        confirm_button.pack(side=LEFT, padx=0, pady=10,expand=True)

    def confirm_create(self, entries, fields): 
        student_data = [entries[label_text].get() for label_text, _ in fields] # Lấy thông tin sinh viên từ các ô nhập liệu
        for i, (field, placeholder) in enumerate(fields): # Kiểm tra thông tin nhập vào
            df = pd.read_csv("data/data_clean.csv") # Đọc dữ liệu từ file
            if student_data[0] in df['id'].astype(str).values: # Kiểm tra ID đã tồn tại chưa
                messagebox.showwarning("Cảnh báo", "ID đã tồn tại. Vui lòng nhập ID khác.")
                return
            if student_data[i] == placeholder or student_data[i] == "": 
                messagebox.showwarning("Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
                return
        create_data(student_data, "data/data_clean.csv")
        messagebox.showinfo("Thành công", "Dữ liệu đã được thêm vào!")

    # Update
    def update(self):
        self.clear_content_frame()
        fields = [("id", "e.g., 0, 1, 2..."), ("name", "e.g., Kiana Lor"), ("nationality", "e.g., United States of America"),
                  ("city", "e.g., Oakland"), ("latitude", "e.g., 37.8"), ("longitude", "e.g., -122.27"), ("gender", "e.g., M/F"),
                  ("ethnic.group", "e.g., NA"), ("age", "e.g., 22"), ("english.grade", "e.g., 3.5"), ("math.grade", "e.g., 3.7"),
                  ("sciences.grade", "e.g., 3.2"), ("language.grade", "e.g., 5"), ("portfolio.rating", "e.g., 4"),
                  ("coverletter.rating", "e.g., 5"), ("refletter.rating", "e.g., 4")]
        entries = self.create_form(fields, "CẬP NHẬT SINH VIÊN")
        self.create_search_button(entries, fields, self.search_student_for_update)
        self.create_confirm_button(entries, fields, self.confirm_update,"Update")

    def create_search_button(self, entries, fields, search_command):
        search_button = Button(self.content_frame, text="Search",width = 15, height = 2, command=lambda: search_command(entries, fields))
        search_button.pack(side=LEFT, padx=0, pady=10, expand=True)

    def search_student_for_update(self, entries, fields):
        # Kích hoạt tất cả các trường
        for label_text, entry in entries.items():
            if label_text != "id":
                entry.config(state="normal")

        # Lấy ID sinh viên       
        student_id = entries["id"].get()
        df = pd.read_csv("data/data_clean.csv")
        student_data = df[df['id'].astype(str) == student_id]
        if student_data.empty:
            messagebox.showerror("Error", f"Không tìm thấy sinh viên có ID: {student_id}")
            self.update()  # Hiển thị lại form xóa
            return False
        student_data = student_data.iloc[0] # Lấy thông tin sinh viên

        # chèn data tìm thấy vào entry widget
        for i, (label_text, _) in enumerate(fields): # Điền thông tin sinh viên vào các ô nhập liệu
            entry = entries[label_text] # Lấy entry widget
            entry.delete(0, END) # Xóa dữ liệu cũ
            entry.insert(0, str(student_data[label_text])) # Điền dữ liệu sinh viên
            entry.config(fg="black", font=("Arial", 11)) # Đổi màu chữ và chỉ đọc
            entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 + 1, padx=15, pady=5, ipadx=7, ipady=5) # Đặt ô nhập liệu vào frame
        return True

    def confirm_update(self, entries, fields):
        student_id = str(entries["id"].get())
        # Lấy thông tin sinh viên từ các ô nhập liệu: duyệt từng labeltext và placeholder trong fields, lấy giá trị từ entry widget tương ứng
        new_data = [entries[label_text].get() for label_text, _ in fields] 
        for i, (field, placeholder) in enumerate(fields): # Kiểm tra thông tin nhập vào
            if new_data[i] == "": # Nếu ô nhập liệu trống
                messagebox.showwarning("Cảnh báo", f"Hãy điền đầy đủ các trường '{field}'")
                return
        if update_data(student_id, new_data):
            messagebox.showinfo("Thành công!", "Đã cập nhật thông tin sinh viên.")
        else:
            messagebox.showerror("Cập nhật thất bại.", f"Không tìm thấy sinh viên với ID: {student_id}")
    
    # Delete
    def delete(self):
        self.clear_content_frame()
        fields = [("id", "e.g., 0, 1, 2..."), ("name", "e.g., Kiana Lor"), ("nationality", "e.g., United States of America"),
                  ("city", "e.g., Oakland"), ("latitude", "e.g., 37.8"), ("longitude", "e.g., -122.27"), ("gender", "e.g., M/F"),
                  ("ethnic.group", "e.g., NaN/Asia/.."), ("age", "e.g., 22"), ("english.grade", "e.g., 3.5"), ("math.grade", "e.g., 3.7"),
                  ("sciences.grade", "e.g., 3.2"), ("language.grade", "e.g., 5"), ("portfolio.rating", "e.g., 4"),
                  ("coverletter.rating", "e.g., 5"), ("refletter.rating", "e.g., 4")]
        entries = self.create_form(fields, "XÓA SINH VIÊN")
        self.create_search_button(entries, fields, self.search_student_for_delete)
        self.create_confirm_button(entries, fields, self.confirm_delete,"Delete")

    def search_student_for_delete(self, entries, fields):
        # Kích hoạt tất cả các trường
        for label_text, entry in entries.items():
            if label_text != "id":
                entry.config(state="normal")
        # Lấy ID sinh viên
        student_id = entries["id"].get()
        df = pd.read_csv("data/data_clean.csv")
        student_data = df[df['id'].astype(str) == student_id] # Tìm sinh viên
        if student_data.empty: # Nếu không tìm thấy sinh viên
            messagebox.showerror("Error", f"Không tìm thấy sinh viên có ID: {student_id}")
            self.delete()  # Hiển thị lại form xóa
            return False
        student_data = student_data.iloc[0] # Lấy thông tin sinh viên
        for i, (label_text, _) in enumerate(fields): # Điền thông tin sinh viên vào các ô nhập liệu
            entry = entries[label_text] # Lấy entry widget
            entry.delete(0, END) # Xóa dữ liệu cũ
            entry.insert(0, str(student_data[label_text])) # Điền dữ liệu sinh viên
            entry.config(fg="black", state="readonly", font=("Arial", 11)) # Đổi màu chữ và chỉ đọc
            entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 + 1, padx=15, pady=5, ipadx=7, ipady=5) # Đặt ô nhập liệu vào frame
        return True

    def confirm_delete(self, entries, fields):
        student_id = entries["id"].get() # Lấy ID sinh viên
        if not student_id:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID sinh viên cần xóa.")
            return
        df = pd.read_csv("data/data_clean.csv")
        updated_df = delete_data(df, student_id)
        if updated_df is None:
            messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên với ID: {student_id}.")
        else:
            updated_df.to_csv("data/data_clean.csv", index=False)
            messagebox.showinfo("Thành công", f"Đã XÓA SINH VIÊN có ID {student_id}")

    # Cleaning
    def cleaning(self):
        self.clear_content_frame()
        file_path = "data/student-dataset.csv"
        data = pd.read_csv(file_path)
        data = handle_missing_value(data)
        data = remove_duplicates(data)
        data = correct_formatting(data)
        cleaned_file_path = "data/data_clean.csv"
        save_to_cleaned_data_file(cleaned_file_path, data)
        messagebox.showinfo("Thông báo", "Làm sạch thành công.")
        self.read()

    def exit_program(self):
        self.root.destroy()
        subprocess.run(["python", "gui/home_page.py"])

if __name__ == "__main__":
    root = Tk()
    app = StudentManagementApp(root)
    root.mainloop()

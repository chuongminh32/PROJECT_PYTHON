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


class StudentManagementAppUser:
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
        self.create_menu_button(M_Frame, "Back", self.exit_program, 290)
        
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
        self.clear_content_frame()
        try:
            file_path = "data/student-dataset.csv"
            data = read_data(file_path)
            if not data:
                messagebox.showinfo(
                    "Thông báo", "Không có dữ liệu để hiển thị.")
                return
            v_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical")
            h_scrollbar = ttk.Scrollbar(
                self.content_frame, orient="horizontal")
            columns = data[0]
            tree = ttk.Treeview(self.content_frame, columns=columns, show="headings",
                                yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor='center', width=150)
            for row in data[1:]:
                tree.insert("", "end", values=row)
            tree.grid(row=0, column=0, sticky="nsew")
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            h_scrollbar.grid(row=1, column=0, sticky="ew")
            v_scrollbar.config(command=tree.yview)
            h_scrollbar.config(command=tree.xview)
            self.content_frame.grid_rowconfigure(0, weight=1)
            self.content_frame.grid_columnconfigure(0, weight=1)
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
        for i, (label_text, placeholder) in enumerate(fields):
            col = i % 2
            row = (i // 2) + 1
            Label(field_frame, text=label_text, font=("Arial", 11)).grid(
                row=row, column=col * 2, padx=15, pady=5, sticky="w")
            var = StringVar(value=placeholder)
            entry = Entry(field_frame, textvariable=var, fg="grey",
                          font=("Arial", 11), state="readonly")
            entry.grid(row=row, column=col * 2 + 1, padx=15, pady=5)
            entries[label_text] = entry
            entry.bind("<FocusIn>", lambda e, var=var, placeholder=placeholder: var.set(
                "") if var.get() == placeholder else None)
            entry.bind("<FocusOut>", lambda e, var=var, placeholder=placeholder: var.set(
                placeholder) if var.get() == "" else None)
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)
        Button(button_frame, text="Thêm dữ liệu mẫu", command=lambda: messagebox.showinfo(
            "Thông báo", "Bạn không có quyền khởi tạo.")).pack(side=LEFT, padx=20, pady=10)
        Button(button_frame, text="Create", command=lambda: messagebox.showinfo(
            "Thông báo", "Bạn không có quyền khởi tạo.")).pack(side=RIGHT, padx=20, pady=10)

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
            df = pd.read_csv("data/student-dataset.csv")
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
                entry.config(fg="black", font=("Arial", 11))
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
        Button(button_frame, text="Search", command=search_student).pack(
            side=LEFT, padx=20, pady=10)
        Button(button_frame, text="Update", command=lambda: messagebox.showinfo(
            "Thông báo", "Bạn không có quyền cập nhật.")).pack(side=RIGHT, padx=20, pady=10)

    def delete(self):
        """Xóa sinh viên."""
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
            df = pd.read_csv("data/student-dataset.csv")
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
        Button(button_frame, text="Search", command=search_student).pack(
            side=LEFT, padx=20, pady=10)
        Button(button_frame, text="Delete", command=lambda: messagebox.showinfo(
            "Thông báo", "Bạn không có quyền xóa.")).pack(side=LEFT, padx=20, pady=10)

    def exit_program(self):
        """Thoát chương trình."""
        self.root.destroy()
        subprocess.run(["python", "gui/home_page_user.py"])


def main():
    root = Tk()
    app = StudentManagementAppUser(root)
    root.mainloop()


if __name__ == "__main__":
    main()
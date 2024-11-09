import os
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sys
import pandas as pd

# # Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data, create_data, update_data, delete_data  

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()
        self.create_content_frame()  # Thêm vùng hiển thị nội dung
        root.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ

    def setup_window(self):
        """Thiết lập cửa sổ chính."""
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")

    def create_logo(self):
        """Tạo logo cho ứng dụng."""
        logo_path = os.path.join("images", "logo.png")
        logo_image = Image.open(logo_path).resize((20, 20))
        self.logo_dash = ImageTk.PhotoImage(logo_image)

        Label(self.root, text="Student Management Mini", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        """Tạo menu cho ứng dụng."""
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Read", self.read, 0)
        self.create_menu_button(M_Frame, "Create", self.create, 75)
        self.create_menu_button(M_Frame, "Update", self.update, 150)
        self.create_menu_button(M_Frame, "Delete", self.delete, 220)
        self.create_menu_button(M_Frame, "Exit", self.exit_program, 290)

    def create_content_frame(self):
        """Tạo vùng hiển thị nội dung."""
        self.content_frame = Frame(self.root, bg="lightgrey")
        self.content_frame.place(x=200, y=80, width=800, height=470)
        # self.content_frame.place(x=200, y=80, relwidth=1, relheight=1)

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

    def read(self):
        """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra bảng trong cửa sổ hiện tại."""
        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        try:
            file_path = "data/student-dataset.csv"  # Đường dẫn đến file CSV
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
                tree.column(col, anchor='center', width=150)

            # Thêm dữ liệu vào bảng
            for row in data[1:]:
                tree.insert("", "end", values=row)

            # Đặt Treeview và thanh cuộn vào content_frame
            tree.grid(row=0, column=0, sticky="nsew")
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            h_scrollbar.grid(row=1, column=0, sticky="ew")

            # Kết nối thanh cuộn với Treeview
            v_scrollbar.config(command=tree.yview)
            h_scrollbar.config(command=tree.xview)

            # Thiết lập tỷ lệ mở rộng cho Treeview
            self.content_frame.grid_rowconfigure(0, weight=1)
            self.content_frame.grid_columnconfigure(0, weight=1)

        except FileNotFoundError:
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def create(self):
        """Hàm cho chức năng Create - Tạo bảng nhập dữ liệu sinh viên với các gợi ý cho từng trường."""

        self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

        fields = [
            ("ID", "e.g., 0, 1, 2..."),
            ("Name", "e.g., Kiana Lor"),
            ("Nationality", "e.g., United States of America"),
            ("City", "e.g., Oakland"),
            ("Latitude (vĩ dộ)", "e.g., 37.8"),
            ("Longitude (kinh độ)", "e.g., -122.27"),
            ("Gender", "e.g., M/F"),
            ("Ethnic Group", "e.g., NA"),
            ("Age", "e.g., 22"),
            ("English Grade", "e.g., 3.5"),
            ("Math Grade", "e.g., 3.7"),
            ("Sciences Grade", "e.g., 3.2"),
            ("Language Grade", "e.g., 5"),
            ("Portfolio Rating", "e.g., 4"),
            ("Cover Letter Rating", "e.g., 5"),
            ("Reference Letter Rating", "e.g., 4")
        ]

        entries = {}

        # Tạo frame chứa các ô nhập liệu
        field_frame = Frame(self.content_frame) 
        # field_frame.pack(pady=10, padx=15)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)
        # Tạo tiêu đề
        Label(field_frame, text="Thêm sinh viên", font=("Arial", 12, "bold")).grid(row=0, column=1, columnspan=2, pady=5)
        for i, (label_text, placeholder) in enumerate(fields):
            col = i % 2  # Xác định cột (0 hoặc 1)
            row = (i // 2) + 1  # Xác định hàng (+1 để bỏ qua hàng tiêu đề)
            Label(field_frame, text=label_text, font=("Arial", 11)).grid(
            row=row, column=col * 2, padx=15, pady=5, sticky="w") # Đặt label

            var = StringVar(value=placeholder)
            entry = Entry(field_frame, textvariable=var, fg="grey", font=("Arial", 11)) # Tạo ô nhập liệu
            entry.grid(row=row, column=col * 2 + 1, padx=15, pady=5) # Đặt entry
            entries[label_text] = entry # Lưu entry vào từ điển

            def clear_placeholder(e, var=var, placeholder=placeholder): # Xóa placeholder khi người dùng nhấn vào ô nhập liệu
                if var.get() == placeholder:
                    var.set("")
                    entry.config(fg="black")

            def restore_placeholder(e, var=var, placeholder=placeholder): # Hiển thị placeholder khi ô nhập liệu trống
                if var.get() == "":
                    var.set(placeholder)
                    entry.config(fg="grey")

            # Khi người dùng nhấn vào ô nhập liệu, nếu placeholder hiển thị thì xóa nó
            entry.bind("<FocusIn>", clear_placeholder)
            # Khi người dùng rời khỏi ô nhập liệu, nếu ô nhập liệu trống thì hiển thị placeholder
            entry.bind("<FocusOut>", restore_placeholder)

        # Tạo Frame riêng cho các nút để cố định vị trí của chúng
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)

        # Thêm hàm để điền dữ liệu mẫu
        def fill_sample_data():
            sample_data = {
                "ID": "1",
                "Name": "Chuong Min",
                "Nationality": "Vietnam",
                "City": "Ho Chi Minh",
                "Latitude (vĩ dộ)": "37.8",
                "Longitude (kinh độ)": "-122.27",
                "Gender": "F",
                "Ethnic Group": "NA",
                "Age": "22",
                "English Grade": "4.0",
                "Math Grade": "3.9",
                "Sciences Grade": "3.8",
                "Language Grade": "5",
                "Portfolio Rating": "4",
                "Cover Letter Rating": "5",
                "Reference Letter Rating": "4"
            }
            for label_text, sample_value in sample_data.items():
                entries[label_text].delete(0, END)
                entries[label_text].insert(0, sample_value) # Điền dữ liệu mẫu
                entries[label_text].config(fg="black")  # Đổi màu chữ thành đen khi điền dữ liệu mẫu

        # Thêm nút "Thêm dữ liệu mẫu"
        sample_button = Button(button_frame, text="Thêm dữ liệu mẫu", command=fill_sample_data)
        sample_button.pack(side=LEFT, padx=20, pady=10)


        # Thêm nút xác nhận
        def confirm():
            student_data = [entries[label_text].get() for label_text, _ in fields]  # '_' bỏ qua giá trị placeholder

            for i, (field, placeholder) in enumerate(fields):
                if student_data[i] == placeholder or student_data[i] == "":
                    messagebox.showwarning("Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
                    return

            create_data(student_data, "data/student-dataset.csv")
            messagebox.showinfo("Thành công", "Dữ liệu đã được thêm vào!")

        confirm_button = Button(button_frame,text="Create", command=confirm)
        confirm_button.pack(side=RIGHT, padx=20, pady=10)
    def update(self):
        """Hàm cho chức năng Update - Tìm kiếm và cập nhật thông tin sinh viên dựa trên ID."""
        self.clear_content_frame()  

        fields = [
            ("id", "e.g., 0, 1, 2..."),
            ("name", "e.g., Kiana Lor"),
            ("nationality", "e.g., United States of America"),
            ("city", "e.g., Oakland"),
            ("latitude", "e.g., 37.8"),
            ("longitude", "e.g., -122.27"),
            ("gender", "e.g., M/F"),
            ("ethnic.group", "e.g., NA"),
            ("age", "e.g., 22"),
            ("english.grade", "e.g., 3.5"),
            ("math.grade", "e.g., 3.7"),
            ("sciences.grade", "e.g., 3.2"),
            ("language.grade", "e.g., 5"),
            ("portfolio.rating", "e.g., 4"),
            ("coverletter.rating", "e.g., 5"),
            ("refletter.rating", "e.g., 4")
        ]

        # Tạo một từ điển để lưu trữ các ô nhập liệu
        entries = {}

        # Tạo frame chứa các ô nhập liệu
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)

        # Tạo frame con để căn giữa nội dung
        inner_frame = Frame(field_frame) # Tạo frame con
        inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER) #  Căn giữa

        # Tạo thanh tìm kiếm
        Label(inner_frame, text="Nhập ID Sinh Viên:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
        student_id_entry = Entry(inner_frame, justify="center") # Căn giữa
        student_id_entry.grid(row=0, column=2, columnspan=2, padx=10, pady=5)
        # Hàm clear_content_frame() đã có sẵn để xóa các nội dung cũ, giữ lại phần nhập ID và nút tìm kiếm.

        def search_student():
            student_id = student_id_entry.get()
            df = pd.read_csv("data/student-dataset.csv")

            # Kiểm tra nếu không tìm thấy sinh viên nào với ID đã nhập
            student_data = df[df['id'].astype(str) == student_id]

            if student_data.empty:
                messagebox.showerror("Error", f"Không tìm thấy sinh viên có ID: {student_id}")
                # Ẩn các trường thông tin sinh viên
                for entry in entries.values():
                    entry.grid_forget() # Ẩn entry khi không tìm thấy sinh viên
                return False

            # Lấy thông tin sinh viên từ dòng đầu tiên
            student_data = student_data.iloc[0]

            # Điền thông tin sinh viên vào các ô nhập liệu và hiện chúng lên
            for i, (label_text, _) in enumerate(fields):
                entry = entries[label_text]  # Lấy entry từ từ điển
                entry.delete(0, END)  # Xóa dữ liệu cũ
                entry.insert(0, str(student_data[label_text]))  # Điền thông tin sinh viên vào ô nhập liệu
                entry.config(fg="black", font=("Arial", 11))  # Đổi màu chữ thành đen và tăng kích thước chữ
                # Hiển thị các entry tương ứng với label
                entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 + 1, padx=15, pady=5, ipadx=7, ipady=5)  # Căn giữa và tăng kích thước ô

            return True

        # Tạo ô nhập liệu cho từng trường thông tin
        for i, (label_text, placeholder) in enumerate(fields):
            col = i % 2
            row = (i // 2) + 1
            Label(inner_frame, text=label_text, font=10).grid(row=row, column=col * 2, padx=15, pady=5, sticky="w")  # Đặt label
            entry = Entry(inner_frame, justify="center")  # Tạo ô nhập liệu
            # Ban đầu ẩn các entry
            entry.grid_forget()  # Ẩn entry khi mới bắt đầu
            entries[label_text] = entry  # Lưu entry vào từ điển

        # Tạo nút
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)

        # Nút tìm kiếm
        search_button = Button(button_frame, text="Search", command=search_student)
        search_button.pack(side=LEFT, padx=20, pady=10) 

        # Nút Xác nhận
        def confirm_update():
            student_id = str(student_id_entry.get())
            new_data = [entries[label_text].get() for label_text, _ in fields] # Lấy thông tin mới từ các ô nhập liệu

            for i, (field, placeholder) in enumerate(fields): # Kiểm tra xem có trường nào trống không
                if  new_data[i] == "":
                    messagebox.showwarning("Cảnh báo", f"Hãy điền đầy đủ các trường '{field}'")
                    return

            if update_data(student_id, new_data):
                messagebox.showinfo("Thành công!","Đã cập nhật thông tin sinh viên.")
            else:
                messagebox.showerror("Cập nhật thất bại.", f"Không tìm thấy sinh viên với ID: {student_id}")

        confirm_button = Button(button_frame, text="Update", command=confirm_update)
        confirm_button.pack(side=RIGHT, padx=20, pady=10)


    def delete(self):
        """Hàm cho chức năng Delete - Xóa sinh viên."""
        self.clear_content_frame()  

        fields = [
            ("id", "e.g., 0, 1, 2..."),
            ("name", "e.g., Kiana Lor"),
            ("nationality", "e.g., United States of America"),
            ("city", "e.g., Oakland"),
            ("latitude", "e.g., 37.8"),
            ("longitude", "e.g., -122.27"),
            ("gender", "e.g., M/F"),
            ("ethnic.group", "e.g., NA"),
            ("age", "e.g., 22"),
            ("english.grade", "e.g., 3.5"),
            ("math.grade", "e.g., 3.7"),
            ("sciences.grade", "e.g., 3.2"),
            ("language.grade", "e.g., 5"),
            ("portfolio.rating", "e.g., 4"),
            ("coverletter.rating", "e.g., 5"),
            ("refletter.rating", "e.g., 4")
        ]

        # Tạo một từ điển để lưu trữ các ô nhập liệu
        entries = {}

        # Tạo frame chứa các ô nhập liệu
        field_frame = Frame(self.content_frame)
        field_frame.pack(fill="both", expand=True, pady=10, padx=15)

         # Tạo frame con để căn giữa nội dung
        inner_frame = Frame(field_frame) # Tạo frame con
        inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER) #  Căn giữa

        # Tạo thanh tìm kiếm
        Label(inner_frame, text="Nhập ID Sinh Viên:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
        student_id_entry = Entry(inner_frame, justify="center") # Căn giữa
        student_id_entry.grid(row=0, column=2, columnspan=2, padx=10, pady=5)
        # Hàm clear_content_frame() đã có sẵn để xóa các nội dung cũ, giữ lại phần nhập ID và nút tìm kiếm.

        def search_student():
            student_id = student_id_entry.get()
            df = pd.read_csv("data/student-dataset.csv")

            # Kiểm tra nếu không tìm thấy sinh viên nào với ID đã nhập
            student_data = df[df['id'].astype(str) == student_id]

            if student_data.empty:
                messagebox.showerror("Error", f"Không tìm thấy sinh viên có ID: {student_id}")
                # Ẩn các trường thông tin sinh viên
                for entry in entries.values():
                    entry.grid_forget() # Ẩn entry khi không tìm thấy sinh viên
                return False

            # Lấy thông tin sinh viên từ dòng đầu tiên
            student_data = student_data.iloc[0]

            # Điền thông tin sinh viên vào các ô nhập liệu và hiện chúng lên
            for i, (label_text, _) in enumerate(fields):
                entry = entries[label_text]  # Lấy entry từ từ điển
                entry.delete(0, END)  # Xóa dữ liệu cũ
                entry.insert(0, str(student_data[label_text]))  # Điền thông tin sinh viên vào ô nhập liệu
                entry.config(fg="black", state="readonly", font=("Arial", 11))  # Đổi màu chữ thành đen và tăng kích thước chữ
                # Hiển thị các entry tương ứng với label
                entry.grid(row=(i // 2) + 1, column=(i % 2) * 2 + 1, padx=15, pady=5, ipadx=7, ipady=5)  # Căn giữa và tăng kích thước ô

            return True

        # Tạo ô nhập liệu cho từng trường thông tin
        for i, (label_text, placeholder) in enumerate(fields):
            col = i % 2
            row = (i // 2) + 1
            Label(inner_frame, text=label_text, font=10).grid(row=row, column=col * 2, padx=15, pady=5, sticky="w")  # Đặt label
            entry = Entry(inner_frame, justify="center")  # Tạo ô nhập liệu
            # Ban đầu ẩn các entry
            entry.grid_forget()  # Ẩn entry khi mới bắt đầu
            entries[label_text] = entry  # Lưu entry vào từ điển

        # Tạo nút
        button_frame = Frame(self.content_frame)
        button_frame.pack(pady=10)

        # Nút tìm kiếm
        search_button = Button(button_frame, text="Search", command=search_student)
        search_button.pack(side=LEFT, padx=20, pady=10)

        # Định nghĩa hàm xác nhận việc xóa sinh viên
        def confirm_delete():
            student_id = student_id_entry.get()
            if not student_id:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID sinh viên cần xóa.")
                return

            df = pd.read_csv("data/data_clean.csv")
            updated_df = delete_data(df, student_id)
            if updated_df is None:
                messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên với ID: {student_id}.")
            else:
                updated_df.to_csv("data/data_clean.csv", index=False)
                messagebox.showinfo("Thành công", f"Đã xóa sinh viên có ID {student_id}")
                delete_window.destroy()

        # Nút Xóa
        confirm_button = Button(button_frame, text="Delete", command=confirm_delete)
        confirm_button.pack(side=LEFT, padx=20, pady=10)


    def exit_program(self):
        """Chức năng thoát chương trình."""
        self.root.destroy()


def main():
    root = Tk()
    app = StudentManagementApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

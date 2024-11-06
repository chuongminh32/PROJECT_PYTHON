# import os
# import sys
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import subprocess
# import csv
# import pandas as pd


# # Thêm thư mục gốc của dự án vào sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from modules.data_crud import read_data, create_data, update_data, delete_data  # Cập nhật đường dẫn import nếu cần

# def open_manage_page():
#     """Hàm để mở trang quản lý sinh viên."""
#     manage_root = Tk()
#     manage_root.title("Quản lý sinh viên")
#     manage_root.geometry("1000x550+300+200")
#     manage_root.configure(background="white")

#     # === Icon ===
#     logo_path = os.path.join("images", "logo.png")
#     logo_image = Image.open(logo_path).resize((20, 20))
#     logo_dash = ImageTk.PhotoImage(logo_image)

#     # === Title ===
#     title = Label(manage_root, text="Students Management", image=logo_dash, padx=10, compound=LEFT, bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
#     title.place(x=0, y=0, relwidth=1, height=80)

#     # === Back Button ===
#     back_button = Button(manage_root, text="Back", border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
#                          command=lambda: return_to_home(manage_root))
#     back_button.place(x=20, y=100, width=90, height=30)

#     # === Menu ===
#     M_Frame = LabelFrame(manage_root, text="Menu", bg="white", font=("Arial", 12, "bold"))
#     M_Frame.place(x=0, y=150, width=200, relheight=1)

#     # Thêm các nút vào khung menu
#     create_menu_button(M_Frame, "Create", create, 0)
#     create_menu_button(M_Frame, "Read", read, 70)
#     create_menu_button(M_Frame, "Update", update, 140)
#     create_menu_button(M_Frame, "Delete", delete, 210)

#     # === Background ===
#     bg_manage = Image.open("images/bg_manage.png")
#     bg_manage = bg_manage.resize((1150, 700))
#     bg_manage = ImageTk.PhotoImage(bg_manage)
#     background_label = Label(manage_root, image=bg_manage)
#     background_label.place(x=200, y=80, relwidth=1, relheight=1)

#     manage_root.mainloop() # Chạy chương trình

# def return_to_home(manage_root):
#     """Hàm để quay lại trang chính."""
#     manage_root.destroy()
#     subprocess.run(["python", "gui/home_page.py"])

# def create_menu_button(parent, text, command, y_position):
#     """Hàm để tạo nút trong khung menu."""
#     button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
#     button.place(x=0, y=y_position, width=200, height=50)
#     button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
#     button.bind("<Leave>", lambda e: button.config(bg="#242533"))
#     return button

# def read():

#     """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra một cửa sổ mới dưới dạng bảng."""

#     try:
#         data = read_data()  # Gọi hàm để lấy dữ liệu từ file CSV
#         if data is None:
#             messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
#             return

#         # Tạo một cửa sổ mới để hiển thị bảng dữ liệu
#         display_window = Toplevel()
#         display_window.title("Dữ liệu sinh viên")
#         display_window.geometry("700x550+300+200")

#         # Tạo khung chứa Treeview và thanh cuộn
#         frame = ttk.Frame(display_window)
#         frame.pack(fill="both", expand=True)

#         # Tạo thanh cuộn dọc và ngang
#         v_scrollbar = ttk.Scrollbar(frame, orient="vertical")
#         h_scrollbar = ttk.Scrollbar(frame, orient="horizontal")

#         # Tạo Treeview để hiển thị bảng dữ liệu
#         columns = data[0]  # Lấy hàng đầu tiên làm tên cột
#         tree = ttk.Treeview(frame, columns=columns, show="headings",
#                              yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

#         # Đặt thanh cuộn cho Treeview
#         v_scrollbar.config(command=tree.yview)
#         h_scrollbar.config(command=tree.xview)

#         # Đặt tiêu đề cho mỗi cột và tùy chỉnh độ rộng
#         for col in columns:
#             tree.heading(col, text=col)
#             tree.column(col, anchor='center', width=150)  # Đặt độ rộng cột 150

#         # Thêm dữ liệu vào bảng với đường kẻ
#         for index, row in enumerate(data[1:]):
#             if index % 2 == 0:
#                 tree.insert("", "end", values=row, tags=("evenrow",))
#             else:
#                 tree.insert("", "end", values=row, tags=("oddrow",))

#         # Thiết lập màu sắc cho các hàng
#         tree.tag_configure("evenrow", background="#f9f9f9")  # Màu nền cho hàng chẵn
#         tree.tag_configure("oddrow", background="white")      # Màu nền cho hàng lẻ

#         # Đặt Treeview và thanh cuộn vào khung
#         tree.grid(row=0, column=0, sticky="nsew")
#         v_scrollbar.grid(row=0, column=1, sticky="ns")
#         h_scrollbar.grid(row=1, column=0, sticky="ew")

#         # Thiết lập tỷ lệ mở rộng cho Treeview
#         frame.grid_rowconfigure(0, weight=1)
#         frame.grid_columnconfigure(0, weight=1)

#     except FileNotFoundError:
#         messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")


# def create():
#     """Hàm cho chức năng Create - Tạo bảng nhập dữ liệu sinh viên với các gợi ý cho từng trường."""
#     create_window = Toplevel()
#     create_window.title("Thêm sinh viên mới")
#     create_window.geometry("700x550+300+200")

#     fields = [
#         ("ID", "e.g., 0, 1, 2..."),
#         ("Name", "e.g., Kiana Lor"),
#         ("Nationality", "e.g., United States of America"),
#         ("City", "e.g., Oakland"),
#         ("Latitude (vĩ dộ)", "e.g., 37.8"),
#         ("Longitude (kinh độ)", "e.g., -122.27"),
#         ("Gender", "e.g., M/F"),
#         ("Ethnic Group", "e.g., NA"),
#         ("Age", "e.g., 22"),
#         ("English Grade", "e.g., 3.5"),
#         ("Math Grade", "e.g., 3.7"),
#         ("Sciences Grade", "e.g., 3.2"),
#         ("Language Grade", "e.g., 5"),
#         ("Portfolio Rating", "e.g., 4"),
#         ("Cover Letter Rating", "e.g., 5"),
#         ("Reference Letter Rating", "e.g., 4")
#     ]

#     entries = {}

#     # Chia số trường thành hai cột
#     for i, (label_text, placeholder) in enumerate(fields):
#         col = i % 2  # Xác định cột (0 hoặc 1)
#         row = i // 2  # Xác định hàng
#         Label(create_window, text=label_text).grid(row=row, column=col * 2, padx=10, pady=5, sticky="w")

#         var = StringVar(value=placeholder)
#         entry = Entry(create_window, textvariable=var, fg="grey")
#         entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5)
#         entries[label_text] = entry

#         def clear_placeholder(e, var=var, placeholder=placeholder):
#             if var.get() == placeholder:
#                 var.set("")
#                 entry.config(fg="black")

#         def restore_placeholder(e, var=var, placeholder=placeholder):
#             if var.get() == "":
#                 var.set(placeholder)
#                 entry.config(fg="grey")

#         # Khi người dùng nhấn vào ô nhập liệu, nếu placeholder hiện thị thì xóa nó
#         entry.bind("<FocusIn>", clear_placeholder)
#         # Khi người dùng rời khỏi ô nhập liệu, nếu ô nhập liệu trống thì hiển thị placeholder
#         entry.bind("<FocusOut>", restore_placeholder)

#     def add_sample_data():
#         """Thêm dữ liệu mẫu vào file CSV khi nút được nhấn."""
#         sample_data = [
#             [1, "Chuong Pham", "Vietnam", "Quang Ngai", 10.8231, 106.6297, "Male", "Kinh", 19, 8.5, 9.0,
#              8.0, 7.5, 4.5, 4.0, 5.0],
#             [2, "Minh Nguyen", "Vietnam", "Dong Nai", 21.0285, 105.8542, "Female", "Kinh", 19, 9.0, 8.5,
#              9.5, 8.0, 4.0, 4.5, 5.5],
#             [3, "Thuy Nguyen", "Vietnam", "Dong Nai", 16.0583, 108.2215, "Female", "Kinh", 19, 7.0, 8.0,
#              6.5, 8.5, 3.5, 3.0, 4.0]
#         ]

#         file_path = 'data/data_clean.csv'  # Đường dẫn đến file CSV
#         for data in sample_data:
#             create_data(data, file_path)

#         messagebox.showinfo("Thành công", "Dữ liệu mẫu đã được thêm vào file CSV!")

#     # Tạo nút để thêm dữ liệu mẫu
#     add_button = Button(create_window, text="Thêm Dữ Liệu Mẫu", command=add_sample_data)
#     add_button.grid(row=len(fields) // 2 + 1, column=1, padx=10, pady=10)

#     def confirm():
#         student_data = [entries[label_text].get() for label_text, _ in fields]

#         for i, (field, placeholder) in enumerate(fields):
#             if student_data[i] == placeholder or student_data[i] == "":
#                 messagebox.showwarning("Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
#                 return

#         create_data(student_data, "data/data_clean.csv")
#         create_window.destroy()

#     confirm_button = Button(create_window, text="Xác nhận", command=confirm)
#     confirm_button.grid(row=len(fields) // 2 + 1, column=2, padx=10, pady=10)


# def update():
#     """Mở cửa sổ để nhập thông tin cập nhật sinh viên."""
#     update_window = Toplevel()
#     update_window.title("Cập nhật thông tin sinh viên")
#     update_window.geometry("550x550+300+200")

#     # Tạo Canvas để cuộn
#     canvas = Canvas(update_window)
#     canvas.pack(side=LEFT, fill=BOTH, expand=True)

#     # Thanh cuộn dọc
#     scrollbar = Scrollbar(update_window, orient=VERTICAL, command=canvas.yview)
#     scrollbar.pack(side=RIGHT, fill=Y)
#     canvas.configure(yscrollcommand=scrollbar.set)

#     # Tạo Frame chứa các ô nhập liệu
#     form_frame = Frame(canvas)
#     canvas.create_window((0, 0), window=form_frame, anchor="nw")

#     # Nhập ID sinh viên
#     Label(form_frame, text="Nhập ID sinh viên để tìm kiếm:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
#     student_id_entry = Entry(form_frame)
#     student_id_entry.grid(row=0, column=1, padx=10, pady=5)

#     # Nút Tìm Kiếm
#     search_button = Button(form_frame, text="Tìm kiếm", command=lambda: search_student(student_id_entry.get(), form_frame, canvas))
#     search_button.grid(row=1, column=0, columnspan=2, pady=10)

#     def search_student(student_id, form_frame, canvas):
#         """Tìm sinh viên theo ID và điền thông tin hiện tại nếu tìm thấy."""
#         df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file data_clean.csv

#         # Kiểm tra nếu ID có trong DataFrame
#         if student_id not in df['id'].astype(str).values:
#             messagebox.showerror("Lỗi", f"Không thấy sinh viên với ID: {student_id}.")
#             return False
#         else:
#             # Lấy dữ liệu sinh viên tương ứng, iloc[0] để lấy hàng đầu tiên (có nhiều data id trùng -> ưu tiên lấy dòng đầu tiên)
#             student_data = df[df['id'].astype(str) == student_id].iloc[0]

#             # Hiển thị các ô nhập liệu và điền thông tin
#             fields = student_data.index.tolist()  # Lấy danh sách các trường dữ liệu của sinh viên
#             entries = {}  # Dictionary lưu trữ các ô nhập liệu cho từng trường
#             for i, field in enumerate(fields, start=2):
#                 # Tạo nhãn (label) cho từng trường dữ liệu
#                 Label(form_frame, text=f"{field}:").grid(row=i, column=0, padx=10, pady=5, sticky="w")

#                 # Tạo ô nhập liệu (entry) cho từng trường
#                 entry = Entry(form_frame)
#                 entry.grid(row=i, column=1, padx=10, pady=5)

#                 # Điền dữ liệu của sinh viên vào ô nhập liệu
#                 entry.insert(0, str(student_data[field]))

#                 # Lưu ô nhập liệu vào dictionary với tên trường làm khóa
#                 entries[field] = entry

#             # Tạo nút Xác nhận để lưu thông tin cập nhật
#             confirm_button = Button(form_frame, text="Xác nhận", command=lambda: confirm_update(student_id, entries))
#             confirm_button.grid(row=len(fields) + 2, column=0, columnspan=2, pady=20)

#             # Cập nhật lại vùng cuộn của canvas để chứa form mới
#             form_frame.update_idletasks()
#             canvas.config(scrollregion=canvas.bbox("all"))
#             return True


#     def confirm_update(student_id, entries):
#         """Xác nhận cập nhật thông tin sinh viên."""
#         new_info = [entry.get() for entry in entries.values()]  # Lấy dữ liệu mới từ các ô nhập liệu

#         # Cập nhật thông tin sinh viên trong file CSV
#         if update_data(student_id, new_info):
#             messagebox.showinfo("Cập nhật thành công", "Thông tin sinh viên đã được cập nhật.")
#         else:
#             messagebox.showerror("Lỗi", "Không tìm thấy sinh viên để cập nhật.")

# def delete():
#     """Mở cửa sổ xóa sinh viên."""
#     delete_window = Tk()
#     delete_window.title("Xóa Sinh Viên")
#     delete_window.geometry("550x550+300+200")

#     # Tạo Canvas để cuộn
#     canvas = Canvas(delete_window)
#     canvas.pack(side=LEFT, fill=BOTH, expand=True)

#     # Thanh cuộn dọc
#     scrollbar = Scrollbar(delete_window, orient=VERTICAL, command=canvas.yview)
#     scrollbar.pack(side=RIGHT, fill=Y)
#     canvas.configure(yscrollcommand=scrollbar.set)

#     # Tạo Frame chứa các ô nhập liệu
#     form_frame = Frame(canvas)
#     canvas.create_window((0, 0), window=form_frame, anchor="nw")

#     # Nhập ID sinh viên
#     Label(form_frame, text="Nhập ID sinh viên cần xóa:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
#     student_id_entry = Entry(form_frame)
#     student_id_entry.grid(row=0, column=1, padx=10, pady=5)

#     # Nút Tìm Kiếm
#     search_button = Button(form_frame, text="Tìm kiếm", command=lambda: search_student(student_id_entry.get(), form_frame, canvas, delete_window))
#     search_button.grid(row=1, column=0, columnspan=2, pady=10)

#     def search_student(student_id, form_frame, canvas, window):
#         """Tìm kiếm thông tin sinh viên theo ID."""
#         df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file data_clean.csv

#         # Kiểm tra nếu ID có trong DataFrame
#         if student_id not in df['id'].astype(str).values:
#             messagebox.showerror("Lỗi", f"Không thấy sinh viên với ID: {student_id}.")
#             return False
#         else:
#             # Lấy dữ liệu sinh viên tương ứng
#             student_data = df[df['id'].astype(str) == student_id].iloc[0]

#             fields = student_data.index.tolist()  # Danh sách các trường
#             print(fields)
#             for i, field in enumerate(fields, start=2):
#                 Label(form_frame, text=f"{field}:").grid(row=i, column=0, padx=10, pady=5, sticky="w")
#                 Label(form_frame, text=str(student_data[field])).grid(row=i, column=1, padx=10, pady=5)

#             # Nút Xác nhận xóa
#             delete_button = Button(form_frame, text="Delete", command=lambda: confirm_delete(student_id, window))
#             delete_button.grid(row=len(fields) + 2, column=0, columnspan=2, pady=20)

#             # Cập nhật lại canvas
#             form_frame.update_idletasks()
#             canvas.config(scrollregion=canvas.bbox("all"))
#             return True

#     def confirm_delete(student_id, window):
#         """Xác nhận việc xóa sinh viên."""
#         df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file CSV
#         original_length = len(df)  # Lưu độ dài ban đầu của DataFrame
#         df_updated = delete_data(df, student_id)  # Gọi hàm xóa và lưu kết quả vào biến mới

#         # Kiểm tra nếu DataFrame đã thay đổi
#         if len(df_updated) < original_length:
#             df_updated.to_csv("data/data_clean.csv", sep=',', index=False)  # Ghi lại dữ liệu đã xóa vào file CSV
#             messagebox.showinfo("Thông báo", f"Đã xóa sinh viên với ID: {student_id}.")
#         else:
#             messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên với ID: {student_id}.")

#         window.destroy()  # Đóng cửa sổ


# if __name__ == "__main__":
#     open_manage_page()


# import os
# import sys
# from tkinter import *
# from tkinter import messagebox, ttk
# from PIL import Image, ImageTk
# import subprocess
# import pandas as pd

# # Thêm thư mục gốc của dự án vào sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from modules.data_crud import read_data, create_data, update_data, delete_data  # Cập nhật đường dẫn import nếu cần


# class StudentManagementApp:
#     def __init__(self):
#         self.manage_root = Tk()
#         self.manage_root.title("Quản lý sinh viên")
#         self.manage_root.geometry("1000x550+300+200")
#         self.manage_root.configure(background="white")

#         self.setup_ui()

#     def setup_ui(self):
#         """Thiết lập giao diện cho ứng dụng."""
#         self.add_title()
#         self.add_back_button()
#         self.add_menu()
#         self.add_background()
#         self.manage_root.mainloop()

#     def add_title(self):
#         """Thêm tiêu đề và logo."""
#         logo_path = os.path.join("images", "logo.png")
#         logo_image = Image.open(logo_path).resize((20, 20))
#         self.logo_dash = ImageTk.PhotoImage(logo_image)

#         title = Label(self.manage_root, text="Students Management", image=self.logo_dash, padx=10,
#                       compound=LEFT, bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
#         title.place(x=0, y=0, relwidth=1, height=80)

#     def add_back_button(self):
#         """Thêm nút Quay lại."""
#         back_button = Button(self.manage_root, text="Back", border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
#                              command=self.return_to_home)
#         back_button.place(x=20, y=100, width=90, height=30)

#     def add_menu(self):
#         """Thêm menu quản lý chức năng."""
#         M_Frame = LabelFrame(self.manage_root, text="Menu", bg="white", font=("Arial", 12, "bold"))
#         M_Frame.place(x=0, y=150, width=200, relheight=1)

#         self.create_menu_button(M_Frame, "Create", self.create, 0)
#         self.create_menu_button(M_Frame, "Read", self.read, 70)
#         self.create_menu_button(M_Frame, "Update", self.update, 140)
#         self.create_menu_button(M_Frame, "Delete", self.delete, 210)

#     def add_background(self):
#         """Thêm nền trang quản lý."""
#         bg_manage = Image.open("images/bg_manage.png").resize((1150, 700))
#         bg_manage = ImageTk.PhotoImage(bg_manage)
#         background_label = Label(self.manage_root, image=bg_manage)
#         background_label.place(x=200, y=80, relwidth=1, relheight=1)

#     def create_menu_button(self, parent, text, command, y_position):
#         """Hàm để tạo nút trong khung menu."""
#         button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
#         button.place(x=0, y=y_position, width=200, height=50)
#         button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
#         button.bind("<Leave>", lambda e: button.config(bg="#242533"))

#     def return_to_home(self):
#         """Hàm để quay lại trang chính."""
#         self.manage_root.destroy()
#         subprocess.run(["python", "gui/home_page.py"])

#     def create(self):
#         CreateStudentWindow()

#     def read(self):
#         ReadStudentWindow()

#     def update(self):
#         UpdateStudentWindow()

#     def delete(self):
#         # Hàm xóa có thể được triển khai tương tự như các chức năng khác.
#         pass


# class CreateStudentWindow:
#     def __init__(self):
#         self.create_window = Toplevel()
#         self.create_window.title("Thêm sinh viên mới")
#         self.create_window.geometry("700x550+300+200")
#         self.entries = {}
#         self.fields = [
#             ("ID", "e.g., 0, 1, 2..."),
#             ("Name", "e.g., Kiana Lor"),
#             ("Nationality", "e.g., United States of America"),
#             ("City", "e.g., Oakland"),
#             ("Latitude (vĩ dộ)", "e.g., 37.8"),
#             ("Longitude (kinh độ)", "e.g., -122.27"),
#             ("Gender", "e.g., M/F"),
#             ("Ethnic Group", "e.g., NA"),
#             ("Age", "e.g., 22"),
#             ("English Grade", "e.g., 3.5"),
#             ("Math Grade", "e.g., 3.7"),
#             ("Sciences Grade", "e.g., 3.2"),
#             ("Language Grade", "e.g., 5"),
#             ("Portfolio Rating", "e.g., 4"),
#             ("Cover Letter Rating", "e.g., 5"),
#             ("Reference Letter Rating", "e.g., 4")
#         ]
#         self.setup_ui()

#     def setup_ui(self):
#         self.create_form()
#         self.add_buttons()

#     def create_form(self):
#         """Tạo form nhập liệu cho sinh viên."""
#         for i, (label_text, placeholder) in enumerate(self.fields):
#             col = i % 2
#             row = i // 2
#             Label(self.create_window, text=label_text).grid(row=row, column=col * 2, padx=10, pady=5, sticky="w")
#             var = StringVar(value=placeholder)
#             entry = Entry(self.create_window, textvariable=var, fg="grey")
#             entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5)
#             self.entries[label_text] = entry

#             entry.bind("<FocusIn>", lambda e, var=var, placeholder=placeholder: self.clear_placeholder(e, var, placeholder))
#             entry.bind("<FocusOut>", lambda e, var=var, placeholder=placeholder: self.restore_placeholder(e, var, placeholder))

#     def add_buttons(self):
#         """Thêm nút để xác nhận và thêm dữ liệu mẫu."""
#         add_button = Button(self.create_window, text="Thêm Dữ Liệu Mẫu", command=self.add_sample_data)
#         add_button.grid(row=len(self.fields) // 2 + 1, column=1, padx=10, pady=10)

#         confirm_button = Button(self.create_window, text="Xác nhận", command=self.confirm)
#         confirm_button.grid(row=len(self.fields) // 2 + 1, column=2, padx=10, pady=10)

#     def add_sample_data(self):
#         """Thêm dữ liệu mẫu vào file CSV."""
#         sample_data = [
#             [1, "Chuong Pham", "Vietnam", "Quang Ngai", 10.8231, 106.6297, "Male", "Kinh", 19, 8.5, 9.0, 8.0, 7.5, 4.5, 4.0, 5.0],
#             [2, "Minh Nguyen", "Vietnam", "Dong Nai", 21.0285, 105.8542, "Female", "Kinh", 19, 9.0, 8.5, 9.5, 8.0, 4.0, 4.5, 5.5],
#             [3, "Thuy Nguyen", "Vietnam", "Dong Nai", 16.0583, 108.2215, "Female", "Kinh", 19, 7.0, 8.0, 6.5, 8.5, 3.5, 3.0, 4.0]
#         ]
#         file_path = 'data/data_clean.csv'
#         for data in sample_data:
#             create_data(data, file_path)
#         messagebox.showinfo("Thành công", "Dữ liệu mẫu đã được thêm vào file CSV!")

#     def confirm(self):
#         """Xác nhận và lưu thông tin sinh viên."""
#         student_data = [self.entries[label_text].get() for label_text, _ in self.fields]
#         for i, (field, placeholder) in enumerate(self.fields):
#             if student_data[i] == placeholder or student_data[i] == "":
#                 messagebox.showwarning("Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
#                 return
#         create_data(student_data, "data/data_clean.csv")
#         self.create_window.destroy()

#     def clear_placeholder(self, e, var, placeholder):
#         if var.get() == placeholder:
#             var.set("")
#             e.widget.config(fg="black")

#     def restore_placeholder(self, e, var, placeholder):
#         if var.get() == "":
#             var.set(placeholder)
#             e.widget.config(fg="grey")


# class ReadStudentWindow:
#     def __init__(self):
#         self.display_window = Toplevel()
#         self.display_window.title("Dữ liệu sinh viên")
#         self.display_window.geometry("700x550+300+200")
#         self.setup_ui()

#     def setup_ui(self):
#         try:
#             data = read_data()
#             if data is None:
#                 messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị!")
#                 self.display_window.destroy()
#                 return

#             columns = data.columns.tolist()
#             tree = ttk.Treeview(self.display_window, columns=columns, show="headings")

#             for col in columns:
#                 tree.heading(col, text=col)
#                 tree.column(col, width=100)

#             for _, row in data.iterrows():
#                 tree.insert("", "end", values=row.tolist())

#             tree.pack(fill="both", expand=True)

#         except FileNotFoundError:
#             messagebox.showerror("Lỗi", "Không tìm thấy file dữ liệu.")
# class UpdateStudentWindow:
#     def __init__(self):
#         self.update_window = Toplevel()
#         self.update_window.title("Cập nhật sinh viên")
#         self.update_window.geometry("700x550+300+200")
#         self.entries = {}
#         self.fields = [
#             ("ID", "Nhập ID sinh viên cần cập nhật"),
#             ("Name", "Tên mới"),
#             ("Nationality", "Quốc gia mới"),
#             ("City", "Thành phố mới"),
#             ("Latitude (vĩ dộ)", "Vĩ độ mới"),
#             ("Longitude (kinh độ)", "Kinh độ mới"),
#             ("Gender", "Giới tính mới"),
#             ("Ethnic Group", "Dân tộc mới"),
#             ("Age", "Tuổi mới"),
#             ("English Grade", "Điểm tiếng Anh mới"),
#             ("Math Grade", "Điểm Toán mới"),
#             ("Sciences Grade", "Điểm Khoa học mới"),
#             ("Language Grade", "Điểm Ngôn ngữ mới"),
#             ("Portfolio Rating", "Xếp hạng Portfolio mới"),
#             ("Cover Letter Rating", "Xếp hạng thư xin việc mới"),
#             ("Reference Letter Rating", "Xếp hạng thư giới thiệu mới")
#         ]
#         self.setup_ui()

#     def setup_ui(self):
#         self.create_form()
#         self.add_buttons()

#     def create_form(self):
#         """Tạo form nhập liệu để cập nhật sinh viên."""
#         for i, (label_text, placeholder) in enumerate(self.fields):
#             col = i % 2
#             row = i // 2
#             Label(self.update_window, text=label_text).grid(row=row, column=col * 2, padx=10, pady=5, sticky="w")
#             var = StringVar(value=placeholder)
#             entry = Entry(self.update_window, textvariable=var, fg="grey")
#             entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5)
#             self.entries[label_text] = entry

#             entry.bind("<FocusIn>", lambda e, var=var, placeholder=placeholder: self.clear_placeholder(e, var, placeholder))
#             entry.bind("<FocusOut>", lambda e, var=var, placeholder=placeholder: self.restore_placeholder(e, var, placeholder))

#     def add_buttons(self):
#         """Thêm nút để xác nhận cập nhật."""
#         update_button = Button(self.update_window, text="Xác nhận cập nhật", command=self.confirm_update)
#         update_button.grid(row=len(self.fields) // 2 + 1, column=1, padx=10, pady=10)

#     def confirm_update(self):
#         """Xác nhận và lưu thông tin cập nhật của sinh viên."""
#         student_data = [self.entries[label_text].get() for label_text, _ in self.fields]
#         student_id = student_data[0]
#         if student_id == self.fields[0][1] or student_id == "":
#             messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID sinh viên cần cập nhật.")
#             return
#         update_data(student_data, "data/data_clean.csv")  # Giả định `update_data` có thể cập nhật dựa trên ID
#         self.update_window.destroy()

#     def clear_placeholder(self, e, var, placeholder):
#         if var.get() == placeholder:
#             var.set("")
#             e.widget.config(fg="black")

#     def restore_placeholder(self, e, var, placeholder):
#         if var.get() == "":
#             var.set(placeholder)
#             e.widget.config(fg="grey")


# class DeleteStudentWindow:
#     def __init__(self):
#         self.delete_window = Toplevel()
#         self.delete_window.title("Xóa sinh viên")
#         self.delete_window.geometry("400x200+300+200")
#         self.setup_ui()

#     def setup_ui(self):
#         """Tạo giao diện để nhập ID sinh viên cần xóa."""
#         Label(self.delete_window, text="Nhập ID sinh viên cần xóa:").pack(pady=10)
#         self.id_entry = Entry(self.delete_window)
#         self.id_entry.pack(pady=5)
#         delete_button = Button(self.delete_window, text="Xóa", command=self.confirm_delete)
#         delete_button.pack(pady=10)

#     def confirm_delete(self):
#         """Xác nhận xóa sinh viên dựa trên ID."""
#         student_id = self.id_entry.get()
#         if not student_id:
#             messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID sinh viên cần xóa.")
#             return
#         delete_data(student_id, "data/data_clean.csv")  # Giả định `delete_data` có thể xóa dựa trên ID
#         messagebox.showinfo("Thành công", f"Đã xóa sinh viên có ID {student_id}")
#         self.delete_window.destroy()


# if __name__ == "__main__":
#     root = Tk()
#     app = StudentManagementApp(root)
#     root.mainloop()


# Cập nhật đường dẫn import nếu cần
import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import csv
from tkinter import Toplevel
from tkinter import ttk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data, create_data, update_data, delete_data


class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")

        # === ICON ===
        logo_path = os.path.join("images", "logo.png")
        logo_image = Image.open(logo_path).resize((20, 20))
        logo_dash = ImageTk.PhotoImage(logo_image)

        # === TITLE ===
        title = Label(self.root, text="Students Management", image=logo_dash, padx=10, compound=LEFT,
                      bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
        title.place(x=0, y=0, relwidth=1, height=80)

        # === NÚT QUAY LẠI ===
        back_button = Button(self.root, text="Quay lại", bg="#242533", fg="white", font=("Arial", 12, "bold"),
                             command=self.return_to_home)
        back_button.place(x=20, y=100, width=90, height=30)

        # === MENU ===
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=150, width=200, relheight=1)

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Create", self.create, 0)
        self.create_menu_button(M_Frame, "Read", self.read, 70)
        self.create_menu_button(M_Frame, "Update", self.update, 140)
        self.create_menu_button(M_Frame, "Delete", self.delete, 210)

        # === BACKGROUND ===
        bg_manage = Image.open("images/bg_manage.png")
        bg_manage = bg_manage.resize((1150, 700), Image.LANCZOS)
        bg_manage = ImageTk.PhotoImage(bg_manage)
        background_label = Label(self.root, image=bg_manage)
        background_label.place(x=200, y=80, relwidth=1, relheight=1)

    def return_to_home(self):
        """Hàm để quay lại trang chính."""
        self.root.destroy()
        subprocess.run(["python", "home_page.py"])

    def create_menu_button(self, parent, text, command, y_position):
        """Hàm để tạo nút trong khung menu."""
        button = Button(parent, text=text, bg="#242533", fg="white",
                        font=("Arial", 12, "bold"), command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))
        return button

    def read(self):
        """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra một cửa sổ mới dưới dạng bảng."""
        try:
            file_path = "data/student-dataset.csv"  # Đường dẫn đến file CSV
            # Gọi hàm read_data để lấy dữ liệu từ file CSV
            data = read_data(file_path)

            if not data:
                messagebox.showinfo(
                    "Thông báo", "Không có dữ liệu để hiển thị.")
                return

            # Tạo một cửa sổ mới để hiển thị bảng dữ liệu
            display_window = Toplevel()
            display_window.title("Dữ liệu sinh viên")
            display_window.geometry("800x400")

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
                # Đặt độ rộng cột 150, có thể điều chỉnh nếu cần
                tree.column(col, anchor='center', width=150)

            # Thêm dữ liệu vào bảng
            for row in data[1:]:
                tree.insert("", "end", values=row)

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

    # Placeholder functions for menu actions
    def create(self):
        """Hàm cho chức năng Create - Tạo bảng nhập dữ liệu sinh viên với các gợi ý cho từng trường."""
        create_window = Toplevel()
        create_window.title("Thêm sinh viên mới")
        create_window.geometry("700x550+300+200")

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

        # Chia số trường thành hai cột
        for i, (label_text, placeholder) in enumerate(fields):
            col = i % 2  # Xác định cột (0 hoặc 1)
            row = i // 2  # Xác định hàng
            Label(create_window, text=label_text).grid(
                row=row, column=col * 2, padx=10, pady=5, sticky="w")

            var = StringVar(value=placeholder)
            entry = Entry(create_window, textvariable=var, fg="grey")
            entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5)
            entries[label_text] = entry

            def clear_placeholder(e, var=var, placeholder=placeholder):
                if var.get() == placeholder:
                    var.set("")
                    entry.config(fg="black")

            def restore_placeholder(e, var=var, placeholder=placeholder):
                if var.get() == "":
                    var.set(placeholder)
                    entry.config(fg="grey")

            # Khi người dùng nhấn vào ô nhập liệu, nếu placeholder hiện thị thì xóa nó
            entry.bind("<FocusIn>", clear_placeholder)
            # Khi người dùng rời khỏi ô nhập liệu, nếu ô nhập liệu trống thì hiển thị placeholder
            entry.bind("<FocusOut>", restore_placeholder)

        def add_sample_data():
            """Thêm dữ liệu mẫu vào file CSV khi nút được nhấn."""
            sample_data = [
                [1, "Chuong Pham", "Vietnam", "Quang Ngai", 10.8231, 106.6297, "Male", "Kinh", 19, 8.5, 9.0,
                 8.0, 7.5, 4.5, 4.0, 5.0],
                [2, "Minh Nguyen", "Vietnam", "Dong Nai", 21.0285, 105.8542, "Female", "Kinh", 19, 9.0, 8.5,
                 9.5, 8.0, 4.0, 4.5, 5.5],
                [3, "Thuy Nguyen", "Vietnam", "Dong Nai", 16.0583, 108.2215, "Female", "Kinh", 19, 7.0, 8.0,
                 6.5, 8.5, 3.5, 3.0, 4.0]
            ]

            file_path = 'data/data_clean.csv'  # Đường dẫn đến file CSV
            for data in sample_data:
                create_data(data, file_path)

            messagebox.showinfo(
                "Thành công", "Dữ liệu mẫu đã được thêm vào file CSV!")

        # Tạo nút để thêm dữ liệu mẫu
        add_button = Button(
            create_window, text="Thêm Dữ Liệu Mẫu", command=add_sample_data)
        add_button.grid(row=len(fields) // 2 + 1, column=1, padx=10, pady=10)

        def confirm():
            student_data = [entries[label_text].get()
                            for label_text, _ in fields]

            for i, (field, placeholder) in enumerate(fields):
                if student_data[i] == placeholder or student_data[i] == "":
                    messagebox.showwarning(
                        "Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
                    return

            create_data(student_data, "data/data_clean.csv")
            create_window.destroy()

        confirm_button = Button(
            create_window, text="Xác nhận", command=confirm)
        confirm_button.grid(row=len(fields) // 2 + 1,
                            column=2, padx=10, pady=10)

    def update(self):
        """Hàm cho chức năng Update - Cập nhật thông tin sinh viên."""
        update_window = Toplevel()
        update_window.title("Cập nhật thông tin sinh viên")
        update_window.geometry("700x550+300+200")

        # Tạo Canvas để cuộn
        canvas = Canvas(update_window)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Thanh cuộn dọc
        scrollbar = Scrollbar(
            update_window, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Tạo Frame chứa các ô nhập liệu
        form_frame = Frame(canvas)
        canvas.create_window((0, 0), window=form_frame, anchor="nw")

        # Nhập ID sinh viên
        Label(form_frame, text="Nhập ID sinh viên để tìm kiếm:").grid(
            row=0, column=0, padx=10, pady=5, sticky="w")
        student_id_entry = Entry(form_frame)
        student_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Nút Tìm Kiếm
        search_button = Button(form_frame, text="Tìm kiếm", command=lambda: self.search_student(
            student_id_entry.get(), form_frame, canvas))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

        def search_student(self, student_id, form_frame, canvas):
            """Tìm sinh viên theo ID và điền thông tin hiện tại nếu tìm thấy."""
            df = pd.read_csv(
                "data/data_clean.csv")  # Đọc dữ liệu từ file data_clean.csv

            # Kiểm tra nếu ID có trong DataFrame
            if student_id not in df['ID'].astype(str).values:
                messagebox.showerror(
                    "Lỗi", f"Không thấy sinh viên với ID: {student_id}.")
                return False
            else:
                # Lấy dữ liệu sinh viên tương ứng
                student_data = df[df['ID'].astype(str) == student_id].iloc[0]

                # Hiển thị các ô nhập liệu và điền thông tin
                # Lấy danh sách các trường dữ liệu của sinh viên
                fields = student_data.index.tolist()
                entries = {}  # Dictionary lưu trữ các ô nhập liệu cho từng trường
                for i, field in enumerate(fields, start=2):
                    # Tạo nhãn (label) cho từng trường dữ liệu
                    Label(form_frame, text=f"{field}:").grid(
                        row=i, column=0, padx=10, pady=5, sticky="w")

                    # Tạo ô nhập liệu (entry) cho từng trường
                    entry = Entry(form_frame)
                    entry.grid(row=i, column=1, padx=10, pady=5)

                    # Điền dữ liệu của sinh viên vào ô nhập liệu
                    entry.insert(0, str(student_data[field]))

                    # Lưu ô nhập liệu vào dictionary với tên trường làm khóa
                    entries[field] = entry

                # Tạo nút Xác nhận để lưu thông tin cập nhật
                confirm_button = Button(
                    form_frame, text="Xác nhận", command=lambda: self.confirm_update(student_id, entries))
                confirm_button.grid(row=len(fields) + 2,
                                    column=0, columnspan=2, pady=20)

                # Cập nhật lại vùng cuộn của canvas để chứa form mới
                form_frame.update_idletasks()
                canvas.config(scrollregion=canvas.bbox("all"))
                return True

        def confirm_update(self, student_id, entries):
            """Xác nhận cập nhật thông tin sinh viên."""
            new_info = [entry.get() for entry in entries.values()
                        ]  # Lấy dữ liệu mới từ các ô nhập liệu

            # Cập nhật thông tin sinh viên trong file CSV
            if update_data(student_id, new_info):
                messagebox.showinfo("Cập nhật thành công",
                                    "Thông tin sinh viên đã được cập nhật.")
            else:
                messagebox.showerror(
                    "Lỗi", "Không tìm thấy sinh viên để cập nhật.")

    def delete(self):
        """Hàm cho chức năng Delete - Xóa sinh viên."""
        delete_window = Toplevel()
        delete_window.title("Xóa sinh viên")
        delete_window.geometry("400x200+300+200")

        Label(delete_window, text="Nhập ID sinh viên cần xóa:").pack(pady=10)
        student_id_entry = Entry(delete_window)
        student_id_entry.pack(pady=5)

        def confirm_delete():
            student_id = student_id_entry.get()
            if not student_id:
                messagebox.showwarning(
                    "Cảnh báo", "Vui lòng nhập ID sinh viên cần xóa.")
                return

            df = pd.read_csv("data/data_clean.csv")
            if student_id not in df['ID'].astype(str).values:
                messagebox.showerror(
                    "Lỗi", f"Không thấy sinh viên với ID: {student_id}.")
                return

            df = df[df['ID'].astype(str) != student_id]
            df.to_csv("data/data_clean.csv", index=False)
            messagebox.showinfo(
                "Thành công", f"Đã xóa sinh viên có ID {student_id}")
            delete_window.destroy()

        delete_button = Button(
            delete_window, text="Xóa", command=confirm_delete)
        delete_button.pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    app = StudentManagementApp(root)
    root.mainloop()

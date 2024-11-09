# import os
# from tkinter import *
# from tkinter import messagebox, ttk
# from PIL import Image, ImageTk
# import sys
# import pandas as pd

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt


# # Thêm thư mục gốc của dự án vào sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from modules.data_crud import read_data, create_data, update_data, delete_data  
# from modules.data_visualization import plot_grade, plot_age, plot_country
# from modules.data_cleaning import handle_missing_value, remove_duplicates, correct_formatting, save_to_cleaned_data_file

# class ViewPage:
#     def __init__(self, root):
#         self.root = root
#         self.setup_window()
#         self.create_logo()
#         self.create_menu()
#         self.create_content_frame()  
#         root.resizable(False, False)

#     def setup_window(self):
#         """Thiết lập cửa sổ chính."""
#         self.root.title("Hệ thống quản lý sinh viên")
#         self.root.geometry("1000x550+300+200")
#         self.root.configure(background="white")

#     def create_logo(self):
#         """Tạo logo cho ứng dụng."""
#         logo_path = os.path.join("images", "logo.png")
#         logo_image = Image.open(logo_path).resize((20, 20))
#         self.logo_dash = ImageTk.PhotoImage(logo_image)

#         Label(self.root, text="Student Management Mini", image=self.logo_dash, padx=10, compound=LEFT,
#               bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

#     def create_menu(self):
#         """Tạo menu cho ứng dụng."""
#         M_Frame = LabelFrame(self.root, text="Menu",
#                              bg="white", font=("Arial", 12, "bold"))
#         M_Frame.place(x=0, y=80, width=200, relheight=1)

#         # Thêm các nút vào khung menu
#         self.create_menu_button(M_Frame, "Plot Age", self.plot_age, 0)
#         self.create_menu_button(M_Frame, "Plot Country", self.plot_country, 75)
#         self.create_menu_button(M_Frame, "Plot Grade", self.plot_grade, 150)
#         self.create_menu_button(M_Frame, "Cleaning", self.cleaning, 220)
#         self.create_menu_button(M_Frame, "Read", self.read, 290)
#         self.create_menu_button(M_Frame, "Exit", self.exit_program, 360)

#     def create_content_frame(self):
#         """Tạo vùng hiển thị nội dung."""
#         self.content_frame = Frame(self.root, bg="lightgrey")
#         # self.content_frame.place(x=200, y=80, width=800, height=470)
#         self.content_frame.place(x=200, y=80, relwidth=0.87, relheight=0.9)


#     def create_menu_button(self, parent, text, command, y_position):
#         """Tạo nút menu."""
#         button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
#                         command=command)
#         button.place(x=0, y=y_position, width=200, height=50)
#         button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
#         button.bind("<Leave>", lambda e: button.config(bg="#242533"))

#     def clear_content_frame(self):
#         """Xóa nội dung trong khung hiển thị nội dung."""
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#     def read(self):
#         """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra bảng trong cửa sổ hiện tại."""
#         self.clear_content_frame()  # Xóa nội dung cũ trong khung hiển thị nội dung

#         try:
#             file_path = "data/student-dataset.csv"  # Đường dẫn đến file CSV
#             data = read_data(file_path)  # Lấy dữ liệu từ file CSV

#             if not data:
#                 messagebox.showinfo(
#                     "Thông báo", "Không có dữ liệu để hiển thị.")
#                 return

#             # Tạo thanh cuộn dọc và ngang cho Treeview
#             v_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical")
#             h_scrollbar = ttk.Scrollbar(
#                 self.content_frame, orient="horizontal")

#             # Tạo Treeview để hiển thị bảng dữ liệu
#             columns = data[0]  # Lấy hàng đầu tiên làm tên cột
#             tree = ttk.Treeview(self.content_frame, columns=columns, show="headings",
#                                 yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

#             # Đặt tiêu đề cho mỗi cột và tùy chỉnh độ rộng
#             for col in columns:
#                 tree.heading(col, text=col)
#                 tree.column(col, anchor='center', width=150) # Độ rộng cố định

#             # Thêm dữ liệu vào bảng
#             for row in data[1:]:
#                 tree.insert("", "end", values=row)

#             # Đặt Treeview và thanh cuộn vào content_frame
#             tree.grid(row=0, column=0, sticky="nsew")
#             v_scrollbar.grid(row=0, column=1, sticky="ns") # Cần thêm cột này để thanh cuộn dọc hoạt động
#             h_scrollbar.grid(row=1, column=0, sticky="ew") # Cần thêm hàng này để thanh cuộn ngang hoạt động

#             # Kết nối thanh cuộn với Treeview
#             v_scrollbar.config(command=tree.yview)  # Cuộn dọc
#             h_scrollbar.config(command=tree.xview)  # Cuộn ngang

#             # Thiết lập tỷ lệ mở rộng cho Treeview
#             self.content_frame.grid_rowconfigure(0, weight=1) # Cột 0
#             self.content_frame.grid_columnconfigure(0, weight=1) # Hàng 0

#         except FileNotFoundError:
#             messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
#         except Exception as e:
#             messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

#     def plot_age(self):
#         """Hàm trực quan độ tuổi"""
#         self.clear_content_frame()
#         file_path = "data/student-dataset.csv"
#         plot_age(file_path)

#     def plot_country(self):
#         """Hàm trực quan quốc gia."""
#         self.clear_content_frame()
#         file_path = "data/student-dataset.csv"
#         plot_country(file_path)
       

#     def plot_grade(self):
#         """Hàm trực quan điểm học tập."""
#         self.clear_content_frame()
#         file_path = "data/student-dataset.csv"
#         plot_grade(file_path)

#     def cleaning(self):    
#         """Hàm làm sạch dữ liệu."""
#         self.clear_content_frame()
#         file_path = "data/student-dataset.csv"
#         data = pd.read_csv(file_path)
#         # Xử lí dữ liệu
#         data = handle_missing_value(data)

#         # Loại bỏ trùng
#         data = remove_duplicates(data)

#         # Sửa định dạng
#         data = correct_formatting(data)

#         # Lưu dữ liệu
#         cleaned_file_path = "data/data_clean.csv"
#         save_to_cleaned_data_file(cleaned_file_path, data)

#         # Thông báo
#         messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch và lưu vào file data_clean.csv.")

#     def exit_program(self):
#         """Hàm cho chức năng Exit - Thoát chương trình."""
#         self.root.destroy()

# def main():
#     root = Tk()
#     app = ViewPage(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()


import os
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sys
import pandas as pd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.data_crud import read_data, create_data, update_data, delete_data  
from modules.data_visualization import plot_grade_data, plot_age_data, plot_country_data
from modules.data_cleaning import handle_missing_value, remove_duplicates, correct_formatting, save_to_cleaned_data_file

class ViewPage:
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
        self.create_menu_button(M_Frame, "Plot Age", self.plot_age, 0)
        self.create_menu_button(M_Frame, "Plot Country", self.plot_country, 75)
        self.create_menu_button(M_Frame, "Plot Grade", self.plot_grade, 150)
        self.create_menu_button(M_Frame, "Cleaning", self.cleaning, 220)
        self.create_menu_button(M_Frame, "Read", self.read, 290)
        self.create_menu_button(M_Frame, "Exit", self.exit_program, 360)

    def create_content_frame(self):
        """Tạo vùng hiển thị nội dung."""
        self.content_frame = Frame(self.root, bg="lightgrey")
        self.content_frame.place(x=200, y=80, relwidth=0.87, relheight=0.9)

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

    def plot_age(self):
        """Hàm trực quan độ tuổi"""
        self.clear_content_frame()
        fig = plot_age_data("data/student-dataset.csv")  # Hàm này trả về một Figure từ matplotlib
        self.display_plot(fig)

    def plot_country(self):
        """Hàm trực quan quốc gia."""
        self.clear_content_frame()
        fig = plot_country_data("data/student-dataset.csv")  # Hàm này trả về một Figure từ matplotlib
        self.display_plot(fig)

    def plot_grade(self):
        """Hàm trực quan điểm học tập."""
        self.clear_content_frame()
        fig = plot_grade_data("data/student-dataset.csv")  # Hàm này trả về một Figure từ matplotlib
        self.display_plot(fig)

    def display_plot(self, fig):
        """Hiển thị biểu đồ trên content_frame."""
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)

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
        messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch và lưu vào file data_clean.csv.")

    def exit_program(self):
        """Hàm cho chức năng Exit - Thoát chương trình."""
        self.root.destroy()

def main():
    root = Tk()
    app = ViewPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()

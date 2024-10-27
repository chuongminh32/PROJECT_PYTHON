import os
import sys
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import csv
from tkinter import Toplevel
from tkinter import ttk
import pandas as pd
from tkinter import Tk, Frame, Label, Entry, Button, Canvas, Scrollbar, messagebox, LEFT, RIGHT, VERTICAL, BOTH, Y



# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data, create_data, update_data, delete_data  # Cập nhật đường dẫn import nếu cần

def open_manage_page():
    """Hàm để mở trang quản lý sinh viên."""
    manage_root = Tk()
    manage_root.title("Quản lý sinh viên")
    manage_root.geometry("1350x700")
    manage_root.configure(background="white")

    # === ICON === 
    logo_path = os.path.join("images", "logo2.png")
    if not os.path.exists(logo_path):
        messagebox.showerror("Error", f"File not found: {logo_path}")
        return
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((40, 40), Image.LANCZOS)
    logo_dash = ImageTk.PhotoImage(logo_image)

    # === TITLE ===
    title = Label(manage_root, text="Students Management", image=logo_dash, padx=10, compound=LEFT,
                  bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
    title.place(x=0, y=0, relwidth=1, height=80)

    # === NÚT QUAY LẠI ===
    back_button = Button(manage_root, text="Quay lại", bg="#242533", fg="white", font=("Arial", 12, "bold"),
                         command=lambda: return_to_home(manage_root))
    back_button.place(x=20, y=100, width=90, height=30)

    # === MENU === 
    M_Frame = LabelFrame(manage_root, text="Menu", bg="white", font=("Arial", 12, "bold"))
    M_Frame.place(x=0, y=150, width=200, relheight=1)

    # Thêm các nút vào khung menu
    create_menu_button(M_Frame, "Create", create, 0)
    create_menu_button(M_Frame, "Read", read, 70)
    create_menu_button(M_Frame, "Update", update, 140)
    create_menu_button(M_Frame, "Delete", delete, 210)

    # === BACKGROUND ===
    bg_manage = Image.open("images/bg_manage.png")
    bg_manage = bg_manage.resize((1150, 700), Image.LANCZOS)
    bg_manage = ImageTk.PhotoImage(bg_manage)
    background_label = Label(manage_root, image=bg_manage)
    background_label.place(x=200, y=80, relwidth=1, relheight=1)

    manage_root.mainloop()

def return_to_home(manage_root):
    """Hàm để quay lại trang chính."""
    manage_root.destroy()
    subprocess.run(["python", "home_page.py"])

def create_menu_button(parent, text, command, y_position):
    """Hàm để tạo nút trong khung menu."""
    button = Button(parent, text=text, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
    button.place(x=0, y=y_position, width=200, height=50)
    button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
    button.bind("<Leave>", lambda e: button.config(bg="#242533"))
    return button

def read():
    """Hàm cho chức năng Read - Hiển thị dữ liệu trong file ra một cửa sổ mới dưới dạng bảng."""
    try:
        data = read_data()  # Gọi hàm để lấy dữ liệu từ file CSV
        if data is None:
            messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
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
            tree.column(col, anchor='center', width=150)  # Đặt độ rộng cột 150, có thể điều chỉnh nếu cần

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

def create():
    """Hàm cho chức năng Create - Tạo bảng nhập dữ liệu sinh viên với các gợi ý cho từng trường."""
    create_window = Toplevel()
    create_window.title("Thêm sinh viên mới")
    create_window.geometry("500x600")
    
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
    
    for i, (label_text, placeholder) in enumerate(fields):
        Label(create_window, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        
        var = StringVar(value=placeholder)
        entry = Entry(create_window, textvariable=var, fg="grey")
        entry.grid(row=i, column=1, padx=10, pady=5)
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

        messagebox.showinfo("Thành công", "Dữ liệu mẫu đã được thêm vào file CSV!")

    # Tạo nút để thêm dữ liệu mẫu
    add_button = Button(create_window, text="Thêm Dữ Liệu Mẫu", command=add_sample_data)
    add_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

    def confirm():
        student_data = [entries[label_text].get() for label_text, _ in fields]

        for i, (field, placeholder) in enumerate(fields):
            if student_data[i] == placeholder or student_data[i] == "":
                messagebox.showwarning("Cảnh báo", f"Vui lòng nhập thông tin cho trường '{field}'.")
                return

        create_data(student_data, "data/data_clean.csv")
        create_window.destroy()

    confirm_button = Button(create_window, text="Xác nhận", command=confirm)
    confirm_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=20)

def update():
    """Mở cửa sổ để nhập thông tin cập nhật sinh viên."""
    update_window = Toplevel()
    update_window.title("Cập nhật thông tin sinh viên")
    update_window.geometry("450x400")

    # Tạo Canvas để cuộn
    canvas = Canvas(update_window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Thanh cuộn dọc
    scrollbar = Scrollbar(update_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Tạo Frame chứa các ô nhập liệu
    form_frame = Frame(canvas)
    canvas.create_window((0, 0), window=form_frame, anchor="nw")

    # Nhập ID sinh viên
    Label(form_frame, text="Nhập ID sinh viên để tìm kiếm:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    student_id_entry = Entry(form_frame)
    student_id_entry.grid(row=0, column=1, padx=10, pady=5)

    # Nút Tìm Kiếm
    search_button = Button(form_frame, text="Tìm kiếm", command=lambda: search_student(student_id_entry.get(), form_frame, canvas))
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def search_student(student_id, form_frame, canvas):
        """Tìm sinh viên theo ID và điền thông tin hiện tại nếu tìm thấy."""
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file data_clean.csv
    
        # Kiểm tra nếu ID có trong DataFrame
        if student_id not in df['id'].astype(str).values:
            messagebox.showerror("Lỗi", f"Không thấy sinh viên với ID: {student_id}.")
            return False
        else:
            # Lấy dữ liệu sinh viên tương ứng, iloc[0] để lấy hàng đầu tiên (có nhiều data id trùng -> ưu tiên lây dòng đầu tiên)
            student_data = df[df['id'].astype(str) == student_id].iloc[0]
    
            # Hiển thị các ô nhập liệu và điền thông tin
            fields = student_data.index.tolist()  # Danh sách các trường
            entries = {}
            for i, field in enumerate(fields, start=2):
                Label(form_frame, text=f"{field}:").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                entry = Entry(form_frame)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entry.insert(0, str(student_data[field]))  # Điền dữ liệu sinh viên
                entries[field] = entry  # Lưu ô nhập liệu vào dictionary
    
            # Nút Xác nhận
            confirm_button = Button(form_frame, text="Xác nhận", command=lambda: confirm_update(student_id, entries))
            confirm_button.grid(row=len(fields) + 2, column=0, columnspan=2, pady=20)
    
            # Cập nhật lại canvas
            form_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
            return True

    def confirm_update(student_id, entries):
        """Xác nhận cập nhật thông tin sinh viên."""
        new_info = [entry.get() for entry in entries.values()]  # Lấy dữ liệu mới từ các ô nhập liệu
    
        # Cập nhật thông tin sinh viên trong file CSV
        if update_data(student_id, new_info):
            messagebox.showinfo("Cập nhật thành công", "Thông tin sinh viên đã được cập nhật.")
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy sinh viên để cập nhật.")



def delete():
    """Mở cửa sổ xóa sinh viên."""
    delete_window = Tk()
    delete_window.title("Xóa Sinh Viên")
    delete_window.geometry("500x400")

    # Tạo Canvas để cuộn
    canvas = Canvas(delete_window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Thanh cuộn dọc
    scrollbar = Scrollbar(delete_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Tạo Frame chứa các ô nhập liệu
    form_frame = Frame(canvas)
    canvas.create_window((0, 0), window=form_frame, anchor="nw")

    # Nhập ID sinh viên
    Label(form_frame, text="Nhập ID sinh viên cần xóa:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    student_id_entry = Entry(form_frame)
    student_id_entry.grid(row=0, column=1, padx=10, pady=5)

    # Nút Tìm Kiếm
    search_button = Button(form_frame, text="Tìm kiếm", command=lambda: search_student(student_id_entry.get(), form_frame, canvas, delete_window))
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def search_student(student_id, form_frame, canvas, window):
        """Tìm kiếm thông tin sinh viên theo ID."""
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file data_clean.csv

        # Kiểm tra nếu ID có trong DataFrame
        if student_id not in df['id'].astype(str).values:
            messagebox.showerror("Lỗi", f"Không thấy sinh viên với ID: {student_id}.")
            return False
        else:
            # Lấy dữ liệu sinh viên tương ứng
            student_data = df[df['id'].astype(str) == student_id].iloc[0]

            fields = student_data.index.tolist()  # Danh sách các trường
            print(fields)
            for i, field in enumerate(fields, start=2):
                Label(form_frame, text=f"{field}:").grid(row=i, column=0, padx=10, pady=5, sticky="w")
                Label(form_frame, text=str(student_data[field])).grid(row=i, column=1, padx=10, pady=5)

            # Nút Xác nhận xóa
            delete_button = Button(form_frame, text="Delete", command=lambda: confirm_delete(student_id, window))
            delete_button.grid(row=len(fields) + 2, column=0, columnspan=2, pady=20)

            # Cập nhật lại canvas
            form_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
            return True

    def confirm_delete(student_id, window):
        """Xác nhận việc xóa sinh viên."""
        df = pd.read_csv("data/data_clean.csv")  # Đọc dữ liệu từ file CSV
        original_length = len(df)  # Lưu độ dài ban đầu của DataFrame
        df_updated = delete_data(df, student_id)  # Gọi hàm xóa và lưu kết quả vào biến mới

        # Kiểm tra nếu DataFrame đã thay đổi
        if len(df_updated) < original_length:  
            df_updated.to_csv("data/data_clean.csv", sep=',', index=False)  # Ghi lại dữ liệu đã xóa vào file CSV
            messagebox.showinfo("Thông báo", f"Đã xóa sinh viên với ID: {student_id}.")
        else:
            messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên với ID: {student_id}.")
            
        window.destroy()  # Đóng cửa sổ



if __name__ == "__main__":
    open_manage_page()




    
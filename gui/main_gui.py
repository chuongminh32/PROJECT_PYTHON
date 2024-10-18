# import tkinter as tk
# from tkinter import messagebox, filedialog
# import pandas as pd
# from modules import data_crud

# # Đường dẫn mặc định đến file CSV
# default_file_path = 'data/dataset.csv'

# # Đọc dữ liệu ban đầu
# df = data_crud.read_data(default_file_path)

# def load_file():
#     """
#     Hàm này mở hộp thoại file để người dùng chọn file CSV từ máy tính.
#     Sau khi chọn file, nó sẽ đọc dữ liệu từ file CSV và hiển thị lên giao diện.
#     Nếu không chọn file, sẽ sử dụng file CSV mặc định.
#     """
#     global df
#     file_path = filedialog.askopenfilename(
#         title="Chọn file CSV",
#         filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
#     )
    
#     if file_path:
#         df = data_crud.read_data(file_path)
#     else:
#         messagebox.showinfo("Thông báo", f"Sử dụng file mặc định: {default_file_path}")
#         df = data_crud.read_data(default_file_path)
    
#     if df is not None:
#         display_table(df)
#     else:
#         messagebox.showerror("Lỗi", "Không thể đọc dữ liệu từ file CSV đã chọn.")

# def display_table(dataframe):
#     """
#     Hiển thị dữ liệu từ DataFrame lên giao diện.

#     Hàm sẽ xóa nội dung hiện tại trong hộp văn bản và hiển thị toàn bộ DataFrame.
#     """
#     text_output.config(state='normal')
#     text_output.delete(1.0, tk.END)
#     text_output.insert(tk.END, dataframe.to_string(index=False))
#     text_output.config(state='disabled')

# def display_student():
#     """
#     Hiển thị thông tin sinh viên dựa trên số báo danh (SBD) được nhập.
#     """
#     sbd = entry_sbd.get()
#     student = df[df['sbd'] == sbd]
#     if not student.empty:
#         student_info = student.to_string(index=False)
#         text_output.config(state='normal')
#         text_output.delete(1.0, tk.END)
#         text_output.insert(tk.END, student_info)
#         text_output.config(state='disabled')
#     else:
#         messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên với SBD {sbd}")

# def add_student():
#     """
#     Thêm sinh viên mới vào DataFrame và lưu vào file CSV.
#     """
#     new_row = {
#         'sbd': entry_sbd.get(),
#         'toan': entry_math.get(),
#         'ngu_van': entry_literature.get(),
#         'ngoai_ngu': entry_foreign_lang.get(),
#     }
#     global df
#     df = data_crud.add_data(df, new_row)
#     data_crud.save_data(df, default_file_path)
#     messagebox.showinfo("Thành công", "Đã thêm sinh viên thành công")
#     display_table(df)

# def update_student():
#     """
#     Cập nhật thông tin sinh viên dựa trên SBD được nhập.
#     """
#     sbd = entry_sbd.get()
#     updated_row = {
#         'sbd': sbd,
#         'toan': entry_math.get(),
#         'ngu_van': entry_literature.get(),
#         'ngoai_ngu': entry_foreign_lang.get(),
#     }
#     global df
#     df = data_crud.update_data(df, sbd, updated_row)
#     data_crud.save_data(df, default_file_path)
#     messagebox.showinfo("Thành công", "Đã cập nhật thông tin sinh viên")
#     display_table(df)

# def delete_student():
#     """
#     Xóa sinh viên dựa trên SBD được nhập.
#     """
#     sbd = entry_sbd.get()
#     global df
#     df = data_crud.delete_data(df, sbd)
#     data_crud.save_data(df, default_file_path)
#     messagebox.showinfo("Thành công", "Đã xóa sinh viên")
#     display_table(df)

# def center_window(root):
#     """
#     Căn giữa cửa sổ Tkinter trên màn hình.
#     """
#     root.update_idletasks()
#     width = root.winfo_width()
#     height = root.winfo_height()
#     x = (root.winfo_screenwidth() // 2) - (width // 2)
#     y = (root.winfo_screenheight() // 2) - (height // 2)
#     root.geometry(f'{width}x{height}+{x}+{y}')

# # Tạo giao diện Tkinter
# root = tk.Tk()
# root.title("Quản lý sinh viên")

# # Căn giữa cửa sổ
# root.update()
# center_window(root)

# # Các trường nhập liệu với khoảng cách padding
# tk.Label(root, text="SBD:").grid(row=0, column=0, padx=10, pady=5)
# entry_sbd = tk.Entry(root)
# entry_sbd.grid(row=0, column=1, padx=10, pady=5)

# tk.Label(root, text="Toán:").grid(row=1, column=0, padx=10, pady=5)
# entry_math = tk.Entry(root)
# entry_math.grid(row=1, column=1, padx=10, pady=5)

# tk.Label(root, text="Ngữ văn:").grid(row=2, column=0, padx=10, pady=5)
# entry_literature = tk.Entry(root)
# entry_literature.grid(row=2, column=1, padx=10, pady=5)

# tk.Label(root, text="Ngoại ngữ:").grid(row=3, column=0, padx=10, pady=5)
# entry_foreign_lang = tk.Entry(root)
# entry_foreign_lang.grid(row=3, column=1, padx=10, pady=5)

# # Nút thêm, sửa, xóa, hiển thị với khoảng cách padding
# btn_add = tk.Button(root, text="Thêm sinh viên", command=add_student)
# btn_add.grid(row=4, column=0, padx=10, pady=5)

# btn_update = tk.Button(root, text="Cập nhật sinh viên", command=update_student)
# btn_update.grid(row=4, column=1, padx=10, pady=5)

# btn_delete = tk.Button(root, text="Xóa sinh viên", command=delete_student)
# btn_delete.grid(row=5, column=0, padx=10, pady=5)

# btn_display = tk.Button(root, text="Hiển thị sinh viên", command=display_student)
# btn_display.grid(row=5, column=1, padx=10, pady=5)

# # Nút để tải file CSV
# btn_load_file = tk.Button(root, text="Tải file CSV", command=load_file)
# btn_load_file.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# # Text box để hiển thị thông tin sinh viên
# text_output = tk.Text(root, height=15, width=70, state='disabled')
# text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# # Hiển thị dữ liệu mặc định khi khởi động
# if df is not None:
#     display_table(df)

# # Căn giữa cửa sổ khi thay đổi kích thước
# root.bind('<Configure>', lambda event: center_window(root))

# # Chạy giao diện chính
# root.mainloop()



import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from modules import data_crud

# Đường dẫn mặc định đến file CSV
default_file_path = 'data/dataset_demo.csv'

# Đọc dữ liệu ban đầu
df = data_crud.read_data(default_file_path)

def load_file():
    """
    Hàm này mở hộp thoại file để người dùng chọn file CSV từ máy tính.
    Sau khi chọn file, nó sẽ đọc dữ liệu từ file CSV và hiển thị lên giao diện.
    Nếu không chọn file, sẽ sử dụng file CSV mặc định.
    """
    global df
    file_path = filedialog.askopenfilename(
        title="Chọn file CSV",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    
    if file_path:
        df = data_crud.read_data(file_path)
    else:
        messagebox.showinfo("Thông báo", f"Sử dụng file mặc định: {default_file_path}")
        df = data_crud.read_data(default_file_path)
    
    if df is not None:
        display_table(df)
    else:
        messagebox.showerror("Lỗi", "Không thể đọc dữ liệu từ file CSV đã chọn.")

def display_table(dataframe):
    """
    Hiển thị dữ liệu từ DataFrame lên giao diện.

    Hàm sẽ xóa nội dung hiện tại trong hộp văn bản và hiển thị toàn bộ DataFrame.
    """
    text_output.config(state='normal')
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, dataframe.to_string(index=False))
    text_output.config(state='disabled')

def display_student():
    """
    Hiển thị thông tin sinh viên dựa trên số báo danh (SBD) được nhập.
    """
    sbd = entry_sbd.get()
    student = df[df['sbd'] == sbd]
    if not student.empty:
        student_info = student.to_string(index=False)
        text_output.config(state='normal')
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, student_info)
        text_output.config(state='disabled')
    else:
        messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên với SBD {sbd}")

def add_student():
    """
    Thêm sinh viên mới vào DataFrame và lưu vào file CSV.
    """
    new_row = {
        'sbd': entry_sbd.get(),
        'toan': entry_math.get(),
        'ngu_van': entry_literature.get(),
        'ngoai_ngu': entry_foreign_lang.get(),
    }
    global df
    df = data_crud.add_data(df, new_row)
    data_crud.save_data(df, default_file_path)
    messagebox.showinfo("Thành công", "Đã thêm sinh viên thành công")
    display_table(df)

def update_student():
    """
    Cập nhật thông tin sinh viên dựa trên SBD được nhập.
    """
    sbd = entry_sbd.get()
    updated_row = {
        'sbd': sbd,
        'toan': entry_math.get(),
        'ngu_van': entry_literature.get(),
        'ngoai_ngu': entry_foreign_lang.get(),
    }
    global df
    df = data_crud.update_data(df, sbd, updated_row)
    data_crud.save_data(df, default_file_path)
    messagebox.showinfo("Thành công", "Đã cập nhật thông tin sinh viên")
    display_table(df)

def delete_student():
    """
    Xóa sinh viên dựa trên SBD được nhập.
    """
    sbd = entry_sbd.get()
    global df
    df = data_crud.delete_data(df, sbd)
    data_crud.save_data(df, default_file_path)
    messagebox.showinfo("Thành công", "Đã xóa sinh viên")
    display_table(df)

def center_window(root):
    """
    Căn giữa cửa sổ Tkinter trên màn hình.
    """
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Quản lý sinh viên")

# Căn giữa cửa sổ
root.update()
center_window(root)

# Các trường nhập liệu với khoảng cách padding
tk.Label(root, text="SBD:").grid(row=0, column=0, padx=10, pady=5)
entry_sbd = tk.Entry(root)
entry_sbd.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Toán:").grid(row=1, column=0, padx=10, pady=5)
entry_math = tk.Entry(root)
entry_math.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ngữ văn:").grid(row=2, column=0, padx=10, pady=5)
entry_literature = tk.Entry(root)
entry_literature.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Ngoại ngữ:").grid(row=3, column=0, padx=10, pady=5)
entry_foreign_lang = tk.Entry(root)
entry_foreign_lang.grid(row=3, column=1, padx=10, pady=5)

# Nút thêm, sửa, xóa, hiển thị với khoảng cách padding
btn_add = tk.Button(root, text="Thêm sinh viên", command=add_student)
btn_add.grid(row=4, column=0, padx=10, pady=5)

btn_update = tk.Button(root, text="Cập nhật sinh viên", command=update_student)
btn_update.grid(row=4, column=1, padx=10, pady=5)

btn_delete = tk.Button(root, text="Xóa sinh viên", command=delete_student)
btn_delete.grid(row=5, column=0, padx=10, pady=5)

btn_display = tk.Button(root, text="Hiển thị sinh viên", command=display_student)
btn_display.grid(row=5, column=1, padx=10, pady=5)

# Nút để tải file CSV
btn_load_file = tk.Button(root, text="Tải file CSV", command=load_file)
btn_load_file.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Text box để hiển thị thông tin sinh viên
text_output = tk.Text(root, height=15, width=70, state='disabled')
text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Hiển thị dữ liệu mặc định khi khởi động
if df is not None:
    display_table(df)

# Căn giữa cửa sổ khi thay đổi kích thước
root.bind('<Configure>', lambda event: center_window(root))

# Chạy giao diện chính
root.mainloop()
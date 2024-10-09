import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from modules.data_cleaning import remove_missing_values, remove_duplicates, correct_formatting
from modules.data_visualization import plot_average_scores
from modules.data_crud import read_data, add_data, update_data, delete_data, save_data

# Khởi tạo DataFrame ban đầu
df = pd.DataFrame()

# Hàm tải dữ liệu từ file CSV
def load_data():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = read_data(file_path)
        refresh_table()

# Hàm làm sạch dữ liệu
def clean_data():
    global df
    if df is not None:
        df = remove_missing_values(df)
        df = remove_duplicates(df)
        df = correct_formatting(df)
        refresh_table()
        messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch.")

# Hàm trực quan hóa dữ liệu
def visualize_data():
    if df is not None:
        plot_average_scores(df)

# Hàm làm mới bảng sau khi thêm hoặc xóa dữ liệu
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))

# Thêm sinh viên mới
def add_student():
    global df
    try:
        sbd = int(sbd_entry.get())
        toan = float(toan_entry.get())
        ngu_van = float(ngu_van_entry.get())
        ngoai_ngu = float(ngoai_ngu_entry.get())
        vat_li = float(vat_li_entry.get())
        hoa_hoc = float(hoa_hoc_entry.get())
        sinh_hoc = float(sinh_hoc_entry.get())
        lich_su = float(lich_su_entry.get())
        dia_li = float(dia_li_entry.get())
        gdcd = float(gdcd_entry.get())
        ma_ngoai_ngu = int(ma_ngoai_ngu_entry.get())

        new_row = {
            'sbd': sbd,
            'toan': toan,
            'ngu_van': ngu_van,
            'ngoai_ngu': ngoai_ngu,
            'vat_li': vat_li,
            'hoa_hoc': hoa_hoc,
            'sinh_hoc': sinh_hoc,
            'lich_su': lich_su,
            'dia_li': dia_li,
            'gdcd': gdcd,
            'ma_ngoai_ngu': ma_ngoai_ngu
        }

        df = df.append(new_row, ignore_index=True)
        refresh_table()
        messagebox.showinfo("Thông báo", "Sinh viên đã được thêm thành công!")
        clear_entries()

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng cho các trường!")

# Xóa thông tin trong các trường nhập
def clear_entries():
    sbd_entry.delete(0, tk.END)
    toan_entry.delete(0, tk.END)
    ngu_van_entry.delete(0, tk.END)
    ngoai_ngu_entry.delete(0, tk.END)
    vat_li_entry.delete(0, tk.END)
    hoa_hoc_entry.delete(0, tk.END)
    sinh_hoc_entry.delete(0, tk.END)
    lich_su_entry.delete(0, tk.END)
    dia_li_entry.delete(0, tk.END)
    gdcd_entry.delete(0, tk.END)
    ma_ngoai_ngu_entry.delete(0, tk.END)

# Hàm lọc sinh viên có điểm cao
def filter_students_by_score():
    global df
    selected_subject = subject_combobox.get()
    if selected_subject in df.columns:
        top_students = df[df[selected_subject] == df[selected_subject].max()]
        refresh_table(top_students)

# GUI chính
def run_gui():
    global sbd_entry, toan_entry, ngu_van_entry, ngoai_ngu_entry, vat_li_entry
    global hoa_hoc_entry, sinh_hoc_entry, lich_su_entry, dia_li_entry, gdcd_entry, ma_ngoai_ngu_entry
    global tree, subject_combobox

    root = tk.Tk()
    root.title("Quản lý điểm thi THPT")

    # Tạo khung nhập liệu
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    # Các trường nhập dữ liệu sinh viên
    tk.Label(input_frame, text="SBD").grid(row=0, column=0)
    sbd_entry = tk.Entry(input_frame)
    sbd_entry.grid(row=0, column=1)

    tk.Label(input_frame, text="Toán").grid(row=1, column=0)
    toan_entry = tk.Entry(input_frame)
    toan_entry.grid(row=1, column=1)

    tk.Label(input_frame, text="Ngữ Văn").grid(row=2, column=0)
    ngu_van_entry = tk.Entry(input_frame)
    ngu_van_entry.grid(row=2, column=1)

    tk.Label(input_frame, text="Ngoại Ngữ").grid(row=3, column=0)
    ngoai_ngu_entry = tk.Entry(input_frame)
    ngoai_ngu_entry.grid(row=3, column=1)

    tk.Label(input_frame, text="Vật Lý").grid(row=4, column=0)
    vat_li_entry = tk.Entry(input_frame)
    vat_li_entry.grid(row=4, column=1)

    tk.Label(input_frame, text="Hóa Học").grid(row=5, column=0)
    hoa_hoc_entry = tk.Entry(input_frame)
    hoa_hoc_entry.grid(row=5, column=1)

    tk.Label(input_frame, text="Sinh Học").grid(row=6, column=0)
    sinh_hoc_entry = tk.Entry(input_frame)
    sinh_hoc_entry.grid(row=6, column=1)

    tk.Label(input_frame, text="Lịch Sử").grid(row=7, column=0)
    lich_su_entry = tk.Entry(input_frame)
    lich_su_entry.grid(row=7, column=1)

    tk.Label(input_frame, text="Địa Lý").grid(row=8, column=0)
    dia_li_entry = tk.Entry(input_frame)
    dia_li_entry.grid(row=8, column=1)

    tk.Label(input_frame, text="GDCD").grid(row=9, column=0)
    gdcd_entry = tk.Entry(input_frame)
    gdcd_entry.grid(row=9, column=1)

    tk.Label(input_frame, text="Mã Ngoại Ngữ").grid(row=10, column=0)
    ma_ngoai_ngu_entry = tk.Entry(input_frame)
    ma_ngoai_ngu_entry.grid(row=10, column=1)

    # Nút Thêm sinh viên
    add_button = tk.Button(root, text="Thêm Sinh Viên", command=add_student)
    add_button.pack(pady=10)

    # Tạo bảng hiển thị dữ liệu
    tree_frame = tk.Frame(root)
    tree_frame.pack()

    tree = ttk.Treeview(tree_frame, columns=(df.columns), show="headings", height=10)
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack()

    # Tải dữ liệu, làm sạch, trực quan, và lọc
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    load_button = tk.Button(btn_frame, text="Tải Dữ Liệu", command=load_data)
    load_button.grid(row=0, column=0, padx=10)

    clean_button = tk.Button(btn_frame, text="Làm Sạch Dữ Liệu", command=clean_data)
    clean_button.grid(row=0, column=1, padx=10)

    visualize_button = tk.Button(btn_frame, text="Trực Quan Dữ Liệu", command=visualize_data)
    visualize_button.grid(row=0, column=2, padx=10)

    # Chọn môn học để lọc
    subject_combobox = ttk.Combobox(btn_frame, values=list(df.columns), state="readonly")
    subject_combobox.grid(row=1, column=0, padx=10)
    filter_button = tk.Button(btn_frame, text="Lọc Sinh Viên", command=filter_students_by_score)
    filter_button.grid(row=1, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()

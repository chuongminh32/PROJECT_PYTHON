import pandas as pd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import seaborn as sns

# === Chức năng 1: Xếp hạng sinh viên ===
def rank_students(data_path, top_n):
    df = pd.read_csv(data_path)
    df['GPA'] = df[['english.grade', 'math.grade', 'sciences.grade', 'language.grade']].mean(axis=1)
    df = df.sort_values(by='GPA', ascending=False)
    top_students = df.head(top_n)

    # Hiển thị bảng xếp hạng
    result_window = Toplevel()
    result_window.title(f"Top {top_n} Sinh Viên")
    tree = ttk.Treeview(result_window, columns=('ID', 'Name', 'GPA'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('GPA', text='GPA')
    for _, row in top_students.iterrows():
        tree.insert("", END, values=(row['id'], row['name'], round(row['GPA'], 2)))
    tree.pack(fill=BOTH, expand=True)

# === Chức năng 2: Phân bố điểm số ===


# === Chức năng 3: Phân tích điểm theo nhóm ===
def analyze_by_group(data_path, group_by):
    df = pd.read_csv(data_path)
    group_data = df.groupby(group_by)[['english.grade', 'math.grade', 'sciences.grade', 'language.grade']].mean()

    # Hiển thị bảng kết quả
    result_window = Toplevel()
    result_window.title(f"Điểm trung bình theo {group_by}")
    tree = ttk.Treeview(result_window, columns=('Group', 'English', 'Math', 'Sciences', 'Language'), show='headings')
    tree.heading('Group', text=group_by)
    tree.heading('English', text='English')
    tree.heading('Math', text='Math')
    tree.heading('Sciences', text='Sciences')
    tree.heading('Language', text='Language')
    for group, row in group_data.iterrows():
        tree.insert("", END, values=(group, *[round(val, 2) for val in row]))
    tree.pack(fill=BOTH, expand=True)

# === Giao diện chính ===
def show_menu():
    root = Tk()
    root.title("Hệ thống Quản lý Sinh viên")
    root.geometry("400x300")

    data_path = "data/data_clean.csv"  # Đường dẫn đến tệp CSV

    def handle_rank():
        rank_students(data_path, 5)

    def handle_distribution():
        plot_distribution(data_path, "math.grade")

    def handle_analyze():
        analyze_by_group(data_path, "nationality")

    def handle_correlation():
        plot_correlation(data_path)

    Label(root, text="Quản lý Sinh viên", font=("Arial", 16, "bold")).pack(pady=20)

    Button(root, text="Xếp hạng sinh viên", command=handle_rank).pack(pady=10)
    Button(root, text="Phân bố điểm số", command=handle_distribution).pack(pady=10)
    Button(root, text="Phân tích theo quốc tịch", command=handle_analyze).pack(pady=10)
    Button(root, text="Mối tương quan", command=handle_correlation).pack(pady=10)

    root.mainloop()

# === Chạy ứng dụng ===
if __name__ == "__main__":
    show_menu()



import csv
import tkinter as tk
from tkinter import ttk
import pandas as pd

class Student:
    def __init__(self, student_id, name, country, total_score):
        self.student_id = student_id
        self.name = name
        self.country = country
        self.total_score = total_score

def stu_filter(students, country):
    return [student for student in students if student.country.lower() == country.lower()]
    def display_students_in_frame(students, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        columns = ('ID', 'Name', 'Country', 'Total Score')
        tree = ttk.Treeview(frame, columns=columns, show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Country', text='Country')
        tree.heading('Total Score', text='Total Score')

        for student in students:
            tree.insert('', tk.END, values=(student.student_id, student.name, student.country, student.total_score))

        tree.pack(fill=tk.BOTH, expand=True)

def stu_top(students):
    return sorted(students, key=lambda student: student.total_score, reverse=True)[:10]

def stu_find(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def read_students_from_csv(file_path):
    students = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = int(row['id'])
            name = row['name']
            country = row['nationality']
            total_score = sum(float(row[subject]) for subject in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade'])
            students.append(Student(student_id, name, country, total_score))
    return students

def sort_increase_point():
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("data/data_clean.csv")

        # Các cột liên quan đến điểm
        score_columns = [
            "english.grade", "math.grade", "sciences.grade", "language.grade",
            "portfolio.rating", "coverletter.rating", "refletter.rating"
        ]

        # Điền giá trị 0 vào các ô trống trong các cột liên quan đến điểm
        df[score_columns] = df[score_columns].fillna(0)

        # Tính tổng điểm
        df["total_score"] = df[score_columns].sum(axis=1)

        # Sắp xếp giảm dần theo tổng điểm
        df_sorted_desc = df.sort_values(by="total_score", ascending=False)

        # Lưu DataFrame đã sắp xếp vào file CSV mới
        df_sorted_desc.to_csv("data/sorted_file.csv", index=False)

        return True  # Trả về True khi hoàn tất
    except Exception as e:
        print(f"Lỗi: {e}")
        return False  # Trả về False nếu xảy ra lỗ
result = sort_increase_point()
print(f"Kết quả sắp xếp và lưu file: {result}")

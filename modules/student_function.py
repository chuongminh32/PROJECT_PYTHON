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
            "english.grade", "math.grade", "sciences.grade", "language.grade", "portfolio.rating", "coverletter.rating", "refletter.rating"
        ]

        # Điền giá trị 0 vào các ô trống trong các cột liên quan đến điểm
        df[score_columns] = df[score_columns].fillna(0)

        # Tính tổng điểm
        df["total_score"] = df[score_columns].sum(axis=1)

        # Sắp xếp giảm dần theo tổng điểm
        df_sorted_desc = df.sort_values(by="total_score", ascending=False)

        # Lưu DataFrame đã sắp xếp vào file CSV mới
        df_sorted_desc.to_csv("data/sorted_by_point.csv", index=False)

        return True  # Trả về True khi hoàn tất
    except Exception as e:
        print(f"Lỗi: {e}")
        return False  # Trả về False nếu xảy ra lỗ
def sort_increase_age():
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("data/data_clean.csv")

        # Điền giá trị 0 vào các ô trống trong cột tuổi nếu có
        df["age"] = df["age"].fillna(0)

        # Sắp xếp tăng dần theo cột Tuổi
        df_sorted_age = df.sort_values(by="age", ascending=True)

        # Lưu DataFrame đã sắp xếp vào file CSV mới
        df_sorted_age.to_csv("data/sorted_by_age.csv", index=False)

        return True  # Trả về True khi hoàn tất
    except Exception as e:
        print(f"Lỗi: {e}")
        return False  # Trả về False nếu xảy ra lỗi



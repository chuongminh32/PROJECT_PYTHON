import csv
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



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

def sort_desc_gpa():
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("data/data_clean.csv")

        # Các cột liên quan đến điểm GPA
        gpa_columns = ["english.grade", "math.grade", "sciences.grade", "language.grade"]

        # Điền giá trị 0 vào các ô trống trong các cột GPA
        df[gpa_columns] = df[gpa_columns].fillna(0)

        # Tính GPA
        df["GPA"] = df[gpa_columns].mean(axis=1)

        # Sắp xếp giảm dần theo GPA
        df_sorted_asc = df.sort_values(by="GPA", ascending=False)

        # Lưu DataFrame đã sắp xếp vào file CSV mới
        df_sorted_asc.to_csv("data/sorted_by_gpa.csv", index=False)

        print("Sắp xếp thành công. File đã được lưu tại: data/sorted_by_gpa.csv")
        return True  # Trả về True khi hoàn tất
    except Exception as e:
        print(f"Lỗi: {e}")
        return False  # Trả về False nếu xảy ra lỗi

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

# chart
def plot_distribution(data_path, subject):
    df = pd.read_csv(data_path)
    grades = df[subject]

    # Tạo biểu đồ phân bố
    plt.figure(figsize=(8, 5))
    sns.histplot(grades, bins=10, kde=True, color='blue')
    plt.title(f"Phân bố điểm số: {subject}")
    plt.xlabel("Điểm số")
    plt.ylabel("Số lượng sinh viên")
    plt.grid()
    plt.show()



def plot_correlation(data_path):
    df = pd.read_csv(data_path)
    correlation_matrix = df[['english.grade', 'math.grade', 'sciences.grade', 'language.grade', 'age']].corr()

    # Vẽ heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Ma trận tương quan giữa các yếu tố")
    plt.show()




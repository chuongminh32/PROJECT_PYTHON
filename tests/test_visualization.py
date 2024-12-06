import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mplcursors

import unittest
from io import StringIO
import os

def plot_country_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    nation = df['nationality'].value_counts()
    total = nation.sum()

    labels = [label if size / total >= 0.024 else "" for label, size in zip(nation.index, nation)]
    sizes = nation.values

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p >= 10 else '', startangle=140)

    plt.show()

def plot_grade_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    subject = ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']

    # Kiểm tra nếu DataFrame trống hoặc thiếu các cột cần thiết
    if df.empty or df[subject].isnull().all().all():
        raise ValueError("DataFrame trống hoặc không có dữ liệu hợp lệ.")
    if not all(sub in df.columns for sub in subject):
        raise KeyError("DataFrame thiếu các cột cần thiết.")

    grade = df[subject].mean()

    plt.figure(figsize=(10,6))
    plt.bar(subject, grade)
    plt.xlabel("Môn học")
    plt.ylabel("Điểm")
    plt.title("Biều đồ điểm trung bình môn học")

    for i, value in enumerate(grade):
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

    plt.show()

class TestPlotGradeBtn(unittest.TestCase):

    def tearDown(self):
        if hasattr(self, 'temp_file') and os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_empty_data(self):
    # Tạo file tạm với nội dung trống, chỉ có tiêu đề các cột
        empty_data = """ english.grade,math.grade,sciences.grade,language.grade \n"""
        self.temp_file = 'temp_empty_data.csv'
        with open(self.temp_file, 'w') as f:
            f.write(empty_data)

        with self.assertRaises(ValueError):
            plot_grade_btn(self.temp_file)

    def test_mismatched_data(self):
        # Tạo dữ liệu không khớp và lưu vào file tạm thời
        mismatched_data = """english.grade,math.grade,sciences.grade
        4.0,3.8,4.5
        4.3,4.1,5.0
        3.6,4.1,4.4
        5.0,4.7,4.5
        3.9,4.6,4.5"""

        # Tạo tên tạm cho file CSV
        self.temp_file = 'temp_mismatched_data.csv'

        # Ghi dữ liệu vào file CSV
        with open(self.temp_file, 'w') as f:
            f.write(mismatched_data)

        # Kiểm tra xem KeyError có được ném keông
        with self.assertRaises(KeyError):
            plot_grade_btn(self.temp_file)
    '''
if __name__ == '__main__':
    unittest.main()

'''
if __name__ == '__main__':
    plot_country_btn("data/student-dataset.csv")



class TestPlotGradeBtn(unittest.TestCase):

    def tearDown(self):
        if hasattr(self, 'temp_file') and os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_empty_data(self):
    # Tạo file tạm với nội dung trống, chỉ có tiêu đề các cột
        empty_data = """ english.grade,math.grade,sciences.grade,language.grade \n"""
        self.temp_file = 'temp_empty_data.csv'
        with open(self.temp_file, 'w') as f:
            f.write(empty_data)

        with self.assertRaises(ValueError):
            plot_grade_btn(self.temp_file)

    def test_mismatched_data(self):
        # Tạo dữ liệu không khớp và lưu vào file tạm thời
        mismatched_data = """english.grade,math.grade,sciences.grade
        4.0,3.8,4.5
        4.3,4.1,5.0
        3.6,4.1,4.4
        5.0,4.7,4.5
        3.9,4.6,4.5"""

        # Tạo tên tạm cho file CSV
        self.temp_file = 'temp_mismatched_data.csv'

        # Ghi dữ liệu vào file CSV
        with open(self.temp_file, 'w') as f:
            f.write(mismatched_data)

        # Kiểm tra xem KeyError có được ném keông
        with self.assertRaises(KeyError):
            plot_grade_btn(self.temp_file)


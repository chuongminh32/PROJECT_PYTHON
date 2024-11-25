import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_top_students(df, column_name):
    return df.nlargest(10, column_name)
    
# sắp xếp giảm dần theo GPA
def sort_desc_gpa():
    """
    Sắp xếp dữ liệu sinh viên theo điểm GPA giảm dần và lưu vào file CSV mới.
    Hàm này thực hiện các bước sau:
    1. Đọc dữ liệu từ file CSV "data/data_clean.csv".
    2. Điền giá trị 0 vào các ô trống trong các cột GPA.
    3. Tính điểm GPA trung bình cho mỗi sinh viên.
    4. Sắp xếp dữ liệu theo điểm GPA giảm dần.
    5. Lưu dữ liệu đã sắp xếp vào file CSV mới "data/sorted_by_gpa.csv".
    Returns:
        bool: Trả về True nếu quá trình hoàn tất thành công, ngược lại trả về False nếu có lỗi xảy ra.
    """
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

# sắp xếp tăng dần theo tuổi
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

# biểu đồ phân bố điểm số
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

# biểu đồ tương quan giữa các yếu tố
def plot_correlation(data_path):
    df = pd.read_csv(data_path)
    correlation_matrix = df[['english.grade', 'math.grade', 'sciences.grade', 'language.grade', 'age']].corr()

    # Vẽ heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Ma trận tương quan giữa các yếu tố")
    plt.show()

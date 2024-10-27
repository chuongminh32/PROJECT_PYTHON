import matplotlib.pyplot as plt
import numpy as np

print("TRỰC QUAN HÓA DATA".center(50, '='))
def plot_grade(df):
    """Vẽ biểu đồ điểm học tập."""
    grade_cols = ['english.grade','math.grade','sciences.grade','language.grade']

    df_grades = df[grade_cols]

    # Tạo màu thay đổi cho từng cột (tạo dãy màu)
    colours = plt.cm.viridis(np.linspace(0, 1, len(grade_cols)))

    df_grades.plot(kind='bar', figsize=(10, 6))

    plt.title("Comparison of Grades in Different Subjects")
    plt.xlabel("Student ID")
    plt.ylabel("Grades")

    # Tạo lưới mờ
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Thêm số liệu trên đầu các cột
    for i, value in enumerate(df_grades):
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

    # In nghiêng các subject
    plt.xticks(rotation=45)

    # Lấy tên của các cột làm nhãn cho chú thích
    plt.legend(title="Subjects")

    plt.show()
    '''
    # Tạo heatmap 
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[ratings_cols].T, annot=True, cmap="YlGnBu", cbar=True, linewidths=0.5)
    plt.title("Heatmap of Grades and Portfolio Ratings")
    plt.xlabel("Student ID")
    plt.ylabel("Grades / Ratings")
    plt.show()
    '''
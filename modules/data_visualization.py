import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from pathlib import Path


print("TRỰC QUAN HÓA DỮ LIỆU".center(50, '='))

def plot_grade(df):
    """Vẽ biểu đồ điểm học tập."""
    grade_cols = ['english.grade','math.grade','sciences.grade','language.grade']

    df_grades = df[grade_cols].mean()

    # Tạo màu thay đổi cho từng cột (tạo dãy màu từ xanh dương tới xanh lá)
    colours = plt.cm.coolwarm(np.linspace(0, 1, len(grade_cols)))

    # Thiết lập kích thước và màu sắc cho biểu đồ
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
    bars = ax.bar(grade_cols, df_grades, color=colours)

    plt.title("Biểu đồ điểm học tập trung bình")
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

    # Hover interaction
    annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(bar):
        """Cập nhật chú thích khi hover."""
        x = bar.get_x() + bar.get_width() / 2
        y = bar.get_height()
        annot.xy = (x, y)
        text = f"{bar.get_label()}:\n{y:.2f}"
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.6)

    def on_hover(event):
        """Hiển thị thông tin khi hover chuột."""
        visible = annot.get_visible()
        if event.inaxes == ax:
            for bar in bars:
                if bar.contains(event)[0]:
                    update_annot(bar)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if visible:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    # Click interaction
    def on_click(event):
        """Xử lý sự kiện khi click."""
        if event.inaxes == ax:
            for bar in bars:
                if bar.contains(event)[0]:
                    subject = bar.get_label()
                    grade = bar.get_height()
                    print(f"Bạn đã chọn: {subject} - Điểm trung bình: {grade:.2f}")

    fig.canvas.mpl_connect("motion_notify_event", on_hover)
    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.tight_layout()
    plt.show()

# def main():
#      # Đường dẫn đến thư mục cha của thư mục "modules"
#     project_root = Path(__file__).resolve().parent.parent

#     # Đường dẫn đến file data.csv trong thư mục data
#     file_path = project_root / "data" / "data_demo.csv"
#     df = pd.read_csv(file_path)
#     plot_grade(df)

# if __name__ == "__main__":
#     main()

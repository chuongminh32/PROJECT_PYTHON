import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("TRỰC QUAN HÓA DỮ LIỆU".center(50, '='))
def plot_grade(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    """Vẽ biểu đồ điểm học tập."""
    grade_cols = ['english.grade','math.grade','sciences.grade','language.grade']

    df_grades = df[grade_cols].mean()

    # Thiết lập kích thước và màu sắc cho biểu đồ
    colours = plt.cm.Blues(np.linspace(0.5, 1, len(grade_cols)))
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
    bars = ax.bar(grade_cols, df_grades, color=colours)

    #df_grades.plot(kind='bar', figsize=(10, 6))

    plt.title("Biểu đồ điểm học tập trung bình")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")

    # Tạo lưới mờ
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Thêm số liệu trên đầu các cột
    for i, value in enumerate(df_grades):
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

    # In nghiêng các subject
    plt.xticks(rotation=45)
    plt.legend()

    # Hover interaction
    annot = ax.annotate("", xy=(0,0), xytext=(11,11),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="m"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(bar):
        """Cập nhật chú thích khi hover."""
        x = bar.get_x() + bar.get_width() / 2
        y = bar.get_height()
        for gr in grade_cols:
            if df[gr].mean() == bar.get_height():
                label = gr
        annot.xy = (x, y)
        text = f"{label}:\n{y:.2f}"
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.3)

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
                    for gr in grade_cols:
                        if df[gr].mean() == bar.get_height():
                            subject = gr
                    grade = bar.get_height()
                    print(f"Bạn đã chọn: {subject} - Điểm trung bình: {grade:.2f}")

    fig.canvas.mpl_connect("motion_notify_event", on_hover)
    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.tight_layout()
    plt.show()

def plot_age(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    """Vẽ biểu đồ phân bố độ tuổi."""

    plt.figure(figsize=(8, 5))
    plt.hist(df['age'], bins=5)
    plt.title("Age Distribution of Students")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.xticks([15,20,21,22,23,24,25,26,30])
    plt.show()

def plot_country(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    """Vẽ biểu đồ phân bố quốc gia."""
    nationality_counts = df['nationality'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Phân bố quốc gia")
    plt.legend()
    plt.legend(loc='lower right')
    plt.show()

#plot_grade('data/data_demo.csv')
#plot_age('data/data_demo.csv')

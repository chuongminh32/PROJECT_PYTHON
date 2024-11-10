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
    plt.xlabel("Môn học")
    plt.ylabel("Điểm")

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
    plt.title("Biểu đồ phân bố độ tuổi")
    plt.xlabel("Tuổi")
    plt.ylabel("Mật độ")
    plt.xticks([15,19,20,21,22,23,24,25,26,30])
    plt.show()

def plot_country(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    """Vẽ biểu đồ phân bố quốc gia."""
    nationality_counts = df['nationality'].value_counts()
    total = nationality_counts.sum()
    labels = []
    sizes = []
    for label, size in zip(nationality_counts.index, nationality_counts):
        if size / total >= 0.024:
            labels.append(label)
        else:
            labels.append("")
        sizes.append(size)

    fig, ax = plt.subplots(figsize=(12, 7))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.4 else '', startangle=140)

    plt.title("Phân bố quốc gia")

    plt.legend(labels=nationality_counts.index, loc='center left', bbox_to_anchor=(1, 0.5))

    # Thềm phần hover chuột để xem phần trăm những nước có % nhỏ
    annot = ax.annotate("", xy=(0,0), xytext=(10,10), textcoords="offset points", bbox=dict     (boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(wedge, event):
        x, y = wedge.center
        angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
        x = x + wedge.r * 0.5 * np.cos(np.radians(angle))
        y = y + wedge.r * 0.5 * np.sin(np.radians(angle))
        annot.xy = (x, y)
        label = nationality_counts.index[wedges.index(wedge)]
        size = sizes[wedges.index(wedge)]
        percent = size / total * 100
        text = f"{label}: {percent:.1f}%"
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor('lightblue')
        annot.set_fontsize(12)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            for wedge in wedges:
                if wedge.contains(event)[0]:
                    update_annot(wedge, event)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()


#plot_grade('data/student-dataset.csv')
#plot_age('data/student-dataset.csv')
#plot_country('data/student-dataset.csv')
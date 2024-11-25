import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import mplcursors


# FigureCanvasTkAgg biến một đối tượng Figure (biểu đồ) của Matplotlib
#  thành một widget của Tkinter để bạn có thể nhúng vào giao diện.
# widget là một widget của Tkinter, frame là một widget Frame của Tkinter.
# Tạo một widget FigureCanvasTkAgg từ một đối tượng Figure của Matplotlib.
def create_canvas(fig, frame):
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# Tạo biểu đồ cột từ một DataFrame.
def create_bar_chart(df, cols, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(cols, df[cols].mean(), color=plt.cm.Blues(np.linspace(0.5, 1, len(cols))))
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    for i, value in enumerate(df[cols].mean()): # Hiển thị giá trị trên cột
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')
    return fig

# Tạo biểu đồ hình tròn từ một DataFrame.
def create_pie_chart(df, col, title):
    """
    Tạo biểu đồ hình tròn từ một DataFrame.
    Parameters:
    df (pandas.DataFrame): DataFrame chứa dữ liệu.
    col (str): Tên cột trong DataFrame để tạo biểu đồ hình tròn.
    title (str): Tiêu đề của biểu đồ.
    Returns:
    matplotlib.figure.Figure: Đối tượng Figure của biểu đồ hình tròn.
    Hàm con:
    update_annot(wedge, event):
        Cập nhật chú thích khi di chuột qua một phần của biểu đồ.
        Parameters:
        wedge (matplotlib.patches.Wedge): Phần của biểu đồ hình tròn.
        event (matplotlib.backend_bases.Event): Sự kiện di chuột.
    hover(event):
        Xử lý sự kiện di chuột để hiển thị chú thích.
        Parameters:
        event (matplotlib.backend_bases.Event): Sự kiện di chuột.
    """
    counts = df[col].value_counts()
    total = counts.sum()
    labels = [label if size / total >= 0.024 else "" for label, size in zip(counts.index, counts)]
    sizes = counts.values
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set(title=title)
    wedges, _, _ = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p >= 10 else '', startangle=140)
    annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(wedge, event):
        angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
        x = wedge.r * 0.5 * np.cos(np.radians(angle)) # r = 1
        y = wedge.r * 0.5 * np.sin(np.radians(angle)) # r = 1
        annot.xy = (x, y)
        label = counts.index[wedges.index(wedge)]
        percent = sizes[wedges.index(wedge)] / total * 100
        annot.set_text(f"{label}: {percent:.1f}%")
        annot.get_bbox_patch().set_facecolor('lightblue')
        annot.set_fontsize(12)

    def hover(event):
        if event.inaxes == ax:
            for wedge in wedges:
                if wedge.contains(event)[0]:
                    update_annot(wedge, event)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        annot.set_visible(False)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    return fig

# Tạo biểu đồ đường từ một DataFrame.
def plot_grade(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)
    fig = create_bar_chart(df, ['english.grade', 'math.grade', 'sciences.grade', 'language.grade'], "Biểu đồ điểm học tập trung bình", "Môn học", "Điểm")
    create_canvas(fig, frame)

# Tạo biểu đồ đường từ một DataFrame detail
def plot_grade_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    fig = create_bar_chart(df, ['english.grade', 'math.grade', 'sciences.grade', 'language.grade'], "Biểu đồ điểm học tập trung bình", "Môn học", "Điểm")
    plt.show()

def plot_country(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)
    fig = create_pie_chart(df, 'nationality', "Biểu đồ phân bố quốc tịch")
    create_canvas(fig, frame)

def plot_country_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    fig = create_pie_chart(df, 'nationality', "Biểu đồ phân bố quốc tịch")
    plt.show()

# Tạo biểu đồ cột từ một DataFrame.
def plot_age(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['age'], bins=5)
    ax.set_title("Biểu đồ phân bố độ tuổi")
    ax.set_xlabel("Tuổi")
    ax.set_ylabel("Mật độ")
    ax.set_xticks([15, 19, 20, 21, 22, 23, 24, 25, 26, 30])
    plt.tight_layout()
    create_canvas(fig, frame)

def plot_age_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['age'], bins=5)
    ax.set_title("Biểu đồ phân bố độ tuổi")
    ax.set_xlabel("Tuổi")
    ax.set_ylabel("Mật độ")
    ax.set_xticks([15, 19, 20, 21, 22, 23, 24, 25, 26, 30])
    plt.tight_layout()
    plt.show()

# 
def plot_gender(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)
    fig = create_pie_chart(df, 'gender', "Biểu đồ Tỉ Lệ Nam Nữ")
    create_canvas(fig, frame) 

def plot_gender_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    fig = create_pie_chart(df, 'gender', "Biểu đồ Tỉ Lệ Nam Nữ")
    plt.show()


def plot_point_old(FILE_PATH, frame):
    data = pd.read_csv(FILE_PATH)
    fig = plt.Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        ax.scatter(data['age'], data[mon], label=mon, alpha=0.7, s=50)
    ax.set_xlabel('Tuổi', fontsize=12)
    ax.set_ylabel('Điểm số', fontsize=12)
    ax.set_title('Biểu đồ phân tán của Tuổi và Điểm học tập', fontsize=14)
    mplcursors.cursor(ax, hover=True)
    create_canvas(fig, frame)

def plot_point_old_btn(FILE_PATH):
    plt.close('all')
    data = pd.read_csv(FILE_PATH)
    fig, ax = plt.subplots(figsize=(10, 6))
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        ax.scatter(data['age'], data[mon], label=mon, alpha=0.7, s=50)
    ax.set_xlabel('Tuổi', fontsize=12)
    ax.set_ylabel('Điểm số', fontsize=12)
    ax.set_title('Biểu đồ phân tán của Tuổi và Điểm học tập', fontsize=14)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Môn học")
    mplcursors.cursor(ax, hover=True)
    plt.tight_layout()
    plt.show()

def plot_personal(FILE_PATH, frame):
    data = pd.read_csv(FILE_PATH)
    fig = plt.Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    diem_trung_binh = data[['portfolio.rating', 'coverletter.rating', 'refletter.rating']].mean()
    bars = diem_trung_binh.plot(kind='bar', color=['#4CAF50', '#FF5722', '#2196F3'], ax=ax)
    ax.set_xlabel('Loại Đánh Giá')
    ax.set_ylabel('Điểm Trung Bình')
    ax.set_title('Biểu đồ thanh của Điểm Đánh Giá Cá Nhân Trung Bình')
    ax.set_xticklabels(diem_trung_binh.index, rotation=0)
    for bar in bars.patches:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)
    create_canvas(fig, frame)

def plot_personal_btn(FILE_PATH):
    data = pd.read_csv(FILE_PATH)
    plt.close('all')
    fig, ax = plt.subplots(figsize=(10, 6))
    diem_trung_binh = data[['portfolio.rating', 'coverletter.rating', 'refletter.rating']].mean()
    bars = diem_trung_binh.plot(kind='bar', color=['#4CAF50', '#FF5722', '#2196F3'], ax=ax)
    ax.set_xlabel('Loại Đánh Giá')
    ax.set_ylabel('Điểm Trung Bình')
    ax.set_title('Biểu đồ Thanh của Điểm Đánh Giá Cá Nhân Trung Bình')
    ax.set_xticklabels(diem_trung_binh.index, rotation=0)
    for bar in bars.patches:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_point_rating(FILE_PATH, frame):
    data = pd.read_csv(FILE_PATH)
    fig = plt.Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    scatter_plots = []
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        scatter_plots.append(ax.scatter(data[mon], data['portfolio.rating'], label=f'{mon} và Đánh Giá Hồ Sơ', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['coverletter.rating'], label=f'{mon} và Đánh Giá Thư Xin Việc', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['refletter.rating'], label=f'{mon} và Đánh Giá Thư Giới Thiệu', alpha=0.6))
    ax.set_xlabel('Điểm số')
    ax.set_ylabel('Đánh giá')
    ax.set_title('Biểu đồ phân tán của Điểm và Đánh giá Cá Nhân')
    mplcursors.cursor(scatter_plots, hover=True)
    create_canvas(fig, frame)

def plot_point_rating_btn(FILE_PATH):
    plt.close('all')
    data = pd.read_csv(FILE_PATH)
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter_plots = []
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        scatter_plots.append(ax.scatter(data[mon], data['portfolio.rating'], label=f'{mon} - Hồ Sơ', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['coverletter.rating'], label=f'{mon} - Thư Xin Việc', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['refletter.rating'], label=f'{mon} - Thư Giới Thiệu', alpha=0.6))
    ax.set_xlabel('Điểm số')
    ax.set_ylabel('Đánh giá')
    ax.set_title('Biểu đồ phân tán của Điểm và Đánh giá Cá Nhân')
    mplcursors.cursor(scatter_plots, hover=True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.tight_layout()
    plt.show()

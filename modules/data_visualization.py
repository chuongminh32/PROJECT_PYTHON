# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# # Hàm vẽ biểu đồ điểm học tập


# def plot_grade(FILE_PATH, frame):
#     df = pd.read_csv(FILE_PATH)
#     grade_cols = ['english.grade', 'math.grade',
#                   'sciences.grade', 'language.grade']
#     df_grades = df[grade_cols].mean()  # Tính điểm trung bình các môn

#     # Tạo biểu đồ thanh
#     fig, ax = plt.subplots(figsize=(10, 6))
#     bars = ax.bar(grade_cols, df_grades, color=plt.cm.Blues(
#         np.linspace(0.5, 1, len(grade_cols))))

#     # Tùy chỉnh đồ thị
#     ax.set(title="Biểu đồ điểm học tập trung bình",
#            xlabel="Môn học", ylabel="Điểm")
#     plt.grid(axis='y', linestyle='--', alpha=0.5)  # Lưới mờ
#     for i, value in enumerate(df_grades):  # Hiển thị giá trị trên mỗi cột
#         plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

#     # Tạo canvas để nhúng biểu đồ vào trong Tkinter
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill="both", expand=True)

# # Hàm vẽ biểu đồ phân bố quốc gia


# def plot_country(FILE_PATH, frame):
#     df = pd.read_csv(FILE_PATH)
#     nationality_counts = df['nationality'].value_counts()
#     total = nationality_counts.sum()

#     # Chuẩn bị dữ liệu cho biểu đồ tròn
#     labels, sizes = [], []
#     for label, size in zip(nationality_counts.index, nationality_counts):
#         labels.append(label if size / total >= 0.024 else "")
#         sizes.append(size)

#     # Vẽ biểu đồ tròn
#     fig, ax = plt.subplots(figsize=(10, 6))

#     # tên biểu đồ
#     ax.set(title="Biểu đồ phân bố quốc tịch")

#     wedges, _, autotexts = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(
#         p) if p >= 2.4 else '', startangle=140)

#     # Tùy chỉnh hover để hiển thị thông tin chi tiết
#     annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points", bbox=dict(
#         boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
#     annot.set_visible(False)

#     def update_annot(wedge, event):
#         angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
#         x = wedge.r * 0.5 * np.cos(np.radians(angle))
#         y = wedge.r * 0.5 * np.sin(np.radians(angle))
#         annot.xy = (x, y)
#         label = nationality_counts.index[wedges.index(wedge)]
#         percent = sizes[wedges.index(wedge)] / total * 100
#         annot.set_text(f"{label}: {percent:.1f}%")
#         annot.get_bbox_patch().set_facecolor('lightblue')
#         annot.set_fontsize(12)

#     # Hàm xử lý hover
#     def hover(event):
#         if event.inaxes == ax:
#             for wedge in wedges:
#                 if wedge.contains(event)[0]:
#                     update_annot(wedge, event)
#                     annot.set_visible(True)
#                     fig.canvas.draw_idle()
#                     return
#         annot.set_visible(False)
#         fig.canvas.draw_idle()

#     fig.canvas.mpl_connect("motion_notify_event", hover)

#     # Tạo canvas để nhúng biểu đồ vào trong Tkinter
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill="both", expand=True)

# # Hàm vẽ biểu đồ phân bố độ tuổi


# def plot_age(FILE_PATH, frame):
#     df = pd.read_csv(FILE_PATH)

#     # Vẽ histogram độ tuổi
#     fig, ax = plt.subplots(figsize=(10, 6))
#     ax.hist(df['age'], bins=5)
#     ax.set_title("Biểu đồ phân bố độ tuổi")
#     ax.set_xlabel("Tuổi")
#     ax.set_ylabel("Mật độ")
#     ax.set_xticks([15, 19, 20, 21, 22, 23, 24, 25, 26, 30])
#     plt.tight_layout()

#     # Tạo canvas để nhúng biểu đồ vào trong Tkinter
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill="both", expand=True)


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Hàm vẽ biểu đồ điểm học tập
def plot_grade(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)
    grade_cols = ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']
    df_grades = df[grade_cols].mean()  # Tính điểm trung bình các môn

    # Tạo biểu đồ thanh
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(grade_cols, df_grades, color=plt.cm.Blues(np.linspace(0.5, 1, len(grade_cols))))

    # Tùy chỉnh đồ thị
    ax.set(title="Biểu đồ điểm học tập trung bình", xlabel="Môn học", ylabel="Điểm")
    plt.grid(axis='y', linestyle='--', alpha=0.5)  # Lưới mờ
    for i, value in enumerate(df_grades):  # Hiển thị giá trị trên mỗi cột
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

    # Tạo canvas để nhúng biểu đồ vào trong Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Hàm vẽ biểu đồ phân bố quốc gia
def plot_country(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)
    nationality_counts = df['nationality'].value_counts()
    total = nationality_counts.sum()

    # Chuẩn bị dữ liệu cho biểu đồ tròn
    labels, sizes = [], []
    for label, size in zip(nationality_counts.index, nationality_counts):
        labels.append(label if size / total >= 0.024 else "")
        sizes.append(size)

    # Vẽ biểu đồ tròn
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set(title="Biểu đồ phân bố quốc tịch")
    wedges, _, autotexts = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.4 else '', startangle=140)

    # Tùy chỉnh hover để hiển thị thông tin chi tiết
    annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points", bbox=dict(
        boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(wedge, event):
        angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
        x = wedge.r * 0.5 * np.cos(np.radians(angle))
        y = wedge.r * 0.5 * np.sin(np.radians(angle))
        annot.xy = (x, y)
        label = nationality_counts.index[wedges.index(wedge)]
        percent = sizes[wedges.index(wedge)] / total * 100
        annot.set_text(f"{label}: {percent:.1f}%")
        annot.get_bbox_patch().set_facecolor('lightblue')
        annot.set_fontsize(12)

    # Hàm xử lý hover
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

    # Tạo canvas để nhúng biểu đồ vào trong Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Hàm vẽ biểu đồ phân bố độ tuổi
def plot_age(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)

    # Vẽ histogram độ tuổi
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['age'], bins=5)
    ax.set_title("Biểu đồ phân bố độ tuổi")
    ax.set_xlabel("Tuổi")
    ax.set_ylabel("Mật độ")
    ax.set_xticks([15, 19, 20, 21, 22, 23, 24, 25, 26, 30])
    plt.tight_layout()

    # Tạo canvas để nhúng biểu đồ vào trong Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Hàm vẽ biểu đồ tỉ lệ nam nữ
def plot_gender(FILE_PATH, frame):
    df = pd.read_csv(FILE_PATH)

    # Tính số lượng nam nữ
    gender_counts = df['gender'].value_counts()
    total = gender_counts.sum()

    # Chuẩn bị dữ liệu cho biểu đồ tròn
    labels = gender_counts.index
    sizes = gender_counts.values

    # Vẽ biểu đồ tròn
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set(title="Biểu đồ Tỉ Lệ Nam Nữ")
    wedges, _, autotexts = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p), startangle=140)

    # Tùy chỉnh hover để hiển thị thông tin chi tiết
    annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points", bbox=dict(
        boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(wedge, event):
        angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
        x = wedge.r * 0.5 * np.cos(np.radians(angle))
        y = wedge.r * 0.5 * np.sin(np.radians(angle))
        annot.xy = (x, y)
        label = gender_counts.index[wedges.index(wedge)]
        percent = sizes[wedges.index(wedge)] / total * 100
        annot.set_text(f"{label}: {percent:.1f}%")
        annot.get_bbox_patch().set_facecolor('lightblue')
        annot.set_fontsize(12)

    # Hàm xử lý hover
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

    # Tạo canvas để nhúng biểu đồ vào trong Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

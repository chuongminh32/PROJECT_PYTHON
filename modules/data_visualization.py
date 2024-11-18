import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors # Thư viện hỗ trợ hiển thị thông tin chi tiết khi hover qua các điểm trên biểu đồ
from mpl_toolkits.mplot3d import Axes3D

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
    
def plot_grade_btn(FILE_PATH):
    plt.close('all')
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
    plt.show()



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
    wedges, _, autotexts = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p >= 10 else '', startangle=140)

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

# Hàm vẽ biểu đồ phân bố quốc gia - btn
def plot_country_btn(FILE_PATH):
    plt.close('all')

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
    wedges, _, autotexts = ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p >= 10 else '', startangle=140)

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

    plt.show()


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

# Hàm vẽ biểu đồ phân bố độ tuổi
def plot_age_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)

    # Vẽ histogram độ tuổi
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['age'], bins=5)
    ax.set_title("Biểu đồ phân bố độ tuổi")
    ax.set_xlabel("Tuổi")
    ax.set_ylabel("Mật độ")
    ax.set_xticks([15, 19, 20, 21, 22, 23, 24, 25, 26, 30])
    plt.tight_layout()

    plt.show()


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

# Hàm vẽ biểu đồ tỉ lệ nam nữ
def plot_gender_btn(FILE_PATH):
    
    plt.close('all')
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

    plt.show()



#  Vẽ biểu đồ phân tán giữa Tuổi và Điểm số học tập
def plot_point_old(FILE_PATH, frame):
    data = pd.read_csv(FILE_PATH) # Đọc dữ liệu từ file CSV
    fig = plt.Figure(figsize=(10, 6)) # Khởi tạo figure
    ax = fig.add_subplot(111) # Khởi tạo subplot

    # Vẽ các điểm phân tán với độ trong suốt và kích thước điểm
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        ax.scatter(data['age'], data[mon], label=mon, alpha=0.7, s=50)  # alpha: độ trong suốt, s: kích thước điểm

    ax.set_xlabel('Tuổi', fontsize=12) # Đặt nhãn trục Ox
    ax.set_ylabel('Điểm số', fontsize=12) # Đặt nhãn trục Oy
    ax.set_title('Biểu đồ phân tán của Tuổi và Điểm học tập', fontsize=14) # Đặt tiêu đề

    # Sử dụng mplcursors để hiển thị thông tin chi tiết khi hover qua các điểm
    mplcursors.cursor(ax, hover=True) 

    # Tích hợp biểu đồ vào Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)  # Tạo canvas để nhúng biểu đồ vào trong Tkinter
    canvas.draw() # Vẽ biểu đồ
    canvas.get_tk_widget().pack(fill="both", expand=True) # Hiển thị biểu đồ

#  Vẽ biểu đồ phân tán giữa Tuổi và Điểm số học tập
def plot_point_old_btn(FILE_PATH):
    plt.close('all')  # Đóng tất cả các biểu đồ trước đó
    data = pd.read_csv(FILE_PATH)  # Đọc dữ liệu từ file CSV
    
    # Tạo figure và axis
    fig, ax = plt.subplots(figsize=(10, 6))  # Tạo figure và axis
    
    # Vẽ các điểm phân tán cho từng môn học
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        ax.scatter(data['age'], data[mon], label=mon, alpha=0.7, s=50)  # alpha: độ trong suốt, s: kích thước điểm

    # Đặt nhãn trục Ox và Oy
    ax.set_xlabel('Tuổi', fontsize=12)
    ax.set_ylabel('Điểm số', fontsize=12)
    
    # Đặt tiêu đề biểu đồ
    ax.set_title('Biểu đồ phân tán của Tuổi và Điểm học tập', fontsize=14)
    
    # Hiển thị chú thích (legend) ở ngoài biểu đồ
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Môn học")

    # Sử dụng mplcursors để hiển thị thông tin chi tiết khi hover qua các điểm
    mplcursors.cursor(ax, hover=True) 

    # Hiển thị biểu đồ
    plt.tight_layout()  # Đảm bảo không bị cắt khi hiển thị
    plt.show()



#  Vẽ biểu đồ thanh so sánh Đánh giá Hồ sơ cá nhân
def plot_personal(FILE_PATH, frame):
    data = pd.read_csv(FILE_PATH)
    fig = plt.Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    diem_trung_binh = data[['portfolio.rating', 'coverletter.rating', 'refletter.rating']].mean()
    bars = diem_trung_binh.plot(kind='bar', color=['#4CAF50', '#FF5722', '#2196F3'], ax=ax)
    ax.set_xlabel('Loại Đánh Giá')
    ax.set_ylabel('Điểm Trung Bình')
    ax.set_title('Biểu đồ thanh của Điểm Đánh Giá Cá Nhân Trung Bình')
    ax.set_xticklabels(diem_trung_binh.index, rotation=0)  # Đặt nhãn trục Ox nằm ngang

    # Không hiển thị chú thích mặc định, nhưng thêm thông tin vào các thanh
    for bar in bars.patches:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', 
                ha='center', va='bottom', fontsize=10)

    # Tích hợp biểu đồ vào Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

#  Vẽ biểu đồ thanh so sánh Đánh giá Hồ sơ cá nhân
def plot_personal_btn(FILE_PATH):
  # Đọc dữ liệu từ file CSV
    data = pd.read_csv(FILE_PATH)
    
    # Đóng tất cả các biểu đồ trước đó
    plt.close('all')
    
    # Tạo figure và axis bằng plt.subplots()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Tính điểm trung bình của các đánh giá
    diem_trung_binh = data[['portfolio.rating', 'coverletter.rating', 'refletter.rating']].mean()
    
    # Vẽ biểu đồ thanh 2D
    bars = diem_trung_binh.plot(kind='bar', color=['#4CAF50', '#FF5722', '#2196F3'], ax=ax)
    
    # Đặt nhãn cho trục X, Y và tiêu đề
    ax.set_xlabel('Loại Đánh Giá')
    ax.set_ylabel('Điểm Trung Bình')
    ax.set_title('Biểu đồ Thanh của Điểm Đánh Giá Cá Nhân Trung Bình')
    
    # Đặt nhãn trục X nằm ngang
    ax.set_xticklabels(diem_trung_binh.index, rotation=0)
    
    # Thêm giá trị vào các thanh
    for bar in bars.patches:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', 
                ha='center', va='bottom', fontsize=10)

    # Hiển thị biểu đồ
    plt.tight_layout()  # Đảm bảo không bị cắt khi hiển thị
    plt.show()



# Vẽ biểu đồ phân tán liên hệ giữa Điểm các môn học và Đánh giá năng lực cá nhân
def plot_point_rating(FILE_PATH, frame):
   
    data = pd.read_csv(FILE_PATH)
    fig = plt.Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    # Vẽ biểu đồ phân tán cho từng môn học
    scatter_plots = []
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        scatter_plots.append(ax.scatter(data[mon], data['portfolio.rating'], label=f'{mon} và Đánh Giá Hồ Sơ', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['coverletter.rating'], label=f'{mon} và Đánh Giá Thư Xin Việc', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['refletter.rating'], label=f'{mon} và Đánh Giá Thư Giới Thiệu', alpha=0.6))

    ax.set_xlabel('Điểm số')
    ax.set_ylabel('Đánh giá')
    ax.set_title('Biểu đồ phân tán của Điểm và Đánh giá Cá Nhân')

    # Tích hợp chức năng hover để hiển thị chú thích
    mplcursors.cursor(scatter_plots, hover=True)

    # Tích hợp biểu đồ vào Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def plot_point_rating_btn(FILE_PATH):
    # Đóng tất cả các biểu đồ trước đó
    plt.close('all')

    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(FILE_PATH)

    # Tạo hình và trục vẽ
    fig, ax = plt.subplots(figsize=(10, 6))

    # Vẽ biểu đồ phân tán cho từng môn học và loại đánh giá
    scatter_plots = []
    for mon in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']:
        # Vẽ các điểm cho từng môn học và từng loại đánh giá
        scatter_plots.append(ax.scatter(data[mon], data['portfolio.rating'], label=f'{mon} - Hồ Sơ', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['coverletter.rating'], label=f'{mon} - Thư Xin Việc', alpha=0.6))
        scatter_plots.append(ax.scatter(data[mon], data['refletter.rating'], label=f'{mon} - Thư Giới Thiệu', alpha=0.6))

    # Thiết lập các thông số của biểu đồ
    ax.set_xlabel('Điểm số')
    ax.set_ylabel('Đánh giá')
    ax.set_title('Biểu đồ phân tán của Điểm và Đánh giá Cá Nhân')

    # Hiển thị chú thích khi hover chuột lên các điểm dữ liệu
    mplcursors.cursor(scatter_plots, hover=True)

    # Hiển thị chú thích ngoài biểu đồ
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Hiển thị biểu đồ
    plt.tight_layout()  # Đảm bảo các thành phần không bị cắt
    plt.show()


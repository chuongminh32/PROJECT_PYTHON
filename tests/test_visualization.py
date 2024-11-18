import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors
import tkinter as tk



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

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    detail_btn = tk.Button(button_frame, text="Detail", command=plt.show, width=10, height=2)
    detail_btn.pack(side="left", padx=10, pady=10)
    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
button_frame = tk.Frame(root)
button_frame.pack()

plot_grade("data/data_clean.csv", frame)
root.mainloop()
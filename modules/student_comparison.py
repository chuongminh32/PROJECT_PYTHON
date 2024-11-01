import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Hàm tạo heatmap cho hai học sinh dựa trên id
def comparison_heatmap(FILE_PATH, id1, id2):
    # Lọc hai học sinh dựa trên id
    df = pd.read_csv(FILE_PATH)
    df_filtered = df[df['id'].isin([id1, id2])]

    # Kiểm tra nếu có đủ hai học sinh để so sánh
    if len(df_filtered) != 2:
        print("ID không tồn tại. Vui lòng nhập ID hợp lệ có trong dữ liệu.")
        return

    # Lấy các cột cần cho heatmap
    ratings_cols = ["english.grade", "math.grade", "sciences.grade", "language.grade",
                    "portfolio.rating", "coverletter.rating", "refletter.rating"]

    # Chuyển đổi dữ liệu để tiện cho heatmap
    df_comparison = df_filtered[ratings_cols].T
    df_comparison.columns = df_filtered['name'].values  # Đặt tên cột theo tên học sinh

    # Vẽ heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(df_comparison, cmap="YlGnBu", aspect='0.3')
    plt.colorbar()
    # Thêm các annotations vào từng ô của heatmap
    for i in range(df_comparison.shape[0]):
        for j in range(df_comparison.shape[1]):
            plt.text(j, i, f'{df_comparison.iloc[i, j]:.2f}', ha='center', va='center', color='k')
    plt.title(f"So sánh {df_filtered.iloc[0]['name']} và {df_filtered.iloc[1]['name']}")
    plt.xlabel("Students")
    plt.ylabel("Grades / Ratings")
    # Thêm label cho từng dòng và cột
    plt.xticks(np.arange(df_comparison.shape[1]), df_comparison.columns, ha='center')
    plt.yticks(np.arange(df_comparison.shape[0]), df_comparison.index)
    plt.show()

# Sử dụng hàm với ID của hai học sinh, ví dụ ID 0 và 1
#comparison_heatmap('data/data_demo.csv', 0, 1)
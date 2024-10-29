import matplotlib.pyplot as plt
import seaborn as sns

# Hàm tạo heatmap cho hai học sinh dựa trên id
def comparison_heatmap(df, id1, id2):
    # Lọc hai học sinh dựa trên id
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
    sns.heatmap(df_comparison, annot=True, cmap="coolwarm", cbar=True, linewidths=0.5)
    plt.title(f"Comparison Heatmap between {df_filtered.iloc[0]['name']} and {df_filtered.iloc[1]['name']}")
    plt.xlabel("Students")
    plt.ylabel("Grades / Ratings")
    plt.show()

# Sử dụng hàm với ID của hai học sinh, ví dụ ID 0 và 1
#comparison_heatmap(df, 0, 1)
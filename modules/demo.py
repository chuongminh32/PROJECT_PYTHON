import pandas as pd

def sort_csv_by_id(input_file, output_file):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv("data/student-dataset.csv")
    
    # Sắp xếp dữ liệu tăng dần theo cột 'id'
    df_sorted = df.sort_values(by='id', ascending=True)
    
    # Lưu dữ liệu đã sắp xếp vào file CSV mới
    df_sorted.to_csv(output_file, index=False)
    print(f"Dữ liệu đã được sắp xếp và lưu vào {output_file}")

# Sử dụng hàm
input_file = 'data/student-dataset.csv'  # Tên file CSV gốc
output_file = 'data/student-dataset.csv'  # Tên file CSV đầu ra
sort_csv_by_id(input_file, output_file)

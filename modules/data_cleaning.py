import pandas as pd
import csv
from math import ceil

def handle_missing_value(FILE_PATH):
    """Thay thế dữ liệu bị thiếu thành 0.0 (float)
    - Gọi hàm này ở cuối để chạy demo: fill_missing_value("data\data_demo.csv")
    - Hàm xử lý dữ liệu ĐIỂM bị thiếu thành 0.0 và xóa hàng khi giá trị tại cột "SBD" bị rỗng
    """
    df = pd.read_csv(FILE_PATH)
    # Xóa cột Ethic.group
    result_df = df.drop('ethnic.group', axis=1)

    # Xóa hàng không có id
    result_df = result_df.dropna(subset='id')
    
    # Fill ô không có thông tin thành "No infor" (String)
    colums_str = ['name','nationality','city','gender']
    result_df[colums_str] = result_df[colums_str].fillna('No infor')

    # Fill ô không có tuổi thành trung bình tuổi của cột đó (int)
    # ave_age = ceil(result_df['age'].mean())
    ave_age = ceil(result_df['age'].mean())
    result_df['age'] = result_df['age'].fillna(ave_age)

    # Fill ô không có điểm thành 0.0 (Float)
    columns_float = ['latitude', 'longitude','english.grade','math.grade','sciences.grade','language.grade']
    result_df[columns_float] = result_df[columns_float].fillna(0.0)

    # Fill ô không có rating thành 0 (Int)
    colums_int = ['portfolio.rating','coverletter.rating','refletter.rating']
    result_df[colums_int] = result_df[colums_int].fillna(0)

    # Lưu dữ liệu đã được làm sạch vào file
    save_to_cleaned_data_file("data\data_clean.csv", result_df)
    return 1

def remove_duplicates(FILE_PATH):
    """Loại bỏ các giá trị trùng lặp và ghi dữ liệu mới vào file "data_clean.csv"
    - Gọi hàm này ở cuối để chạy demo: remove_duplicates("data\data_demo.csv")
    - df --> đọc file dữ liệu
    - resule_df --> chứa kq đã loại bỏ giá trị trùng lặp
    """
    df = pd.read_csv(FILE_PATH)

    result_df = df.drop_duplicates(subset=['id'])
    save_to_cleaned_data_file("data\data_clean.csv", result_df)
    return 1

def correct_formatting(FILE_PATH):
    """Sửa định dạng dữ liệu"""
    result_df = pd.read_csv(FILE_PATH)

    # Convert cột age thành unsigned int    
    result_df['age'] = pd.Series(result_df['age'], dtype=pd.Int64Dtype())
    result_df['age'] = abs(result_df['age'].values)

    # Convert các cột trong list sau thành unsigned int <= 5
    colums_int = ['portfolio.rating','coverletter.rating','refletter.rating']
    result_df[colums_int] = abs(result_df[colums_int].values % 6)

    save_to_cleaned_data_file("data\data_clean.csv",result_df)
    return 1

def save_to_cleaned_data_file(FILEPATH, result_df):
    """Hàm này để lưu các giá trị sau khi làm sạch vào file "data_clean.csv"
    Hàm đọc dữ liệu từ giá trị đã được làm sạch của df (giá trị này được gán vào result_df)
    """
    with open(FILEPATH,'w',encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result_df.head())
        writer.writerows(result_df.values)

"""
Lời gọi hàm dưới đây chỉ chạy demo, xử lý dữ liệu trong file demo và ghi vào file cleaned
Vì vậy, khi truyền vào tham số "FILE_PATH", lời gọi đầu truyền "data_demo.csv", từ lời gọi
thứ 2, 3, 4 truyền "data\data_clean.csv"
"""
remove_duplicates("data\data_demo.csv") #xóa comment để chạy demo
handle_missing_value("data\data_clean.csv") #xóa comment để chạy demo
correct_formatting("data\data_clean.csv")
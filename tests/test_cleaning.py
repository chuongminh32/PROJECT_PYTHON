import pandas as pd
import numpy as np
import csv
from math import ceil

def test_handle_missing_value(FILE_PATH, FILE_CLEAN_DATA_PATH):
    """Thay thế dữ liệu bị thiếu thành 0.0 (float)
    - Gọi hàm này ở cuối để chạy demo: handle_missing_value("data_demo.csv",'data_clean_demo.csv')
    """
    df = pd.read_csv(FILE_PATH)
    # print(df.info())
    print(df.loc[:,['id','name','age','refletter.rating']])

    #Loại bỏ record khi không chứa id
    df = df.dropna(subset=['id'])

    # Điền dữ liệu chuỗi bị thiếu bằng 'No infor'
    columns_str = ['name', 'nationality', 'city', 'gender']
    for col in columns_str:
        if col in df.columns:
            df[col] = df[col].fillna('No infor')

    # Điền tuổi bị thiếu bằng tuổi trung bình, làm tròn lên
    if 'age' in df.columns:
        ave_age = ceil(df['age'].mean())
        df['age'] = df['age'].fillna(ave_age)

    # Điền điểm số bị thiếu bằng 0.0
    columns_float = ['latitude', 'longitude', 'english.grade', 'math.grade', 'sciences.grade', 'language.grade']
    for col in columns_float:
        if col in df.columns:
            df[col] = df[col].fillna(0.0)

    # Điền đánh giá bị thiếu bằng 0
    columns_int = ['portfolio.rating', 'coverletter.rating', 'refletter.rating']
    for col in columns_int:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    # print(result_df)
    save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, df)
    

    result_df = pd.read_csv(FILE_CLEAN_DATA_PATH)
    print(result_df.loc[:,['id','name','age','refletter.rating']])
    return 1

def remove_duplicates(FILE_PATH, FILE_CLEAN_DATA_PATH):
    """Loại bỏ các giá trị trùng lặp và ghi dữ liệu mới vào file "cleaned_data.csv"
    - Gọi hàm này ở cuối để chạy demo: remove_duplicates("data\dataset_demo.csv")
    - df --> đọc file dữ liệu
    - resule_df --> chứa kq đã loại bỏ giá trị trùng lặp
    """
    df = pd.read_csv(FILE_PATH)
    df = df.drop_duplicates(subset=['id'])
    save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, df)
    # print(result_df)
    return 1


def correct_formatting(FILE_PATH):
    """Sửa định dạng dữ liệu, làm cho cột 'age' và các cột đánh giá thành số nguyên không âm."""
    df = pd.read_csv(FILE_PATH)
    print(df.dtypes)
   # Chuyển đổi 'age' thành số nguyên dương
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)
        df['age'] = abs(df['age'])

    if 'id' in df.columns:
        df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)

    # Đảm bảo các cột đánh giá là số nguyên không âm từ 0 đến 5
    columns_int = ['portfolio.rating', 'coverletter.rating', 'refletter.rating']
    for col in columns_int:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
            df[col] = df[col].apply(lambda x: x if 0 <= x <= 5 else 0)

    print(df.dtypes)

    save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, df)

    return df

def save_to_cleaned_data_file(FILEPATH, result_df):
    """Hàm này để lưu các giá trị sau khi làm sạch vào file "cleaned_data.csv"
    Hàm đọc dữ liệu từ giá trị đã được làm sạch của df (giá trị này được gán vào result_df)
    """
    with open(FILEPATH,'w',encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result_df.head())
        writer.writerows(result_df.values)

"""
Gọi hàm dưới đây chỉ chạy demo, xử lý dữ liệu trong file demo và ghi vào file cleaned
Vì vậy, khi truyền vào tham số "FILE_PATH", lời gọi đầu truyền "dataset_demo.csv", từ lời gọi
thứ 2, 3, 4 truyền FILE_CLEAN_DATA_PATH
"""



# Chạy demo
if __name__ == "__main__":
    FILE_CLEAN_DATA_PATH = str('tests/data_clean_demo.csv')
    # Đường dẫn đến file dataset_demo.csv
    dataset_path = str('tests/data_demo.csv')
    
    # Bước 1: Xử lý giá trị bị thiếu
    df_no_missing = test_handle_missing_value(dataset_path, FILE_CLEAN_DATA_PATH)
    
    # # Bước 2: Xử lý các giá trị bị trùng lặp
    # remove_dup = remove_duplicates(dataset_path,FILE_CLEAN_DATA_PATH)
    
    # Bước 3: Sửa định dạng dữ liệu
    df_corrected = correct_formatting(FILE_CLEAN_DATA_PATH)
    
    # Lưu dữ liệu đã sửa định dạng
    # save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, df_corrected)

# remove_duplicates("data\dataset_demo.csv") #xóa comment để chạy demo
# handle_missing_value(FILE_CLEAN_DATA_PATH) #xóa comment để chạy demo


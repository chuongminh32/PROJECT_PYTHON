# import pandas as pd
# import os

# def handle_missing_value(file_path):
#     """Thay thế dữ liệu bị thiếu thành 0.0 (float)"""
#     df = pd.read_csv(file_path)
#     result_df = df.dropna(subset=['sbd'])  # Xóa hàng có giá trị SBD bị rỗng
#     result_df = result_df.fillna(0.0)       # Thay thế các giá trị thiếu thành 0.0
#     save_to_cleaned_data_file(, result_df)  # Lưu dữ liệu đã làm sạch
#     return result_df  # Trả về DataFrame đã xử lý

# def remove_duplicates(file_path):
#     """Loại bỏ các giá trị trùng lặp và ghi dữ liệu mới vào file "cleaned_data.csv"."""
#     df = pd.read_csv(file_path)
#     result_df = df.drop_duplicates(subset=['sbd'])  # Loại bỏ hàng trùng lặp theo SBD
#     save_to_cleaned_data_file(, result_df)  # Lưu dữ liệu đã loại bỏ trùng lặp
#     return result_df  # Trả về DataFrame đã xử lý

# def correct_formatting(df):
#     """Sửa định dạng dữ liệu, đảm bảo SBD là chuỗi số liên tiếp và các điểm thi là số."""
#     # Chuyển đổi SBD thành chuỗi và loại bỏ bất kỳ giá trị không hợp lệ
#     df['sbd'] = df['sbd'].astype(str).str.replace('.0', '', regex=False)  # Đảm bảo không có ".0"
    
#     columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
#                'lich_su', 'dia_li', 'gdcd']
#     df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')  # Chuyển đổi các điểm thi thành số
#     return df

# def save_to_cleaned_data_file(filepath, result_df):
#     """Hàm này để lưu các giá trị sau khi làm sạch vào file "cleaned_data.csv"."""
#     result_df.to_csv(filepath, index=False, encoding='utf-8')  # Sử dụng pandas để lưu dữ liệu



import pandas as pd
import numpy as np
import csv

def handle_missing_value(FILE_PATH, FILE_CLEAN_DATA_PATH):
    """Thay thế dữ liệu bị thiếu thành 0.0 (float)
    - Gọi hàm này ở cuối để chạy demo: fill_missing_value("data\dataset_demo.csv")
    - Hàm xử lý dữ liệu ĐIỂM bị thiếu thành 0.0 và xóa hàng khi giá trị tại cột "SBD" bị rỗng
    """
    df = pd.read_csv(FILE_PATH)
    result_df = df.dropna(subset=['sbd'])
    result_df = result_df.fillna(0.0)
    # print(result_df)
    save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, result_df)
    return 1

def remove_duplicates(FILE_PATH, FILE_CLEAN_DATA_PATH):
    """Loại bỏ các giá trị trùng lặp và ghi dữ liệu mới vào file "cleaned_data.csv"
    - Gọi hàm này ở cuối để chạy demo: remove_duplicates("data\dataset_demo.csv")
    - df --> đọc file dữ liệu
    - resule_df --> chứa kq đã loại bỏ giá trị trùng lặp
    """
    df = pd.read_csv(FILE_PATH)
    result_df = df.drop_duplicates(subset=['sbd'])
    save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, result_df)
    # print(result_df)
    return 1

# def correct_formatting(df):
#     """Sửa định dạng dữ liệu, đảm bảo SBD là chuỗi số liên tiếp và các điểm thi là số."""
#     # Chuyển đổi SBD thành chuỗi và loại bỏ bất kỳ giá trị không hợp lệ
#     df['sbd'] = df['sbd'].astype(str).str.replace('.0', '', regex=False)  # Đảm bảo không có ".0"
    
#     columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
#                'lich_su', 'dia_li', 'gdcd']
#     df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')  # Chuyển đổi các điểm thi thành số
#     return df

def correct_formatting(df):
    """Sửa định dạng dữ liệu, đảm bảo SBD là chuỗi số liên tiếp và các điểm thi là số."""
    # Chắc chắn rằng cột 'sbd' tồn tại
    if 'sbd' in df.columns:
        # Thay thế giá trị NaN bằng một giá trị mặc định (nếu cần thiết)
        df['sbd'] = df['sbd'].fillna('')  # Hoặc bạn có thể thay bằng '0'
        df['sbd'] = df['sbd'].astype(str).str.replace('.0', '', regex=False)  # Đảm bảo không có ".0"
    else:
        print("Cột 'sbd' không tồn tại trong DataFrame.")

    # Xác định các cột điểm
    columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
               'lich_su', 'dia_li', 'gdcd']
    
    # Chuyển đổi các điểm thi thành số, xử lý NaN nếu cần
    for column in columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors='coerce')  # Chuyển đổi các điểm thi thành số
        else:
            print(f"Cột '{column}' không tồn tại trong DataFrame.")
    
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
    FILE_CLEAN_DATA_PATH = r"G:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\data\cleaned_data.csv"
    # Đường dẫn đến file dataset_demo.csv
    dataset_path = r"G:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\data\dataset_demo.csv"  # Đường dẫn tuyệt đối tới file dữ liệu nguồn
    print("Data source path:", dataset_path)
    
    # Bước 1: Xóa các bản ghi trùng lặp
    df_no_duplicates = remove_duplicates(dataset_path, FILE_CLEAN_DATA_PATH)
    
    # Bước 2: Xử lý các giá trị bị thiếu
    df_cleaned = handle_missing_value(dataset_path, FILE_CLEAN_DATA_PATH)
    
    # Bước 3: Sửa định dạng dữ liệu
    df_corrected = correct_formatting(df_cleaned)
    
    # Lưu dữ liệu đã sửa định dạng
    save_to_cleaned_data_file(FILE_CLEAN_DATA_PATH, df_corrected)

# remove_duplicates("data\dataset_demo.csv") #xóa comment để chạy demo
# handle_missing_value(FILE_CLEAN_DATA_PATH) #xóa comment để chạy demo


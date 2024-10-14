print("Thực hiện các thao tác cleaning trên tập dữ liệu") 


# code demo 
import pandas as pd
import csv

def remove_missing_values(df):
    """Loại bỏ các giá trị thiếu"""

    return df.dropna()

def remove_duplicates(FILE_PATH):
    """Loại bỏ các giá trị trùng lặp và ghi dữ liệu mới vào file "cleaned_data.csv"
    - Gọi hàm này ở cuối để chạy demo: remove_duplicates("data\dataset_demo.csv")
    - df --> đọc file dữ liệu
    - resule_df --> chứa kq đã loại bỏ giá trị trùng lặp
    """
    df = pd.read_csv(FILE_PATH)
    result_df = df.drop_duplicates()
    save_to_cleaned_data_file("data\cleaned_data.csv", result_df)
    # print(result_df)
    return result_df

def correct_formatting(df):
    """Sửa định dạng dữ liệu"""
    columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
               'lich_su', 'dia_li', 'gdcd']
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    return df

def save_to_cleaned_data_file(FILEPATH, result_df):
    """Hàm này để lưu các giá trị sau khi làm sạch vào file "cleaned_data.csv"
    Hàm đọc dữ liệu từ giá trị đã được làm sạch của df (giá trị này được gán vào result_df)
    """
    with open(FILEPATH,'w',encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result_df.head())
        writer.writerows(result_df.values)

# remove_duplicates("data\dataset_demo.csv") #xóa comment để chạy demo
import pandas as pd
import csv

def handle_missing_value(FILE_PATH):
    """Thay thế dữ liệu bị thiếu thành 0.0 (float)
    - Gọi hàm này ở cuối để chạy demo: fill_missing_value("data\dataset_demo.csv")
    - Hàm xử lý dữ liệu ĐIỂM bị thiếu thành 0.0 và xóa hàng khi giá trị tại cột "SBD" bị rỗng
    """
    df = pd.read_csv(FILE_PATH)
    #Xóa hàng không có số báo danh
    result_df = df.dropna(subset=['sbd'])

    #Fill ô không có điểm thành 0.0
    result_df = result_df.fillna(0.0)
    save_to_cleaned_data_file("data\cleaned_data.csv", result_df)
    return 1

def remove_duplicates(FILE_PATH):
    """Loại bỏ các giá trị trùng lặp và ghi dữ liệu mới vào file "cleaned_data.csv"
    - Gọi hàm này ở cuối để chạy demo: remove_duplicates("data\dataset_demo.csv")
    - df --> đọc file dữ liệu
    - resule_df --> chứa kq đã loại bỏ giá trị trùng lặp
    """
    df = pd.read_csv(FILE_PATH)

    result_df = df.drop_duplicates(subset=['sbd'])
    save_to_cleaned_data_file("data\cleaned_data.csv", result_df)
    return 1

<<<<<<< HEAD
def correct_formatting(df):
    """Sửa định dạng dữ liệu, đảm bảo SBD là chuỗi số liên tiếp và các điểm thi là số."""
    # Chuyển đổi SBD thành chuỗi và loại bỏ bất kỳ giá trị không hợp lệ
    df['sbd'] = df['sbd'].astype(str).str.replace('.0', '', regex=False)  # Đảm bảo không có ".0"
    
    columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
               'lich_su', 'dia_li', 'gdcd']
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')  # Chuyển đổi các điểm thi thành số
    return df
=======
def correct_formatting(FILE_PATH):
    """Sửa định dạng dữ liệu"""

    columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
               'lich_su', 'dia_li', 'gdcd']
    df = pd.read_csv(FILE_PATH)
    # result_df = df[columns].apply(pd.to_numeric, errors='coerce')
    # result_df 
    # print(df)
    # df['sbd'] = df['sbd'].apply(pd.to_numeric(downcast='integer'))
    # result_df = df[columns].apply(pd.to_numeric, errors='coerce')
    # save_to_cleaned_data_file("data\cleaned_data.csv",result_df)
    return 1
>>>>>>> efe77949c2a27884d325d070dcae20a3bd9738af

def save_to_cleaned_data_file(FILEPATH, result_df):
    """Hàm này để lưu các giá trị sau khi làm sạch vào file "cleaned_data.csv"
    Hàm đọc dữ liệu từ giá trị đã được làm sạch của df (giá trị này được gán vào result_df)
    """
    with open(FILEPATH,'w',encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result_df.head())
        writer.writerows(result_df.values)

"""
Lời gọi hàm dưới đây chỉ chạy demo, xử lý dữ liệu trong file demo và ghi vào file cleaned
Vì vậy, khi truyền vào tham số "FILE_PATH", lời gọi đầu truyền "dataset_demo.csv", từ lời gọi
thứ 2, 3, 4 truyền "data\cleaned_data.csv"
"""
# remove_duplicates("data\dataset_demo.csv") #xóa comment để chạy demo
# handle_missing_value("data\cleaned_data.csv") #xóa comment để chạy demo
# correct_formatting("data\dataset_demo.csv")
print("Thực hiện các thao tác CRUD trên tập dữ liệu") 

# # file_path = "G:/NamII_HK1/PY/PROJECT/PROJECT_PYTHON/data/dataset.csv" -> demo
# code demo 
import pandas as pd

# Đọc dữ liệu từ CSV
def read_data(file_path):
    try:
        df = pd.read_csv("file_path")
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

# Thêm dữ liệu mới vào DataFrame
def add_data(df, new_row):
     df = df.append(new_row, ignore_index=True)
     return df

# Cập nhật dữ liệu trong DataFrame theo SBD
def update_data(df, sbd, updated_row):
    index = df[df['sbd'] == sbd].index
    if not index.empty:
        df.loc[index, :] = updated_row
    else:
        print(f"Không tìm thấy SBD {sbd}")
    return df

# Xóa một dòng dữ liệu theo SBD
def delete_data(df, sbd):
    df = df[df['sbd'] != sbd]
    return df

# Lưu DataFrame trở lại file CSV
def save_data(df, file_path):
    df.to_csv(file_path, index=False)



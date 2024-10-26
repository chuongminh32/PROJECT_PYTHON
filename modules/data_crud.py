import pandas as pd

def read_data(file_path):
    """
    Đọc dữ liệu từ file CSV.
    """
    try:
        df = pd.read_csv(file_path, delimiter=',')
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

def add_data(df, new_row):
    """
    Thêm hàng mới vào DataFrame.
    """
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    return df

def update_data(df, id, updated_row):
    """
    Cập nhật dữ liệu theo ID.
    """
    index = df[df['id'] == id].index
    if not index.empty:
        for key in updated_row:
            if key in df.columns:
                df.loc[index, key] = updated_row[key]
    else:
        print(f"Không tìm thấy ID {id}")
    return df

def delete_data(df, id):
    """
    Xóa hàng dữ liệu theo ID.
    """
    index = df[df['id'] == id].index
    if not index.empty:
        df = df.drop(index)
        print(f"Đã xóa ID {id}")
    else:
        print(f"Không tìm thấy ID {id}")
    return df

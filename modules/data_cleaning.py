import pandas as pd
from math import ceil
from pathlib import Path
def handle_missing_value(df):
    """Thay thế dữ liệu bị thiếu bằng các giá trị mặc định và trả về DataFrame đã được làm sạch.
    - Điền điểm số bị thiếu bằng 0.0, dữ liệu nhân khẩu học bị thiếu bằng 'No infor',
      và thay thế tuổi bị thiếu bằng tuổi trung bình.
    - Xóa các hàng có giá trị 'id' bị thiếu.
    """
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

    return df

def remove_duplicates(df):
    """Loại bỏ các hàng trùng lặp dựa trên 'id' và trả về DataFrame đã được làm sạch."""
    df = df.drop_duplicates(subset=['id'])
    return df

def correct_formatting(df):
    """Sửa định dạng dữ liệu, làm cho cột 'age' và các cột đánh giá thành số nguyên không âm."""
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

    # df['coverletter.rating'] = pd.to_numeric(df['coverletter.rating'], errors='coerce').fillna(0).astype(int)
    # df['coverletter.rating'] = df['coverletter.rating'].apply(lambda x: x if 0 <= x <= 5 else 0)
    return df

def save_to_cleaned_data_file(filepath, result_df):
    """Lưu dữ liệu được làm sạch vào dile clean_data.csv."""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(filepath, index=False, encoding="utf-8")

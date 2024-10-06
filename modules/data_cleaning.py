print("Thực hiện các thao tác cleaning trên tập dữ liệu") 


# code demo 
import pandas as pd

def remove_missing_values(df):
    """Loại bỏ các giá trị thiếu"""
    return df.dropna()

def remove_duplicates(df):
    """Loại bỏ các giá trị trùng lặp"""
    return df.drop_duplicates()

def correct_formatting(df):
    """Sửa định dạng dữ liệu"""
    columns = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
               'lich_su', 'dia_li', 'gdcd']
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    return df

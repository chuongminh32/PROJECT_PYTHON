# print("Các hàm tiện ích dùng chung cho nhiều module") 
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)



# Hàm kiểm tra sinh viên có tồn tại hay không
def student_exists(df, sbd):
    return not df[df['sbd'] == sbd].empty

# Hàm tính tổng điểm cho một sinh viên
def calculate_total_score(student_row):
    return student_row[['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
                        'lich_su', 'dia_li', 'gdcd']].sum(axis=1).values[0]

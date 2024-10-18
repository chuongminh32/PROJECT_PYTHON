import pandas as pd

# Đọc dữ liệu từ tập tin CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Tìm sinh viên có tổng điểm 3 môn Toán, Lý, Hóa cao nhất
def find_highest_total_score_tlh(df):
    df['total_tlh'] = df[['toan', 'vat_li', 'hoa_hoc']].sum(axis=1)
    highest_tlh = df.loc[df['total_tlh'].idxmax()]
    return highest_tlh[['sbd', 'toan', 'vat_li', 'hoa_hoc', 'total_tlh']]

# Tìm sinh viên có tổng điểm 3 môn Toán, Lý, Anh cao nhất
def find_highest_total_score_tla(df):
    df['total_tla'] = df[['toan', 'vat_li', 'ngoai_ngu']].sum(axis=1)
    highest_tla = df.loc[df['total_tla'].idxmax()]
    return highest_tla[['sbd', 'toan', 'vat_li', 'ngoai_ngu', 'total_tla']]

# Tìm sinh viên có điểm Toán cao nhất
def find_highest_score_math(df):
    highest_math = df.loc[df['toan'].idxmax()]
    return highest_math[['sbd', 'toan']]

# Tìm sinh viên có điểm Anh (Ngoại ngữ) cao nhất
def find_highest_score_english(df):
    highest_english = df.loc[df['ngoai_ngu'].idxmax()]
    return highest_english[['sbd', 'ngoai_ngu']]

# Ví dụ sử dụng các chức năng
if __name__ == "__main__":
    data_file = '../data/cleaned_data.csv'
    data = load_data(data_file)
    
    # Tìm sinh viên có tổng điểm Toán, Lý, Hóa cao nhất
    highest_tlh = find_highest_total_score_tlh(data)
    print("Sinh viên có tổng điểm Toán, Lý, Hóa cao nhất:")
    print(highest_tlh)
    
    # Tìm sinh viên có tổng điểm Toán, Lý, Anh cao nhất
    highest_tla = find_highest_total_score_tla(data)
    print("\nSinh viên có tổng điểm Toán, Lý, Anh cao nhất:")
    print(highest_tla)
    
    # Tìm sinh viên có điểm Toán cao nhất
    highest_math = find_highest_score_math(data)
    print("\nSinh viên có điểm Toán cao nhất:")
    print(highest_math)
    
    # Tìm sinh viên có điểm Ngoại ngữ (Anh) cao nhất
    highest_english = find_highest_score_english(data)
    print("\nSinh viên có điểm Ngoại ngữ (Anh) cao nhất:")
    print(highest_english)

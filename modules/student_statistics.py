import pandas as pd

# Đọc dữ liệu từ tập tin CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Tính toán điểm trung bình của tất cả các môn học
def calculate_average_score(df):
    subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
                'lich_su', 'dia_li', 'gdcd']
    df['average_score'] = df[subjects].mean(axis=1)
    return df[['sbd', 'average_score']]

# Tính điểm trung bình của từng môn học trong toàn bộ dataset
def calculate_subject_averages(df):
    subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
                'lich_su', 'dia_li', 'gdcd']
    subject_averages = df[subjects].mean()
    return subject_averages

# Ví dụ sử dụng
if __name__ == "__main__":
    data_file = '../data/cleaned_data.csv'
    data = load_data(data_file)
    
    # Tính điểm trung bình của từng sinh viên
    average_scores = calculate_average_score(data)
    print("Điểm trung bình của mỗi sinh viên:")
    print(average_scores)
    
    # Tính điểm trung bình của từng môn
    subject_averages = calculate_subject_averages(data)
    print("Điểm trung bình của từng môn:")
    print(subject_averages)

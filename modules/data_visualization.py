print("Trục quan hóa data")

# code demo 
import matplotlib.pyplot as plt

def plot_average_scores(df):
    """Vẽ biểu đồ điểm trung bình các môn"""
    subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 
                'lich_su', 'dia_li', 'gdcd']
    averages = df[subjects].mean()

    plt.bar(subjects, averages)
    plt.xlabel('Môn học')
    plt.ylabel('Điểm trung bình')
    plt.title('Điểm trung bình các môn thi THPT 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
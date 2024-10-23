import matplotlib.pyplot as plt
import numpy as np

print("TRỰC QUAN HÓA DATA".center(50, '='))
def plot_average_scores(df):
    """Vẽ biểu đồ điểm trung bình các môn."""
    subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
                'lich_su', 'dia_li', 'gdcd']
    averages = df[subjects].mean()

    # Tạo màu thay đổi cho từng cột
    colours = plt.cm.viridis(np.linspace(0, 1, len(subjects)))

    plt.bar(subjects, averages, color = colours)

    for i, value in enumerate(averages):
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

    plt.xlabel('Môn học')
    plt.ylabel('Điểm trung bình')
    plt.title('Điểm trung bình các môn thi THPT 2024')

    # in nghiêng các subject
    plt.xticks(rotation=45)

    # tạo lưới mờ
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()

    plt.show()

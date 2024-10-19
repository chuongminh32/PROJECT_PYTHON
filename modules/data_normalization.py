#CODE CHUAN HOA DATA
import pandas as pd

def normalize_scores(df):
    """Chuẩn hóa các điểm thi về thang điểm 10."""
    columns_to_normalize = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 
                            'sinh_hoc', 'lich_su', 'dia_li', 'gdcd']
    
    # Xác định khoảng giá trị hợp lệ (min=0, max=10) và giới hạn giá trị về khoảng đó
    df[columns_to_normalize] = df[columns_to_normalize].clip(lower=0, upper=10)
    
    return df

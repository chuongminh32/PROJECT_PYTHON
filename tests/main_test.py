

import unittest
import pandas as pd
from modules.data_crud import add_data, update_data, delete_data, read_data
from modules.data_cleaning import remove_missing_values, remove_duplicates, correct_formatting
from modules.data_normalize import normalize_scores

class TestCRUDOperations(unittest.TestCase):

    def setUp(self):
        """Thiết lập dữ liệu ban đầu cho các bài kiểm tra"""
        self.df = pd.DataFrame({
            'sbd': [100001, 100002],
            'toan': [8.5, 6.5],
            'ngu_van': [7.0, 5.5],
            'ngoai_ngu': [9.0, 6.0],
            'vat_li': [8.0, 7.0],
            'hoa_hoc': [7.5, 12.0],  # Điểm này cần được chuẩn hóa
            'sinh_hoc': [8.0, 7.0],
            'lich_su': [6.0, 4.5],
            'dia_li': [7.0, 6.0],
            'gdcd': [8.0, 7.0],
            'ma_ngoai_ngu': [101, 102]
        })

    def test_add_data(self):
        """Kiểm tra thêm dữ liệu mới"""
        new_row = {
            'sbd': 100003, 'toan': 9.0, 'ngu_van': 8.0, 'ngoai_ngu': 8.5, 'vat_li': 9.5,
            'hoa_hoc': 8.0, 'sinh_hoc': 11.0, 'lich_su': 7.5, 'dia_li': 8.0, 'gdcd': 9.0,
            'ma_ngoai_ngu': 101
        }
        df = add_data(self.df, new_row)
        self.assertEqual(len(df), 3)
        self.assertIn(100003, df['sbd'].values)

    def test_update_data(self):
        """Kiểm tra cập nhật dữ liệu"""
        updated_row = {
            'sbd': 100002, 'toan': 7.0, 'ngu_van': 6.0, 'ngoai_ngu': 6.5, 'vat_li': 7.5,
            'hoa_hoc': 8.0, 'sinh_hoc': 7.5, 'lich_su': 5.0, 'dia_li': 6.5, 'gdcd': 7.5,
            'ma_ngoai_ngu': 102
        }
        df = update_data(self.df, 100002, updated_row)
        self.assertEqual(df.loc[df['sbd'] == 100002, 'toan'].values[0], 7.0)

    def test_delete_data(self):
        """Kiểm tra xóa dữ liệu"""
        df = delete_data(self.df, 100002)
        self.assertEqual(len(df), 1)
        self.assertNotIn(100002, df['sbd'].values)

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        """Thiết lập dữ liệu có giá trị thiếu và trùng lặp"""
        self.df = pd.DataFrame({
            'sbd': [100001, 100002, 100002],
            'toan': [8.5, None, 6.5],
            'ngu_van': [7.0, 5.5, 5.5],
            'ngoai_ngu': [9.0, 6.0, 6.0],
            'vat_li': [8.0, 7.0, 7.0]
        })

    def test_remove_missing_values(self):
        """Kiểm tra xóa giá trị thiếu"""
        df_clean = remove_missing_values(self.df)
        self.assertEqual(len(df_clean), 2)
        self.assertNotIn(None, df_clean['toan'].values)

    def test_remove_duplicates(self):
        """Kiểm tra xóa giá trị trùng lặp"""
        df_clean = remove_duplicates(self.df)
        self.assertEqual(len(df_clean), 2)

    def test_correct_formatting(self):
        """Kiểm tra sửa định dạng"""
        self.df.loc[0, 'toan'] = '8.5'  # Định dạng không đúng
        df_clean = correct_formatting(self.df)
        self.assertEqual(df_clean['toan'].dtype, 'float64')

class TestNormalization(unittest.TestCase):

    def setUp(self):
        """Thiết lập dữ liệu cần chuẩn hóa"""
        self.df = pd.DataFrame({
            'sbd': [100001, 100002],
            'toan': [8.5, 6.5],
            'ngu_van': [7.0, 5.5],
            'ngoai_ngu': [9.0, 6.0],
            'vat_li': [8.0, 7.0],
            'hoa_hoc': [7.5, 12.0],  # Điểm không hợp lệ
            'sinh_hoc': [8.0, 7.0],
            'lich_su': [6.0, 4.5],
            'dia_li': [7.0, 6.0],
            'gdcd': [8.0, 7.0]
        })

    def test_normalize_scores(self):
        """Kiểm tra chuẩn hóa điểm"""
        df_normalized = normalize_scores(self.df)
        self.assertEqual(df_normalized['hoa_hoc'].max(), 10.0)
        self.assertEqual(df_normalized['hoa_hoc'].min(), 7.5)

if __name__ == '__main__':
    unittest.main()

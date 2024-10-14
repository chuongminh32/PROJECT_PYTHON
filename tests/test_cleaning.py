# Ctrl + A -> Ctrl + '/' : xóa comment 


import unittest
import pandas as pd
from modules.data_cleaning import remove_duplicates, remove_missing_values, correct_formatting
class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'sbd': [100001, 100002, 100002],
            'toan': [8.5, None, 6.5],
            'ngu_van': [7.0, 5.5, 5.5],
            'ngoai_ngu': [9.0, 6.0, 6.0]
        })

    def test_remove_missing_values(self):
        df_clean = remove_missing_values(self.df)
        self.assertEqual(len(df_clean), 2)
        self.assertNotIn(None, df_clean['toan'].values)

    def test_remove_duplicates(self):
        df_clean = remove_duplicates(self.df)
        self.assertEqual(len(df_clean), 2)

    def test_correct_formatting(self):
        self.df.loc[0, 'toan'] = '8.5'
        df_clean = correct_formatting(self.df)
        self.assertEqual(df_clean['toan'].dtype, 'float64')

if __name__ == '__main__':
    unittest.main()

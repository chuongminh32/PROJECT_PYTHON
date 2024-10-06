

# Demo 
import unittest
import pandas as pd
from modules.data_crud import add_data, update_data, delete_data, read_data

class TestCRUDOperations(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'sbd': [100001, 100002],
            'toan': [8.5, 6.5],
            'ngu_van': [7.0, 5.5],
            'ngoai_ngu': [9.0, 6.0]
        })

    def test_add_data(self):
        new_row = {'sbd': 100003, 'toan': 9.0, 'ngu_van': 8.0, 'ngoai_ngu': 8.5}
        df = add_data(self.df, new_row)
        self.assertEqual(len(df), 3)
        self.assertIn(100003, df['sbd'].values)

    def test_update_data(self):
        updated_row = {'sbd': 100002, 'toan': 7.0, 'ngu_van': 6.0, 'ngoai_ngu': 6.5}
        df = update_data(self.df, 100002, updated_row)
        self.assertEqual(df.loc[df['sbd'] == 100002, 'toan'].values[0], 7.0)

    def test_delete_data(self):
        df = delete_data(self.df, 100002)
        self.assertEqual(len(df), 1)
        self.assertNotIn(100002, df['sbd'].values)

if __name__ == '__main__':
    unittest.main()

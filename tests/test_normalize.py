
# Demo 

import unittest
import pandas as pd
from modules.data_normalize import normalize_scores

class TestNormalization(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'sbd': [100001, 100002],
            'toan': [8.5, 6.5],
            'hoa_hoc': [7.5, 12.0]
        })

    def test_normalize_scores(self):
        df_normalized = normalize_scores(self.df)
        self.assertEqual(df_normalized['hoa_hoc'].max(), 10.0)
        self.assertEqual(df_normalized['hoa_hoc'].min(), 7.5)

if __name__ == '__main__':
    unittest.main()

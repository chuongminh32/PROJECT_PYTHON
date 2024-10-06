
# Demo 

import unittest
import pandas as pd
from modules.data_visualization import plot_histogram, plot_pie_chart

class TestVisualization(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'sbd': [100001, 100002],
            'toan': [8.5, 6.5],
            'ngu_van': [7.0, 5.5],
            'ngoai_ngu': [9.0, 6.0]
        })

    def test_plot_histogram(self):
        """Kiểm tra vẽ biểu đồ histogram"""
        try:
            plot_histogram(self.df, 'toan')
        except Exception as e:
            self.fail(f"plot_histogram failed with exception {e}")

    def test_plot_pie_chart(self):
        """Kiểm tra vẽ biểu đồ hình tròn"""
        try:
            plot_pie_chart(self.df, 'ngoai_ngu')
        except Exception as e:
            self.fail(f"plot_pie_chart failed with exception {e}")

if __name__ == '__main__':
    unittest.main()

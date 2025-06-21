import unittest
import sys
import os
import pandas as pd

# Tambahkan path ke direktori root project agar bisa import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.load import load_data  # Import load.py dari folder utils

class TestLoad(unittest.TestCase):

    def setUp(self):
        # Setup untuk membuat file dummy input CSV
        self.input_csv = 'tests/dummy_input.csv'
        self.output_csv = 'tests/dummy_output.csv'

        dummy_data = pd.DataFrame({
            'title': ['Product A', 'Product B'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0],
            'colors': ['Red', 'Blue'],
            'size': ['M', 'L'],
            'gender': ['Male', 'Female']
        })

        dummy_data.to_csv(self.input_csv, index=False)

    def tearDown(self):
        # Cleanup untuk menghapus file dummy
        if os.path.exists(self.input_csv):
            os.remove(self.input_csv)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)

    def test_load_data(self):
        # Memanggil fungsi load_data
        load_data(self.input_csv, self.output_csv)

        result_df = pd.read_csv(self.output_csv)

        # Memastikan data telah dimuat dan disimpan dengan benar
        self.assertGreater(len(result_df), 0)
        self.assertTrue(os.path.exists(self.output_csv))

if __name__ == '__main__':
    unittest.main()
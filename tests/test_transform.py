import unittest
import sys
import os
import pandas as pd

# Tambahkan path ke direktori 'utils' agar bisa import transform
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.transform import transform_data

class TestTransform(unittest.TestCase):

    def setUp(self):
        # Setup: bikin file dummy input CSV
        self.input_csv = 'tests/dummy_input.csv'
        self.output_csv = 'tests/dummy_output.csv'

        dummy_data = pd.DataFrame({
            'title': ['Product A', 'Unknown Product'],
            'price': ['$10.00', '$20.00'],
            'rating': ['Rating: 4.5 / 5', 'Invalid Rating'],
            'colors': ['Colors: 2', 'Colors: 3'],
            'size': ['Size: M', 'Size: L'],
            'gender': ['Gender: Male', 'Gender: Female']
        })

        dummy_data.to_csv(self.input_csv, index=False)

    def tearDown(self):
        # Cleanup: hapus file dummy
        if os.path.exists(self.input_csv):
            os.remove(self.input_csv)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)

    def test_transform_data_output(self):
        transform_data(self.input_csv, self.output_csv, exchange_rate=16000)

        result_df = pd.read_csv(self.output_csv)

        # Hanya 1 baris valid (yang bukan Unknown Product & Invalid Rating)
        self.assertEqual(len(result_df), 1)

        # Price sudah dikali kurs
        self.assertEqual(result_df['price'].iloc[0], 160000.0)

        # Rating sudah jadi float
        self.assertAlmostEqual(result_df['rating'].iloc[0], 4.5)

        # Kolom sudah dibersihkan
        self.assertEqual(int(result_df['colors'].iloc[0]), 2)  # Fix type mismatch
        self.assertEqual(result_df['size'].iloc[0], 'M')
        self.assertEqual(result_df['gender'].iloc[0], 'Male')

if __name__ == '__main__':
    unittest.main()
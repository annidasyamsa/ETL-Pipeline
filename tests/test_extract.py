import unittest
import sys
import os

# Tambahkan path project root agar bisa import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.extract import scrape_data

class TestExtract(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result = scrape_data()

    def test_title(self):
        self.assertGreater(len(self.result['title']), 0, "Title list is empty")

    def test_price(self):
        self.assertGreater(len(self.result['price']), 0, "Price list is empty")

    def test_rating(self):
        self.assertGreater(len(self.result['rating']), 0, "Rating list is empty")

    def test_length_consistency(self):
        self.assertEqual(len(self.result['title']), len(self.result['price']), "Title and Price length mismatch")
        self.assertEqual(len(self.result['title']), len(self.result['rating']), "Title and Rating length mismatch")

if __name__ == '__main__':
    unittest.main()
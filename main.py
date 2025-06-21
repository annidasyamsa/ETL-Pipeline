from utils.extract import scrape_data
from utils.transform import transform_data
from utils.load import load_data

def main():
    # Extract
    scrape_data()  # Menyimpan data ke scraping_products.csv

    # Transform
    transform_data(
        input_csv='scraping_products.csv',  # Input file CSV dari Extract
        output_csv='scraping_products_transformed.csv',  # Output file hasil transformasi
        exchange_rate=16000  # Kurs yang ingin digunakan
    )

    # Load
    load_data(
        input_file='scraping_products_transformed.csv',  # Input file CSV yang sudah ditransformasi
        output_file='products.csv'  # Output file untuk data yang sudah dimuat
    )

if __name__ == '__main__':
    main()
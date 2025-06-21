import pandas as pd

def transform_data(input_csv, output_csv, exchange_rate=16000):
    # Baca CSV yang dihasilkan oleh extract.py
    product_df = pd.read_csv(input_csv)

    # Hapus baris yang mengandung nilai invalid seperti "Unknown Product"
    product_df = product_df[~product_df['title'].str.contains("Unknown Product", na=False)]

    # Hapus duplikat berdasarkan kolom 'title' dan 'price'
    product_df = product_df.drop_duplicates(subset=['title', 'price'], keep='first')

    # Hapus baris yang memiliki nilai null
    product_df = product_df.dropna(subset=['title', 'rating', 'price', 'colors', 'size', 'gender'])

    # Konversi Price dari USD ke IDR (rupiah)
    product_df['price'] = product_df['price'].apply(
        lambda x: float(x.replace('$', '').replace(',', '')) * exchange_rate if isinstance(x, str) and '$' in x else x
    )

    # Bersihkan kolom 'rating'
    def clean_rating(x):
        if isinstance(x, str):
            x = x.replace('Rating: ', '').replace(' / 5', '').replace('⭐', '').strip()
            try:
                return float(x)
            except ValueError:
                return None
        return x

    product_df['rating'] = product_df['rating'].apply(clean_rating)

    # Bersihkan kolom 'colors' jadi hanya angka
    product_df['colors'] = product_df['colors'].apply(lambda x: ''.join(filter(str.isdigit, str(x))))

    # Bersihkan kolom 'size' dari teks "Size: "
    product_df['size'] = product_df['size'].apply(lambda x: str(x).replace('Size: ', '') if isinstance(x, str) else x)

    # Bersihkan kolom 'gender' dari teks "Gender: "
    product_df['gender'] = product_df['gender'].apply(lambda x: str(x).replace('Gender: ', '') if isinstance(x, str) else x)

    # Konversi price jadi float
    product_df['price'] = pd.to_numeric(product_df['price'], errors='coerce')

    # Hapus baris yang punya price atau rating invalid
    product_df = product_df.dropna(subset=['price', 'rating'])

    # Simpan hasil transformasi
    product_df.to_csv(output_csv, index=False)
    print(f"Data yang sudah ditransformasi telah disimpan di '{output_csv}'")

# Cuma akan jalan kalau file ini dijalankan langsung
if __name__ == '__main__':
    transform_data('scraping_products.csv', 'scraping_products_transformed.csv')
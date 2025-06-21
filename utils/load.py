import pandas as pd

def load_data(input_file, output_file):
    # Membaca data CSV yang sudah ditransformasi
    df = pd.read_csv(input_file)

    # Menampilkan informasi DataFrame
    print("Informasi DataFrame:")
    print(df.info())

    # Menampilkan 5 baris pertama DataFrame
    print("\n5 Baris Pertama DataFrame:")
    print(df.head())

    # Cek tidak ada nilai null
    assert not df.isnull().values.any(), "Masih ada nilai null!"

    # Cek tidak ada duplikat
    assert df.duplicated().sum() == 0, "Masih ada data duplikat!"

    # Simpan ke file CSV final
    df.to_csv(output_file, index=False)
    print(f"Data berhasil disimpan ke {output_file}")


# Supaya tidak langsung jalan saat di import oleh test
if __name__ == '__main__':
    load_data('scraping_products_transformed.csv', 'products.csv')
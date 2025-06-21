import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
from datetime import datetime

def scrape_data():
    product_dict = {'title': [], 'price': [], 'rating': [], 'colors': [], 'size': [], 'gender': []}
    base_url = "https://fashion-studio.dicoding.dev/"
    pages = range(1, 51)

    for page in tqdm(pages, desc="Scraping pages"):
        try:
            url = base_url + f"page{page}" if page > 1 else base_url
            response = requests.get(url)
            soup = bs(response.content, 'html.parser')

            # Ambil semua elemen produk
            products = soup.find_all("div", {"class": "product-details"})

            for product in products:
                judul = product.find('h3').text.strip()
                price_container = product.find('div', class_='price-container')

                if price_container:
                    price = price_container.text.strip()
                    start_rating = 0
                else:
                    price = "NA"
                    start_rating = 1

                p = product.find_all('p')
                rating = p[start_rating].text.strip()
                colors = p[start_rating+1].text.strip()
                size = p[start_rating+2].text.strip()
                gender = p[start_rating+3].text.strip()

                # Simpan data ke dictionary
                product_dict['title'].append(judul)
                product_dict['price'].append(price)
                product_dict['rating'].append(rating)
                product_dict['colors'].append(colors)
                product_dict['gender'].append(gender)
                product_dict['size'].append(size)

        except Exception as e:
            print(f"Error on page {page}: {e}")
            continue

    return product_dict

def save_to_csv(product_dict):
    # Konversi data ke DataFrame
    product_df = pd.DataFrame(product_dict)

     # Tambahkan kolom Timestamp dengan waktu saat ini (ISO format)
    product_df["Timestamp"] = datetime.now().isoformat()

    # Simpan DataFrame ke file CSV
    product_df.to_csv('scraping_products.csv', index=False)
    print("Data mentah telah disimpan di 'scraping_products.csv'")

    # Tampilkan info dan 5 baris pertama
    print("\nInfo DataFrame:")
    print(product_df.info())
    print("\n5 Baris Pertama DataFrame:")
    print(product_df.head())

# Panggil fungsi scrape_data dan simpan ke CSV
raw_data = scrape_data()
save_to_csv(raw_data)
# 🛠️ ETL Pipeline Execution Guide

Selamat datang di proyek ETL Pipeline🎉  
Panduan ini akan membantu Anda menjalankan pipeline, menguji unit test, dan melihat laporan test coverage dengan mudah. 
Pastikan Anda berada di **root folder** yang berisi:

- `main.py`  
- Subfolder: `utils/` dan `tests/`

---
 ## ✅ Persiapan Awal
 
Sebelum menjalankan pipeline, pastikan semua dependensi sudah terpasang:
```pip install -r requirements.txt```

## 🚀 Menjalankan Pipeline

Jalankan skrip utama dengan perintah berikut:
```python main.py```

## 🧪 Menjalankan Unit Test

Untuk menjalankan seluruh unit test yang ada di folder tests/:
```python -m pytest tests```

## 📊 Menjalankan Test Coverage

Ingin mengetahui seberapa banyak kode yang ter-cover oleh test? Gunakan:
```coverage run -m pytest tests```

## 📋 Menampilkan Laporan Coverage

Setelah coverage dijalankan, tampilkan laporannya di terminal dengan:
```coverage report```


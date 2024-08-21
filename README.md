# SSCASN Data Scraper

## Author
**Romi Julianto**

## Deskripsi
Program ini adalah sebuah scraper data untuk portal SSCASN. Program ini mengakses API publik SSCASN untuk mengambil data formasi yang tersedia, kemudian menyimpannya dalam bentuk file Excel dan file teks. Data yang diambil mencakup berbagai informasi mengenai formasi yang tersedia khususnya `S1-Teknik Geomatika`,

Di bagian atas file Excel, metadata seperti `updated_at` dan `auto_update_by` ditambahkan untuk memberikan informasi tentang waktu pembaruan data dan siapa yang menjalankan program.

## Persiapan dan Instalasi

### 1. Clone Repository
Pertama-tama, clone repository ini ke mesin lokal Anda menggunakan Git:

```bash
git clone https://github.com/username/sscasn-scraper.git
cd sscasn-scraper
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Jalankan server

```bash
python server.py
```


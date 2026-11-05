# Analisis dan Visualisasi Harga Mobil Bekas

**Nama:** [Isi nama]  
**NPM:** [Isi NPM]  
**Mata kuliah:** Visualisasi Data

## Deskripsi
Proyek ini menganalisis dataset listing mobil bekas di beberapa kota di India. Dashboard menampilkan KPI jumlah mobil, rata-rata dan median harga, rata-rata jarak tempuh, serta grafik tren harga menurut tahun, perbandingan merek, komposisi bahan bakar, hubungan jarak tempuh dan harga, dan persebaran listing per kota.

## Dataset dan sumber
File kerja berasal dari arsip `archive.zip` yang diberikan untuk pengerjaan. Dataset gabungan berisi 1.725 baris sebelum proses cleaning. **Tautan Kaggle asli belum tercantum di dalam arsip yang diterima.** Lengkapi tautan sumber Kaggle yang benar di sini sebelum mengumpulkan: `[TEMPELKAN URL DATASET KAGGLE]`. Jangan mengarang URL atau mengklaim sumber yang belum diverifikasi.

## Struktur proyek
```
uts_visualisasi_mobil_bekas/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── used_cars_clean.csv
└── notebooks/
    └── analisis_mobil_bekas.ipynb
```

## Menjalankan di JupyterLab
Disarankan menggunakan Python 3.11–3.13 untuk kompatibilitas paket yang luas. Jika lingkungan Python 3.15 yang digunakan belum memiliki wheel untuk seluruh dependensi, buat environment Python stabil yang didukung paket. Jalankan dari terminal:

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Buka `notebooks/analisis_mobil_bekas.ipynb`, lalu jalankan seluruh sel dari atas ke bawah.

## Menjalankan dashboard lokal
Dari folder proyek:

```bash
streamlit run app.py
```

Dashboard akan terbuka di browser lokal, biasanya `http://localhost:8501`.

## Fitur dashboard
- 4 KPI cards.
- 5 visualisasi: line, bar, pie/donut, scatter, dan bar kota.
- Filter interaktif kota, merek, bahan bakar, dan rentang tahun.
- Insight dinamis berdasarkan filter.
- Tabel data dan unduhan CSV.

## Temuan awal dari data gabungan
- Dataset gabungan memiliki 1.725 baris dan 9 kolom utama sebelum cleaning.
- Terdapat 31 merek, 15 label kota, dan 5 kategori bahan bakar.
- Kota dengan jumlah listing paling banyak adalah Chennai (493 baris).
- Merek dengan jumlah listing paling banyak adalah Hyundai (297 baris).
- Jenis bahan bakar terbanyak adalah Diesel (922 baris), disusul Petrol (788 baris).
- Rata-rata harga pada data mentah sekitar ₹1.494.837 dan median sekitar ₹875.000.

Insight tersebut bersifat deskriptif untuk dataset yang diberikan, bukan generalisasi seluruh pasar mobil bekas India.

## Deployment dan GitHub
1. Buat repository GitHub berstatus **Public**.
2. Unggah seluruh folder proyek.
3. Untuk live dashboard, hubungkan repository ke Streamlit Community Cloud dan pilih `app.py` sebagai entry point.
4. Setelah deployment berhasil, masukkan URL live dashboard di bagian ini: `[URL LIVE DASHBOARD]`.
5. Pastikan README berisi nama/NPM, tautan Kaggle yang benar, dan URL dashboard aktif sebelum mengumpulkan.

# Analisis dan Visualisasi Data Mobil Bekas

Dashboard interaktif untuk menganalisis data mobil bekas berdasarkan harga, merek, tahun produksi, jarak tempuh, jenis bahan bakar, dan lokasi penjualan. Proyek ini menggunakan Python dan Streamlit untuk menyajikan hasil pengolahan data dalam bentuk visualisasi yang mudah dipahami.

## 1. Identitas Mahasiswa

| Keterangan | Informasi |
|---|---|
| Nama | Aldri Adi Prakasya |
| NPM | 241051012 |
| Program Studi | Sistem Informasi |
| Mata Kuliah | Visualisasi Data |
| Dosen Pengampu | Muryan Awaludin, S.Kom., M.Kom. |

## 2. Deskripsi Proyek

Proyek ini membahas analisis data mobil bekas untuk mengetahui karakteristik pasar berdasarkan beberapa atribut kendaraan.

Analisis berfokus pada hubungan antara harga mobil dengan tahun produksi, merek, jarak tempuh, jenis bahan bakar, dan lokasi penjualan.

Hasil analisis disajikan melalui dashboard interaktif. Pengguna dapat memilih filter tertentu untuk melihat perubahan informasi dan visualisasi sesuai kebutuhan.

## 3. Tujuan Analisis

Tujuan proyek ini adalah:

1. Mengetahui distribusi harga mobil bekas.
2. Membandingkan jumlah kendaraan berdasarkan merek.
3. Menganalisis hubungan tahun produksi dengan harga kendaraan.
4. Mengetahui komposisi jenis bahan bakar.
5. Menganalisis hubungan jarak tempuh dengan harga mobil.
6. Mengetahui persebaran data mobil bekas berdasarkan kota.

## 4. Sumber Dataset

Dataset yang digunakan dalam proyek ini berasal dari Kaggle.

- **Nama Dataset:** Used Car Information
- **Pembuat Dataset:** Sanjeet Singh Naik
- **Platform:** Kaggle
- **Tautan Dataset:** https://www.kaggle.com/datasets/sanjeetsinghnaik/used-car-information

Dataset berisi informasi kendaraan bekas, termasuk merek, harga, tahun produksi, jarak tempuh, jenis bahan bakar, dan lokasi kendaraan.

Berdasarkan pemeriksaan awal, dataset memiliki 1.725 baris dan 9 kolom sebelum proses pembersihan data.

## 5. Tahapan Pengolahan Data

Pengolahan data dilakukan melalui beberapa tahapan berikut:

1. **Data Collection**  
   Mengumpulkan dataset mobil bekas dari Kaggle.

2. **Data Inspection**  
   Memeriksa struktur dataset, jumlah baris, jumlah kolom, tipe data, dan kelengkapan data.

3. **Data Cleaning**  
   Menangani data kosong, memeriksa data duplikat, dan memperbaiki format data yang diperlukan.

4. **Data Transformation**  
   Menyesuaikan tipe data dan menyiapkan kolom agar dapat digunakan dalam proses analisis.

5. **Exploratory Data Analysis (EDA)**  
   Melakukan analisis statistik deskriptif untuk memahami karakteristik dataset.

6. **Data Visualization**  
   Menyajikan hasil analisis dalam bentuk grafik dan indikator pada dashboard Streamlit.

## 6. Fitur Dashboard

Dashboard menyediakan beberapa fitur utama:

- **KPI Cards:** Menampilkan jumlah mobil, rata-rata harga, median harga, dan rata-rata jarak tempuh.
- **Filter Kota:** Memilih data berdasarkan lokasi kendaraan.
- **Filter Merek:** Memilih merek mobil tertentu.
- **Filter Bahan Bakar:** Menampilkan kendaraan berdasarkan jenis bahan bakar.
- **Filter Tahun:** Membatasi rentang tahun produksi kendaraan.
- **Visualisasi Interaktif:** Menampilkan grafik berdasarkan filter yang dipilih.
- **Dynamic Insights:** Menampilkan informasi berdasarkan hasil penyaringan data.
- **Data Table:** Menampilkan data kendaraan dalam bentuk tabel.
- **Download CSV:** Mengunduh data yang telah difilter.

## 7. Visualisasi yang Digunakan

Dashboard menggunakan lima jenis visualisasi utama:

| No. | Visualisasi | Tujuan |
|---|---|---|
| 1 | Line Chart | Melihat perubahan harga berdasarkan tahun produksi |
| 2 | Bar Chart | Membandingkan jumlah mobil berdasarkan merek |
| 3 | Pie Chart | Menampilkan komposisi jenis bahan bakar |
| 4 | Scatter Plot | Melihat hubungan jarak tempuh dengan harga mobil |
| 5 | Bar Chart | Membandingkan jumlah kendaraan berdasarkan kota |

## 8. Hasil Analisis Awal

Berdasarkan pemeriksaan awal terhadap dataset sebelum proses pembersihan, diperoleh beberapa informasi:

- Jumlah data awal sebanyak 1.725 kendaraan.
- Dataset memiliki 9 kolom.
- Terdapat 31 merek kendaraan.
- Data mencakup 15 label kota.
- Terdapat 5 kategori bahan bakar.
- Chennai memiliki jumlah kendaraan terbanyak, yaitu 493 data.
- Hyundai menjadi merek dengan jumlah data terbanyak, yaitu 297 kendaraan.
- Diesel memiliki 922 data dan Petrol memiliki 788 data.
- Rata-rata harga pada data awal sekitar ₹1.494.837.
- Median harga pada data awal sekitar ₹875.000.

**Catatan:** Angka tersebut merupakan hasil pemeriksaan awal dataset sebelum pembersihan. Angka tersebut tidak otomatis mewakili hasil akhir setelah proses pengolahan data.

## 9. Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Pandas | Pengolahan dan manipulasi data |
| NumPy | Operasi numerik |
| Matplotlib | Pembuatan visualisasi |
| Seaborn | Visualisasi statistik |
| Plotly | Grafik interaktif |
| Streamlit | Pembuatan dashboard web |
| JupyterLab | Pengolahan dan eksplorasi data |

## 10. Struktur Folder Proyek

```text
uts-visualisasi_data_mobil/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── used_cars_clean.csv
│
└── notebooks/
    └── analisis_mobil_bekas.ipynb
```

## 11. Cara Menjalankan Dashboard Secara Lokal

Ikuti langkah berikut untuk menjalankan dashboard pada komputer.

### A. Persyaratan

Pastikan perangkat telah memiliki:

- Python
- JupyterLab (opsional, untuk eksplorasi data)
- Koneksi internet

### B. Clone Repository

Buka Command Prompt atau terminal, kemudian jalankan:

```bash
git clone https://github.com/AldriRobocop/uts-visualisasi_data_mobil.git
```

Masuk ke folder proyek:

```bash
cd uts-visualisasi_data_mobil
```

### C. Instal Library

Jalankan perintah berikut:

```bash
py -m pip install -r requirements.txt
```

### D. Jalankan Streamlit

Setelah instalasi selesai, jalankan:

```bash
py -m streamlit run app.py
```

Dashboard akan terbuka melalui browser. Jika tidak terbuka secara otomatis, akses alamat lokal yang ditampilkan pada terminal, biasanya:

```text
http://localhost:8501
```

## 12. Deployment

Dashboard telah dipublikasikan menggunakan Streamlit Community Cloud.

**Link Dashboard:**

https://uts-visualisasidatamobil.streamlit.app/

**Repository GitHub:**

https://github.com/AldriRobocop/uts-visualisasi_data_mobil

**Sumber Dataset:**

https://www.kaggle.com/datasets/sanjeetsinghnaik/used-car-information

## 13. Kesimpulan

Proyek ini menghasilkan dashboard interaktif untuk menganalisis karakteristik data mobil bekas. Dashboard menyajikan informasi mengenai harga, merek, tahun produksi, jarak tempuh, jenis bahan bakar, dan lokasi kendaraan.

Penggunaan Python, Pandas, Plotly, dan Streamlit membantu proses pengolahan serta penyajian data secara lebih terstruktur. Fitur filter juga memungkinkan pengguna mengeksplorasi data berdasarkan kriteria tertentu.

Melalui proyek ini, visualisasi data dapat membantu pengguna memahami informasi kendaraan bekas dan memperoleh gambaran mengenai karakteristik dataset yang dianalisis.

---

**Dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Visualisasi Data.**
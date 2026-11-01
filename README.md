# 📈 Platform Analisis Kuantitatif Reksa Dana Pasar Modal Indonesia
### *Next-Gen Institutional Multi-Criteria Scoring & Interactive Analytics Dashboard*

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3.4-38bdf8.svg)
![Chart.js](https://img.shields.io/badge/Chart.js-v4.4-FF6384.svg)
![OJK Regulated](https://img.shields.io/badge/Data-OJK%20%26%20Bibit-emerald.svg)

Platform analitik kuantitatif interaktif berbasis web untuk mengevaluasi, membandingkan, dan memeringkatkan **146 Reksa Dana Aktif & Tradeable** di pasar modal Indonesia secara adil (*anti-bias*) menggunakan metodologi *Peer-Group Segmentation*, *Max Drawdown*, dan *Calmar Ratio*.

---

## 📸 Antarmuka Platform & Tangkapan Layar

### 1. Dashboard Analisis Utama
Menampilkan indikator utama pasar, filter kategori aset, pengurutan cerdas, dan kurva pertumbuhan modal terintegrasi untuk 3 Reksa Dana teratas:
![Dashboard Analisis Utama](docs/screenshots/dashboard_utama_v1.png)

### 2. Modal Dialog Analisis Mendalam & Portofolio
Menyajikan 8 metrik finansial esensial, kurva kinerja multi-periode (1Y, 3Y, 5Y), perbandingan vs rata-rata kategori (*peer group*), alokasi aset, serta 5 efek portofolio terbesar (*top holdings*) dengan format penulisan baku dan rapi:
![Modal Detail Reksa Dana](docs/screenshots/modal_detail_v1.png)

### 3. Portal Panduan Edukasi & Kalkulator Simulasi Investor
Buku panduan edukatif berstandar institusional yang menjelaskan konsep reksa dana, glosarium metrik kuantitatif, dan kalkulator simulasi nominal investasi interaktif:
![Buku Panduan Edukasi Investor](docs/screenshots/panduan_edukasi_v1.png)

---

## 📅 Cakupan Periode & Rentang Waktu Data

Seluruh kalkulasi dan simulasi pada platform ini dibangun menggunakan data historis pasar modal Indonesia dengan parameter waktu yang transparan dan dapat diverifikasi:

| Parameter Metrik | Rentang Waktu / Tanggal | Penjelasan Teknis |
| :--- | :--- | :--- |
| **Tanggal Cut-off NAV Harian** | **29 – 30 Oktober 2026** | 135 reksa dana dicatat per **30 Oktober 2026** dan 12 reksa dana per **29 Oktober 2026** (hari bursa aktif terakhir). |
| **Tanggal Laporan Resmi AUM** | **September 2026** | Mengikuti siklus publikasi resmi bulanan Otoritas Jasa Keuangan (OJK) dan KSEI. |
| **Rentang Peluncuran (*Inception*)** | **Tahun 2000 – 2026** | Mencakup reksa dana tertua berumur **26 tahun** (seperti *BNP Paribas Pesona*, *Schroder Dana Prestasi*, *Batavia Dana Saham* yang diluncurkan sejak 5 Januari 2000) hingga reksa dana emisi baru Juli 2026. |
| **Horizon Kinerja 1 Tahun (1Y)** | **Oktober 2025 – Oktober 2026** | Mengukur imbal hasil jangka pendek tahunan (*CAGR 1Y*). |
| **Horizon Kinerja 3 Tahun (3Y)** | **Oktober 2023 – Oktober 2026** | Horizon evaluasi primer untuk kalkulasi imbal hasil majemuk (*CAGR 3Y*), penurunan terdalam (*Max Drawdown 3Y*), dan *Calmar Ratio*. |
| **Horizon Kinerja 5 Tahun (5Y)** | **Oktober 2021 – Oktober 2026** | Mengukur ketahanan modal jangka menengah-panjang melintasi berbagai siklus suku bunga Bank Indonesia. |
| **Sumber Data Primer** | **OJK, KSEI, & Bibit API** | Registri resmi produk investasi reksa dana terdaftar dan diawasi OJK. |

---

## 🚀 Keunggulan Metodologi Kuantitatif (Next-Gen Model)

Model evaluasi konvensional sering kali tidak adil karena membandingkan seluruh reksa dana dalam satu wadah global, sehingga reksa dana pasar uang berisiko nol terdepak oleh reksa dana saham yang berfluktuasi tinggi. Platform ini menerapkan **3 Pilar Penyempurnaan Model Institusional**:

1. **Anti-Bias Kategori (*Peer-Group Segmentation*):**  
   Evaluasi dan perankingan dinilai secara terpisah di dalam masing-masing habitat kelas asetnya (*Pasar Uang vs Pasar Uang, Obligasi vs Obligasi, Saham vs Saham, Campuran vs Campuran*).
2. **Keseimbangan Imbal Hasil vs Risiko (*Calmar Ratio & Max Drawdown 3Y*):**  
   Tingkat penurunan nilai maksimal (*Max Drawdown*) diintegrasikan sebagai pengurang skor utama, dan *Calmar Ratio* digunakan untuk mengukur efisiensi imbal hasil per unit risiko penurunan.
3. **Filter Kelayakan Likuiditas (*AUM Liquidity Penalty*):**  
   Reksa dana dengan dana kelolaan kecil di bawah ambang batas likuiditas sehat (< Rp 25 Miliar) dikenakan penalti diskon skor untuk memitigasi risiko pembubaran produk (*fund liquidation*).

---

## 💻 Fitur Utama Platform

### 1. Dashboard Analisis Utama (`index.html`)
* **Hero Visualization (Top 3 Reksa Dana):**
  * *Mode 1 (Kurva Pertumbuhan 3 Tahun):* Menampilkan trajektori pertumbuhan modal Rp 10.000.000 secara halus (*smooth spline*) dengan *soft gradient fill* tiga garis berbeda.
  * *Mode 2 (Imbal Hasil vs Risiko):* Perbandingan batang berkelompok antara *Return 3Y CAGR* bersanding langsung dengan *Max Drawdown 3Y*.
* **Peta Risiko vs Imbal Hasil (*Scatter Plot*):** Diagram sebar kuadran yang memetakan seluruh reksa dana; kuadran kiri-atas merefleksikan portofolio paling optimal (Drawdown Rendah, Return Tinggi).
* **Peta Manajer Investasi Terbesar:** Grafik batang total dana kelolaan (AUM) per Manajer Investasi di Indonesia.
* **Dropbox Filter Kategori & Urutkan:** Pemilahan cepat berdasarkan kelas aset dan pengurutan (Rank Terbaik, Rank Terburuk, Return 3Y, Drawdown Terendah, dan AUM).
* **Modal Dialog Detail Setiap Reksa Dana:**
  * Profil legalitas & Bank Kustodian
  * 8 Kartu Metrik Finansial
  * Kurva Kinerja Multi-Periode (1Y, 3Y, 5Y)
  * Diagram Komparasi vs Rata-Rata Kategori Sejenis (*Peer Group*)
  * Alokasi Aset & 5 Efek Portofolio Terbesar (*Top Holdings*)
  * Simulasi Pertumbuhan Riil Modal Rp 10 Juta selama 3 Tahun
  * Analisis Karakteristik & Rekomendasi Profil Investor

### 2. Portal Edukasi & Buku Panduan Pemula (`panduan.html`)
* Disusun dengan bahasa baku, formal, dan mudah dipahami tanpa jargon rumit.
* Glosarium resmi metrik keuangan (*CAGR, Max Drawdown, Calmar Ratio, Expense Ratio*).
* Simulasi komparasi nyata uang Rp 10 Juta pada Pasar Uang, Obligasi, dan Saham.
* **Kalkulator Simulasi Interaktif:** Menghitung estimasi nilai akhir portofolio dan potensi koreksi risiko berdasarkan input nominal modal investor.

---

## 📂 Struktur Proyek

```text
├── index.html                  # Halaman dashboard analisis kuantitatif utama
├── panduan.html                # Portal edukasi, glosarium, dan kalkulator simulasi
├── data_indonesia.js           # Dataset 146 reksa dana Indonesia (JSON embedded)
├── serve.py                    # Server web lokal Python (port 3000)
├── README.md                   # Dokumentasi teknis proyek
└── data/                       # Data olahan
    ├── enriched_funds.json     # Metadata portofolio & kustodian lengkap
    ├── reksadana_indonesia_scored.csv   # Hasil scoring kuantitatif
    └── reksadana_indonesia_scored.xlsx  # Lembar kerja kalkulasi model
```

---

## 🛠️ Panduan Instalasi & Menjalankan Lokal

Pastikan Anda telah menginstal **Python 3.8+** pada sistem Anda:

```bash
# 1. Kloning repositori
git clone https://github.com/pranataa-labs/indonesia-mutual-fund-analytics.git
cd indonesia-mutual-fund-analytics

# 2. Jalankan server lokal
python serve.py
```

Buka peramban (*browser*) Anda pada tautan:
* **Dashboard Utama:** `http://localhost:3000/index.html`
* **Buku Panduan Investor:** `http://localhost:3000/panduan.html`

---

## 📜 Lisensi & Atribusi

Proyek ini dirilis di bawah lisensi [MIT License](LICENSE).  
Hak Cipta © 2026 **Pranataa Labs**.

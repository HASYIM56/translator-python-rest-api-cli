# Multi-Language Translation CLI Program (MLTCP)

Program ini adalah aplikasi **Command Line Interface (CLI)** berbasis Python yang berfungsi untuk menerjemahkan teks ke berbagai bahasa menggunakan **H56 Translator API**. Aplikasi ini didesain dengan tampilan tabel ASCII yang rapi sehingga pengalaman penggunaan terasa lebih terstruktur dan mudah dibaca.

------------------------------------------------------------------------

## Daftar Isi

1.  [Pendahuluan](#pendahuluan)
2.  [Fitur Utama](#fitur-utama)
3.  [Fitur Baru](#fitur-baru)
4.  [Struktur Program](#struktur-program)
5.  [Instalasi](#instalasi)
6.  [Menjalankan Program](#menjalankan-program)
7.  [Cara Menggunakan](#cara-menggunakan)
8.  [Dokumentasi API](#dokumentasi-api)
9.  [Riwayat Terjemahan](#riwayat-terjemahan)
10. [Troubleshooting](#troubleshooting)

------------------------------------------------------------------------

## Pendahuluan

Program ini dibuat untuk memudahkan pengguna dalam menerjemahkan teks dari bahasa apa pun ke beberapa bahasa yang didukung melalui antarmuka terminal. Dengan memanfaatkan API pihak ketiga, aplikasi ini memungkinkan pengguna mendapat hasil terjemahan secara cepat dan praktis.

------------------------------------------------------------------------

## Fitur Utama

-   **Antarmuka ASCII yang rapi** menggunakan tabel untuk menu dan hasil terjemahan.
-   **Dukungan banyak bahasa**, yaitu:
    -   `id` --- Indonesia
    -   `en` --- English
    -   `ja` --- Japanese
    -   `ko` --- Korean
    -   `ar` --- Arabic
    -   `fr` --- French
    -   `de` --- German
    -   `es` --- Spanish
    -   `ru` --- Russian
    -   `zh` --- Chinese (Mandarin)
-   **Input ID negara (opsional)**, ditampilkan dalam hasil terjemahan.
-   **Penanganan error** saat API gagal diakses atau terjadi timeout.
-   **Pembersihan layar otomatis** agar tampilan tetap bersih dan profesional.

------------------------------------------------------------------------

## Fitur Baru

Program telah ditingkatkan dengan beberapa fitur tambahan:

### 1. Menu Log Riwayat
- Semua hasil terjemahan otomatis disimpan ke file:
```
h56_history.log
```
- Informasi yang disimpan:
  - Teks asli
  - Hasil terjemahan
  - Bahasa target
  - ID negara (opsional)
  - Timestamp

### 2. Tampilan Riwayat Terjemahan
- Pengguna dapat memilih menu **"Lihat Riwayat Terjemahan"** untuk melihat semua aktivitas sebelumnya.
- Log ditampilkan dalam terminal secara rapi.

### 3. Validasi Input Lebih Baik
- Jika bahasa tidak sesuai daftar, program memberi peringatan.
- Jika input teks kosong, pengguna diminta isi ulang.

### 4. Dukungan Perintah `back`
- Saat memilih bahasa target, ketik `back` untuk kembali ke menu sebelumnya.

### 5. Lebar Tabel Dinamis
Variabel:
```
W = 60
```
digunakan untuk mengatur lebar tampilan tabel ASCII.

------------------------------------------------------------------------

## Struktur Program

Berikut fungsi-fungsi utama dalam kode:

| Fungsi | Deskripsi |
|---|---|
| `main_menu()` | Menampilkan menu utama dan memproses pilihan pengguna. |
| `start_translation()` | Mengatur alur input pengguna dan menampilkan hasil terjemahan. |
| `translate(text, target)` | Mengirim permintaan POST ke API untuk menerjemahkan teks. |
| `show_languages()` | Menampilkan daftar bahasa yang tersedia. |
| `show_history()` | Menampilkan riwayat dari file log. |
| `log_history()` | Menyimpan riwayat ke file `h56_history.log`. |
| `line(width)` | Membuat garis pemisah tabel ASCII. |
| `row(text, width)` | Membuat baris isi tabel ASCII. |
| `clear()` | Membersihkan layar terminal (Windows/Linux/Mac). |

------------------------------------------------------------------------

## Instalasi

### 1. Pastikan Python Terinstal

Program ini menggunakan **Python 3.7+**.

Cek dengan:

```bash
python --version
```

### 2. Install Dependensi

Hanya membutuhkan modul eksternal berikut:

```bash
pip install requests
```

### 3. (Opsional) Clone Repo

```bash
git clone https://github.com/HASYIM56/translator-python-rest-api-cli.git
cd translator-project
```

------------------------------------------------------------------------

## Menjalankan Program

Jalankan program melalui terminal:

```bash
python translator.py
```

------------------------------------------------------------------------

## Cara Menggunakan

### 1. Buka program

Akan muncul menu utama seperti:

```
+--------------------------------------------------+
| PROGRAM TERJEMAHAN MULTI-BAHASA                  |
+--------------------------------------------------+
| 1. Mulai Terjemahkan                             |
| 2. Lihat Riwayat Terjemahan                      |
| 3. Keluar Program                                |
+--------------------------------------------------+
```

### 2. Pilih menu **1** untuk mulai menerjemahkan.

### 3. Masukkan teks yang ingin diterjemahkan.

Contoh:

```
Masukkan teks yang mau diterjemahkan : Hello, how are you?
```

### 4. Pilih bahasa target dari daftar seperti:

```
id = Indonesia
en = English
ja = Japanese
...
```

### 5. (Opsional) Masukkan ID negara.

### 6. Hasil terjemahan akan ditampilkan dalam tabel ASCII.

------------------------------------------------------------------------

## Dokumentasi API

Program ini menggunakan API penerjemah publik:

-   **Endpoint**

```
POST https://h56-translator-api.vercel.app/api/translate
```

-   **Payload**

```json
{
  "text": "teks yang akan diterjemahkan",
  "targetLang": "kode_bahasa"
}
```

-   **Headers**

```
Content-Type: application/json
```

-   **Timeout:** 10 detik

-   **Respons sukses:**

```json
{
  "translatedText": "hasil terjemahan"
}
```

------------------------------------------------------------------------

## Riwayat Terjemahan

Semua riwayat disimpan pada file:
```
h56_history.log
```

Format log:

```
[2025-01-28 13:22:45] FROM: Hello | TO (id) = Halo | CountryID: MY
```

Pengguna dapat melihat riwayat melalui menu:
```
2. Lihat Riwayat Terjemahan
```

------------------------------------------------------------------------

## Troubleshooting

| Masalah | Penyebab | Solusi |
|---|---|---|
| API Timeout | Internet lambat / API down | Coba ulangi setelah beberapa detik |
| Teks kosong | Input kurang valid | Masukkan teks minimal 1 karakter |
| Kode bahasa salah | Salah ketik kode | Lihat tabel bahasa pada menu |
| Terminal tidak bersih | Sistem tidak mendukung `cls/clear` | Jalankan manual `clear` atau `cls` |

------------------------------------------------------------------------

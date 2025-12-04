# Multi-Language Translation CLI Program (MLTCP)

Program ini adalah aplikasi **Command Line Interface (CLI)** berbasis
Python yang berfungsi untuk menerjemahkan teks ke berbagai bahasa
menggunakan **H56 Translator API**. Aplikasi ini didesain dengan
tampilan tabel ASCII yang rapi sehingga pengalaman penggunaan terasa
lebih terstruktur dan mudah dibaca.

------------------------------------------------------------------------

## Daftar Isi

1.  [Pendahuluan](#pendahuluan)
2.  [Fitur Utama](#fitur-utama)
3.  [Struktur Program](#struktur-program)
4.  [Instalasi](#instalasi)
5.  [Menjalankan Program](#menjalankan-program)
6.  [Cara Menggunakan](#cara-menggunakan)
7.  [Dokumentasi API](#dokumentasi-api)
8.  [Troubleshooting](#troubleshooting)

------------------------------------------------------------------------

## Pendahuluan

Program ini dibuat untuk memudahkan pengguna dalam menerjemahkan teks
dari bahasa apa pun ke beberapa bahasa yang didukung melalui antarmuka
terminal. Dengan memanfaatkan API pihak ketiga, aplikasi ini
memungkinkan pengguna mendapat hasil terjemahan secara cepat dan
praktis.

------------------------------------------------------------------------

## Fitur Utama

-   **Antarmuka ASCII yang rapi** menggunakan tabel untuk menu dan hasil
    terjemahan.
-   **Dukungan banyak bahasa**, yaitu:
    -   `id` --- Indonesia
    -   `en` --- English
    -   `ja` --- Japanese
    -   `ko` --- Korean
    -   `ar` --- Arabic
-   **Input ID negara (opsional)**, ditampilkan dalam hasil terjemahan.
-   **Penanganan error** saat API gagal diakses atau terjadi timeout.
-   **Pembersihan layar otomatis** agar tampilan tetap bersih dan
    profesional.

------------------------------------------------------------------------

## Struktur Program

Berikut fungsi-fungsi utama dalam kode:

  -----------------------------------------------------------------------
  Fungsi                        Deskripsi
  ----------------------------- -----------------------------------------
  `main_menu()`                 Menampilkan menu utama dan memproses
                                pilihan pengguna.

  `start_translation()`         Mengatur alur input pengguna dan
                                menampilkan hasil terjemahan.

  `translate(text, target)`     Mengirim permintaan POST ke API untuk
                                menerjemahkan teks.

  `show_languages()`            Menampilkan daftar bahasa yang tersedia.

  `line(width)`                 Membuat garis pemisah tabel ASCII.

  `row(text, width)`            Membuat baris isi tabel ASCII.

  `clear()`                     Membersihkan layar terminal
                                (Windows/Linux/Mac).
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Instalasi

### 1. Pastikan Python Terinstal

Program ini menggunakan **Python 3.7+**.

Cek dengan:

``` bash
python --version
```

### 2. Install Dependensi

Hanya membutuhkan modul eksternal berikut:

``` bash
pip install requests
```

### 3. (Opsional) Clone Repo

``` bash
git https://github.com/HASYIM56/translator-python-rest-api-cli.git
cd translator-project
translator.py
```

------------------------------------------------------------------------

## Menjalankan Program

Jalankan program melalui terminal:

``` bash
python translator.py
```

Ganti `translator.py` jika nama file berbeda.

------------------------------------------------------------------------

## Cara Menggunakan

### 1. Buka program

Akan muncul menu utama seperti:

    +--------------------------------------------------+
    | PROGRAM TERJEMAHAN MULTI-BAHASA                  |
    +--------------------------------------------------+
    | 1. Mulai Terjemahkan                             |
    | 2. Keluar Program                                |
    +--------------------------------------------------+

### 2. Pilih menu **1** untuk mulai menerjemahkan.

### 3. Masukkan teks yang ingin diterjemahkan.

Contoh:

    Masukkan teks yang mau diterjemahkan : Hello, how are you?

### 4. Pilih bahasa target dari daftar seperti:

    id = Indonesia
    en = English
    ja = Japanese
    ko = Korean
    ar = Arabic

### 5. (Opsional) Masukkan ID negara.

### 6. Hasil terjemahan akan ditampilkan dalam tabel ASCII.

------------------------------------------------------------------------

## Dokumentasi API

Program ini menggunakan API penerjemah publik:

-   **Endpoint**

        POST https://h56-translator-api.vercel.app/api/translate

-   **Payload**

    ``` json
    {
      "text": "teks yang akan diterjemahkan",
      "targetLang": "kode_bahasa"
    }
    ```

-   **Headers**

        Content-Type: application/json

-   **Timeout:** 5 detik

-   **Respons sukses:**

    ``` json
    {
      "translatedText": "hasil terjemahan"
    }
    ```

------------------------------------------------------------------------

## Troubleshooting

  ------------------------------------------------------------------------
  Masalah                 Penyebab                   Solusi
  ----------------------- -------------------------- ---------------------
  API Timeout             Internet lambat / API down Coba ulangi setelah
                                                     beberapa detik

  Teks kosong             Input kurang valid         Masukkan teks minimal
                                                     1 karakter

  Kode bahasa salah       Salah ketik kode           Lihat tabel bahasa
                                                     pada menu

  Terminal tidak bersih   Sistem tidak mendukung     Jalankan manual
                          `cls/clear`                `clear` atau `cls`
  

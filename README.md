<!-- Project Title -->
![project](https://img.shields.io/badge/MLTCP-Multi--Language%20Translation%20CLI%20Program-0A84FF?logo=python&logoColor=white&style=for-the-badge&logoWidth=30)

<!-- Version -->
![version](https://img.shields.io/badge/Version-1.0.4-blue?style=for-the-badge&logoWidth=30)

<!-- Python Support -->
![python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white&style=for-the-badge&logoWidth=30)

<!-- Platform -->
![platform](https://img.shields.io/badge/Platform-CLI-lightgrey?style=for-the-badge&logoWidth=30)

<!-- License -->
![license](https://img.shields.io/badge/License-Apache--2.0-green?style=for-the-badge&logoWidth=30)

<!-- Status -->
![status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge&logoWidth=30)

<p align="center">
  <a href="https://github.com/HASYIM56/translator-python-rest-api-cli">
    <img src="/assets/logo.png" alt="Logo Project" width="180" />
  </a>
</p>

# Multi-Language Translation CLI Program (MLTCP)

Program ini adalah aplikasi **Command Line Interface (CLI)** berbasis Python yang berfungsi untuk menerjemahkan teks ke berbagai bahasa menggunakan **H56 Translator API**. Aplikasi ini didesain dengan tampilan tabel ASCII yang rapi sehingga pengalaman penggunaan terasa lebih terstruktur dan mudah dibaca.

---

## Daftar Isi
1. Pendahuluan
2. Fitur Utama
3. Fitur Baru
4. Mode Translate V2 (Slang/Informal)
5. Struktur Program
6. Instalasi
7. Menjalankan Program
8. Cara Menggunakan
9. Dokumentasi API
10. Riwayat Terjemahan
11. Troubleshooting
12. Struktur Folder Program

---

## Pendahuluan
Program ini dibuat untuk memudahkan pengguna dalam menerjemahkan teks dari bahasa apa pun ke beberapa bahasa yang didukung melalui antarmuka terminal. Dengan memanfaatkan API pihak ketiga, aplikasi ini memungkinkan pengguna mendapat hasil terjemahan secara cepat dan praktis.

---

## Fitur Utama
- **Antarmuka ASCII yang rapi** menggunakan tabel untuk menu dan hasil terjemahan.
- **Dukungan banyak bahasa**, yaitu:
  - `id`  Indonesia
  - `en`  English
  - `ja`  Japanese
  - `ko`  Korean
  - `ar`  Arabic
  - `fr`  French
  - `de`  German
  - `es`  Spanish
  - `ru`  Russian
  - `zh`  Chinese (Mandarin)
- **Input ID negara (opsional)**, ditampilkan dalam hasil terjemahan.
- **Penanganan error** saat API gagal diakses atau terjadi timeout.
- **Pembersihan layar otomatis** agar tampilan tetap bersih.

---

## Fitur Baru

### Fitur Tambahan Berdasarkan Kode Python Terbaru
Program kini mendukung **Mode Translasi V2**, yaitu fitur terjemahan dengan gaya bahasa slang / informal. Semua teks di bawah ini ditambahkan tanpa menghapus teks lama.

**Fitur-fitur baru berdasarkan kode Python:**
- **Mode Translate V2** dengan pilihan gaya:
  - `slang`
  - `informal`
  - `slang_v2`
  - `informal_slang_v2`
- Mendukung fungsi API baru:
  - `translate_v1()`  Mode normal
  - `translate_v2()`  Mode slang/informal
- Penambahan menu baru: **Show Modes** untuk menampilkan daftar mode V2.
- Penyimpanan riwayat kini mencatat:
  - Mode translasi (V1 / V2)
  - Mode detail jika menggunakan V2
- Perbaikan tampilan tabel untuk output V2.
- Struktur input lebih lengkap: teks, bahasa target, mode translasi, dan ID negara.
- API endpoint tambahan:
  - `https://h56-translator-api.vercel.app/api/translate/v2`

---

## Fitur Baru (Asli Dari File) (Diperbarui)
### 1. Mode Translate V2 (Slang/Informal)
Program kini mendukung **Mode Translasi V2** dengan variasi gaya bahasa:
- `slang` Casual Slang
- `informal` Informal
- `slang_v2` Slang V2
- `informal_slang_v2` Informal Slang V2

Fitur ini sangat berguna untuk menghasilkan terjemahan dengan nuansa lebih santai, gaul, atau tidak formal.

### 2. Sistem Log Riwayat yang Lebih Lengkap
File log `h56_history.log` kini menyimpan:
- Teks asli
- Teks hasil terjemahan
- Bahasa target
- Mode translasi (V1 / V2 + jenis mode)
- ID negara (opsional)
- Timestamp

### 3. Menu Riwayat Terjemahan
Pengguna dapat melihat daftar lengkap riwayat sebelumnya melalui menu khusus.

### 4. Dua Metode API
Program mengakses dua endpoint:
- **V1 (Normal)**: Terjemahan standar
- **V2 (Slang/Informal)**: Terjemahan dengan style khusus

### 5. Validasi Input Lengkap
- Cek teks kosong
- Cek kode bahasa valid
- Cek mode translasi valid untuk V2
- Fitur `back` untuk kembali ke menu sebelumnya

---

## Mode Translate V2 (Detail)
Fitur V2 menyediakan kemampuan menerjemahkan menggunakan gaya bahasa yang lebih fleksibel.

Daftar mode lengkap:
| Kode | Deskripsi |
|------|-----------|
| `slang` | Terjemahan slang santai |
| `informal` | Terjemahan informal umum |
| `slang_v2` | Slang tingkat lanjutan |
| `informal_slang_v2` | Campuran informal + slang |

Format request V2 menggunakan field tambahan `translationMode`.

---

## Struktur Program
Berikut fungsi-fungsi utama dalam kode:
| Fungsi | Deskripsi |
|--------|-----------|
| `main_menu()` | Menampilkan menu utama. |
| `start_translation()` | Mengatur input dan pemrosesan terjemahan. |
| `translate_v1(text, target)` | API translator mode biasa. |
| `translate_v2(text, target, mode)` | API translator mode slang/informal. |
| `show_languages()` | Menampilkan daftar bahasa. |
| `show_modes()` | Menampilkan mode V2. |
| `log_history()` | Menyimpan riwayat ke file log. |
| `show_history()` | Menampilkan riwayat dari file log. |
| `line()` & `row()` | Membuat elemen tabel ASCII. |
| `clear()` | Membersihkan layar terminal. |

---

## Instalasi
### 1. Pastikan Python Terinstal
```bash
python --version
```

### 2. Install Dependensi
```bash
pip install requests
```

### 3. (Opsional) Clone Repo
```bash
git clone https://github.com/HASYIM56/translator-python-rest-api-cli.git
cd translator-project
```

---

## Menjalankan Program
```bash
python translator.py
```

---

## Cara Menggunakan
1. Jalankan program.
2. Pilih menu utama.
3. Masukkan teks.
4. Pilih bahasa target.
5. Pilih mode translasi (V1 atau V2).
6. (Opsional) Masukkan ID negara.
7. Hasil akan ditampilkan dalam tabel ASCII.

---

## Dokumentasi API

### Penambahan Dokumentasi API Mode V2
API baru yang digunakan program berdasarkan kode Python terbaru:

#### **Endpoint V2** Mode Slang / Informal
```
POST https://h56-translator-api.vercel.app/api/translate/v2
```
Payload:
```json
{
  "text": "teks yang akan diterjemahkan",
  "targetLang": "kode_bahasa",
  "translationMode": "slang | informal | slang_v2 | informal_slang_v2"
}
```
Respons:
```json
{
  "translatedText": "hasil terjemahan"
}
```

---

## Dokumentasi API (Asli Dari File)
### **V1 Endpoint Normal**
```
POST https://h56-translator-api.vercel.app/api/translate
```
Payload:
```json
{
  "text": "teks contoh",
  "targetLang": "id"
}
```
Respons:
```json
{
  "translatedText": "hasil"
}
```

### **V2 Endpoint Slang/Informal**
```
POST https://h56-translator-api.vercel.app/api/translate/v2
```
Payload:
```json
{
  "text": "teks contoh",
  "targetLang": "id",
  "translationMode": "slang"
}
```

---

## Riwayat Terjemahan
Semua riwayat disimpan ke:
```
h56_history.log
```
Format:
```
[YYYY-MM-DD HH:MM:SS] MODE: v2 | FROM: Hello | TO (id) = Halo | CountryID: MY
```

---

## Troubleshooting
| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| Timeout API | Server sibuk / internet lambat | Coba ulangi beberapa saat |
| Input kosong | Pengguna menekan Enter tanpa teks | Masukkan teks minimal 1 karakter |
| Bahasa tidak valid | Kode tidak ada di daftar | Cek kembali daftar bahasa |
| Mode V2 salah | Salah mengetik kode | Gunakan menu daftar mo


---

## Struktur Folder Program

Struktur direktori proyek berdasarkan implementasi kode saat ini adalah sebagai berikut:

```
project/
 translator.py
 history.py
 history_translate/
    h56_history.log
```

**Penjelasan singkat:**
- `translator.py`  
  File utama aplikasi CLI, berisi menu, logika translasi, pemilihan bahasa, mode V1/V2, serta integrasi API.
- `history.py`  
  Modul pendukung untuk mencatat, membaca, dan menampilkan riwayat terjemahan secara terstruktur.
- `history_translate/`  
  Folder penyimpanan histori terjemahan.
- `h56_history.log`  
  File log yang menyimpan semua riwayat translasi lengkap dengan timestamp, mode, bahasa target, dan ID negara.

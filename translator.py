import requests
import json
import os

# Fungsi membuat garis pemisah tabel
def line(width):
    return "+" + "-" * width + "+"

# Fungsi membuat baris teks tabel
def row(text, width):
    return "| " + text.ljust(width - 2) + "|"

# Lebar tabel
W = 50

# Daftar bahasa yang didukung
LANGUAGES = {
    "id": "Indonesia",
    "en": "English",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic"
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_languages():
    print("\n" + line(W))
    print(row("TABEL PILIHAN BAHASA", W))
    print(line(W))
    for code, name in LANGUAGES.items():
        print(row(f"{code} = {name}", W))
    print(line(W))

def translate(text, target):
    url = "https://h56-translator-api.netlify.app/api/translate"
    payload = {"text": text, "targetLang": target}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=5)
        data = response.json()
        return data.get("translatedText", "(gagal menerjemahkan)")
    except Exception as e:
        return f"Error: {str(e)}"

def main_menu():
    while True:
        clear()
        print(line(W))
        print(row("PROGRAM TERJEMAHAN MULTI-BAHASA", W))
        print(line(W))
        print(row("1. Mulai Terjemahkan", W))
        print(row("2. Keluar Program", W))
        print(line(W))

        choice = input("\nPilih menu (1/2): ").strip()

        if choice == "1":
            start_translation()
        elif choice == "2":
            print("\nKeluar program...")
            break
        else:
            print("\nInput tidak valid! Tekan Enter untuk kembali...")
            input()

def start_translation():
    clear()
    print(line(W))
    print(row("TABEL INPUT TERJEMAHAN", W))
    print(line(W))

    input_text = input("Masukkan teks yang mau diterjemahkan : ").strip()
    if not input_text:
        print("\nTeks tidak boleh kosong. Tekan Enter untuk kembali...")
        input()
        return

    # Pilih bahasa target
    while True:
        show_languages()
        target_lang = input("Masukkan bahasa target : ").strip().lower()

        if target_lang in LANGUAGES:
            break
        else:
            print("\nKode bahasa salah! Coba lagi atau ketik 'back' untuk kembali.")
            if target_lang == "back":
                return

    country_id = input("Masukan ID negara (opsional): ")

    # Proses API
    translated_text = translate(input_text, target_lang)

    # Output tabel hasil
    clear()
    print(line(W))
    print(row("HASIL TERJEMAHAN", W))
    print(line(W))
    print(row(f"Teks Asli      : {input_text}", W))
    print(row(f"Bahasa Target  : {target_lang} ({LANGUAGES[target_lang]})", W))
    print(row(f"ID Negara      : {country_id}", W))
    print(line(W))
    print(row("OUTPUT:", W))
    print(line(W))
    print(row(translated_text, W))
    print(line(W))

    input("\nTekan Enter untuk kembali ke menu...")

# ============================
#   JALANKAN PROGRAM
# ============================

main_menu()

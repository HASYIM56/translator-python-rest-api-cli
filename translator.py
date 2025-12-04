import requests
import json
import os
import datetime

# ====================================================
#               CONFIG & GLOBAL VARIABLE
# ====================================================

LOG_FILE = "h56_history.log"

# Lebar tabel
W = 60

# Daftar bahasa yang didukung
LANGUAGES = {
    "id": "Indonesia",
    "en": "English",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "ru": "Russian",
    "zh": "Chinese (Mandarin)"
}

# ====================================================
#                      UTILITIES
# ====================================================

def line(width):
    return "+" + "-" * width + "+"

def row(text, width):
    if len(text) > width - 2:
        text = text[:width-5] + "..."
    return "| " + text.ljust(width - 2) + "|"

def clear():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except:
        pass

def log_history(original, translated, lang, country_id):
    """Menyimpan riwayat ke file log"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] FROM: {original} | TO ({lang}) = {translated} | CountryID: {country_id}\n")

def show_history():
    clear()
    print(line(W))
    print(row("RIWAYAT TERJEMAHAN", W))
    print(line(W))

    if not os.path.exists(LOG_FILE):
        print("Belum ada riwayat tersimpan.\n")
    else:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.readlines()
            if len(logs) == 0:
                print("Belum ada riwayat.\n")
            else:
                for log in logs:
                    print(log.strip())

    input("\nTekan Enter untuk kembali ke menu...")


# ====================================================
#                      MAIN FEATURES
# ====================================================

def show_languages():
    print("\n" + line(W))
    print(row("TABEL PILIHAN BAHASA", W))
    print(line(W))
    for code, name in LANGUAGES.items():
        print(row(f"{code} = {name}", W))
    print(line(W))

def translate(text, target):
    url = "https://h56-translator-api.vercel.app/api/translate"
    payload = {"text": text, "targetLang": target}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        try:
            data = response.json()
        except:
            return "(Server tidak mengirim respons JSON valid!)"

        return data.get("translatedText", "(Gagal menerjemahkan, respons tidak lengkap!)")

    except Exception as e:
        return f"Error: {str(e)}"


# ====================================================
#                    PROGRAM INTERFACE
# ====================================================

def start_translation():
    clear()
    print(line(W))
    print(row("TABEL INPUT TERJEMAHAN", W))
    print(line(W))

    # Input teks
    input_text = input("Masukkan teks yang mau diterjemahkan : ").strip()
    if not input_text:
        print("\nTeks tidak boleh kosong. Tekan Enter untuk kembali...")
        input()
        return

    # Pilih bahasa target
    while True:
        show_languages()
        target_lang = input("Masukkan bahasa target : ").strip().lower()

        if target_lang == "back":
            return

        if target_lang in LANGUAGES:
            break
        else:
            print("\nKode bahasa salah! Coba lagi atau ketik 'back' untuk kembali.")

    country_id = input("Masukkan ID negara (opsional): ")

    # Proses API
    translated_text = translate(input_text, target_lang)

    # Simpan ke log
    log_history(input_text, translated_text, target_lang, country_id)

    # OUTPUT
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

def main_menu():
    while True:
        clear()
        print(line(W))
        print(row("PROGRAM TERJEMAHAN MULTI-BAHASA", W))
        print(line(W))
        print(row("1. Mulai Terjemahkan", W))
        print(row("2. Lihat Riwayat Terjemahan", W))
        print(row("3. Keluar Program", W))
        print(line(W))

        choice = input("\nPilih menu (1/2/3): ").strip()

        if choice == "1":
            start_translation()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("\nKeluar program...")
            break
        else:
            print("\nInput tidak valid! Tekan Enter untuk kembali...")
            input()


# ============================
#       JALANKAN PROGRAM
# ============================

if __name__ == "__main__":
    main_menu()    url = "https://h56-translator-api.vercel.app/api/translate"
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

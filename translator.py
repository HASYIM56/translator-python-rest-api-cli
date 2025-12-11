import requests
import json
import os
import datetime

# ====================================================
# CONFIG & GLOBAL VARIABLE
# ====================================================

LOG_FILE = "h56_history.log"
W = 60  # Lebar tabel

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

# Mode Translate V2
TRANSLATE_MODES = {
    "slang": "Casual Slang",
    "informal": "Informal",
    "slang_v2": "Slang V2",
    "informal_slang_v2": "Informal Slang V2"
}

# ====================================================
# UTILITIES
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

def log_history(original, translated, lang, country_id, mode):
    """Menyimpan riwayat ke file log"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(
            f"[{timestamp}] MODE: {mode} | FROM: {original} | "
            f"TO ({lang}) = {translated} | CountryID: {country_id}\n"
        )

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
# API FUNCTION
# ====================================================

def translate_v1(text, target):
    """Translator Mode V1"""
    url = "https://h56-translator-api.vercel.app/api/translate"
    payload = {"text": text, "targetLang": target}

    try:
        resp = requests.post(url, json=payload, timeout=10)
        data = resp.json()
        return data.get("translatedText", "(Gagal menerjemahkan!)")
    except:
        return "(Error koneksi ke server)"

def translate_v2(text, target, mode):
    """Translator Mode V2 + Slang/Informal"""
    url = "https://h56-translator-api.vercel.app/api/translate/v2"
    payload = {
        "text": text,
        "targetLang": target,
        "translationMode": mode
    }

    try:
        resp = requests.post(url, json=payload, timeout=10)
        data = resp.json()
        return data.get("translatedText", "(Gagal menerjemahkan!)")
    except:
        return "(Error koneksi ke server)"

# ====================================================
# MAIN FEATURES
# ====================================================

def show_languages():
    print("\n" + line(W))
    print(row("TABEL PILIHAN BAHASA", W))
    print(line(W))
    for code, name in LANGUAGES.items():
        print(row(f"{code} = {name}", W))
        print(line(W))

def show_modes():
    print("\n" + line(W))
    print(row("MODE TRANSLATE V2", W))
    print(line(W))
    for code, name in TRANSLATE_MODES.items():
        print(row(f"{code} = {name}", W))
        print(line(W))

# ====================================================
# PROGRAM INTERFACE
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
            print("\nKode bahasa salah!")

    # Pilih mode translate
    print("\nPILIH MODE TRANSLASI:")
    print("1. Mode Normal (V1)")
    print("2. Mode Slang/Informal (V2)")

    mode_select = input("Pilih mode (1/2): ").strip()

    mode_used = "v1"
    selected_mode = None

    if mode_select == "2":
        mode_used = "v2"
        while True:
            show_modes()
            selected_mode = input("Masukkan mode V2: ").strip().lower()

            if selected_mode in TRANSLATE_MODES:
                break
            else:
                print("Kode mode salah!")

    country_id = input("Masukkan ID negara (opsional): ")

    # Proses API
    if mode_used == "v1":
        translated_text = translate_v1(input_text, target_lang)
    else:
        translated_text = translate_v2(input_text, target_lang, selected_mode)

    # Simpan log
    log_history(input_text, translated_text, target_lang, country_id, mode_used)

    # Output
    clear()
    print(line(W))
    print(row("HASIL TERJEMAHAN", W))
    print(line(W))
    print(row(f"Teks Asli      : {input_text}", W))
    print(row(f"Bahasa Target  : {target_lang} ({LANGUAGES[target_lang]})", W))
    print(row(f"Mode           : {mode_used.upper()}", W))
    if mode_used == "v2":
        print(row(f"V2 Mode        : {selected_mode}", W))
    print(row(f"ID Negara      : {country_id}", W))
    print(line(W))
    print(row("OUTPUT:", W))
    print(line(W))
    print(row(translated_text, W))
    print(line(W))

    input("\nTekan Enter untuk kembali ke menu...")

# ====================================================
# MENU UTAMA
# ====================================================

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

# ====================================================
# JALANKAN PROGRAM
# ====================================================

if __name__ == "__main__":
    main_menu()    if len(text) > width - 2:
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

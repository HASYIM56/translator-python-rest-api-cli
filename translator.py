import requests
import json
import os
import datetime
import shutil

# ====================================================
# CONFIG & GLOBAL VARIABLES
# ====================================================

LOG_FILE = "h56_history.log"

def get_terminal_width(default=60):
    """Menentukan lebar tabel dinamis sesuai terminal"""
    try:
        width = shutil.get_terminal_size().columns
        return min(max(width, 40), 100)  # Batas aman
    except:
        return default

W = get_terminal_width()

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

def line(width=W):
    return "+" + "-" * (width - 2) + "+"

def row(text, width=W):
    text = str(text)
    if len(text) > width - 4:
        text = text[:width - 7] + "..."
    return "| " + text.ljust(width - 4) + " |"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="\nTekan Enter untuk kembali ke menu..."):
    input(msg)

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
    print(line())
    print(row("RIWAYAT TERJEMAHAN"))
    print(line())

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

    pause()


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
    print("\n" + line())
    print(row("TABEL PILIHAN BAHASA"))
    print(line())
    for code, name in LANGUAGES.items():
        print(row(f"{code} = {name}"))
    print(line())

def show_modes():
    print("\n" + line())
    print(row("MODE TRANSLATE V2"))
    print(line())
    for code, name in TRANSLATE_MODES.items():
        print(row(f"{code} = {name}"))
    print(line())


# ====================================================
# PROGRAM INTERFACE
# ====================================================

def start_translation():
    clear()
    print(line())
    print(row("TABEL INPUT TERJEMAHAN"))
    print(line())

    input_text = input("Masukkan teks yang mau diterjemahkan : ").strip()
    if not input_text:
        print("\nTeks tidak boleh kosong.")
        pause()
        return

    # Pilih bahasa target
    while True:
        show_languages()
        target_lang = input("Masukkan bahasa target (atau ketik 'back' untuk kembali): ").strip().lower()
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

    country_id = input("Masukkan ID negara (opsional): ").strip()

    # Proses API
    print("\nMemproses terjemahan, harap tunggu...\n")
    if mode_used == "v1":
        translated_text = translate_v1(input_text, target_lang)
    else:
        translated_text = translate_v2(input_text, target_lang, selected_mode)

    # Simpan log
    log_history(input_text, translated_text, target_lang, country_id, mode_used)

    # Output
    clear()
    print(line())
    print(row("HASIL TERJEMAHAN"))
    print(line())
    print(row(f"Teks Asli      : {input_text}"))
    print(row(f"Bahasa Target  : {target_lang} ({LANGUAGES[target_lang]})"))
    print(row(f"Mode           : {mode_used.upper()}"))
    if mode_used == "v2":
        print(row(f"V2 Mode        : {selected_mode}"))
    print(row(f"ID Negara      : {country_id if country_id else '-'}"))
    print(line())
    print(row("OUTPUT:"))
    print(line())
    print(row(translated_text))
    print(line())

    pause()


# ====================================================
# MAIN MENU
# ====================================================

def main_menu():
    while True:
        clear()
        print(line())
        print(row("PROGRAM TERJEMAHAN MULTI-BAHASA"))
        print(line())
        print(row("1. Mulai Terjemahkan"))
        print(row("2. Lihat Riwayat Terjemahan"))
        print(row("3. Keluar Program"))
        print(line())

        choice = input("\nPilih menu (1/2/3): ").strip()

        if choice == "1":
            start_translation()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("\nKeluar program...")
            break
        else:
            print("\nInput tidak valid!")
            pause()


# ====================================================
# RUN PROGRAM
# ====================================================

if __name__ == "__main__":
    main_menu()

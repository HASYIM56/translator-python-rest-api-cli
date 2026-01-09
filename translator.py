import requests
import os
import shutil

# IMPORT MODULE HISTORY
import history

# ====================================================
# COLOR SYSTEM (BRIGHT GREEN)
# ====================================================

class Color:
    GREEN = "\033[92m"
    RESET = "\033[0m"

def green(text):
    return f"{Color.GREEN}{text}{Color.RESET}"

# ====================================================
# ASCII ART HEADER
# ====================================================

ASCII_HEADER = r"""
 /$$      /$$ /$$    /$$$$$$$$ /$$$$$$  /$$$$$$$
| $$$    /$$$| $$   |__  $$__//$$__  $$| $$__  $$
| $$$$  /$$$$| $$      | $$  | $$  \__/| $$  \ $$
| $$ $$/$$ $$| $$      | $$  | $$      | $$$$$$$/
| $$  $$$| $$| $$      | $$  | $$      | $$____/
| $$\  $ | $$| $$      | $$  | $$    $$| $$
| $$ \/  | $$| $$$$$$$$| $$  |  $$$$$$/| $$
|__/     |__/|________/|__/   \______/ |__/
"""

def show_header():
    print(green(ASCII_HEADER))

# ====================================================
# CONFIG & GLOBAL VARIABLES
# ====================================================

def get_terminal_width(default=60):
    try:
        width = shutil.get_terminal_size().columns
        return min(max(width, 40), 120)
    except:
        return default

W = get_terminal_width()

# ====================================================
# SUPPORTED LANGUAGES (EXTENDED)
# ====================================================

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
    "zh": "Chinese (Mandarin)",
    "it": "Italian",
    "pt": "Portuguese",
    "tr": "Turkish",
    "th": "Thai",
    "vi": "Vietnamese",
    "pl": "Polish",
    "nl": "Dutch",
    "sv": "Swedish",
    "fi": "Finnish",
    "cs": "Czech",
    "hu": "Hungarian",
    "jv": "Javanese",
    "ms": "Malay",
    "hi": "Hindi",
    "bn": "Bengali",
    "ur": "Urdu",
    "el": "Greek",
    "he": "Hebrew",
    "ro": "Romanian",
    "uk": "Ukrainian"
}

# ====================================================
# TRANSLATION MODES
# ====================================================

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
    return green("+" + "-" * (width - 2) + "+")

def row(text, width=W):
    text = str(text)
    if len(text) > width - 4:
        text = text[:width - 7] + "..."
    return green("| " + text.ljust(width - 4) + " |")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="\nTekan Enter untuk kembali ke menu..."):
    input(green(msg))

# ====================================================
# API FUNCTION
# ====================================================

def translate_v1(text, target):
    url = "https://h56-translator-api.vercel.app/api/translate"
    payload = {"text": text, "targetLang": target}
    try:
        resp = requests.post(url, json=payload, timeout=15)
        return resp.json().get("translatedText", "(Gagal menerjemahkan!)")
    except:
        return "(Error koneksi ke server)"

def translate_v2(text, target, mode):
    url = "https://h56-translator-api.vercel.app/api/translate/v2"
    payload = {
        "text": text,
        "targetLang": target,
        "translationMode": mode
    }
    try:
        resp = requests.post(url, json=payload, timeout=15)
        return resp.json().get("translatedText", "(Gagal menerjemahkan!)")
    except:
        return "(Error koneksi ke server)"

# ====================================================
# DISPLAY HELPERS
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
# DEVELOPER INFO
# ====================================================

def show_developer_info():
    clear()
    show_header()
    print(line())
    print(row("INFORMASI DEVELOPER"))
    print(line())
    print(row("Program ini dibuat oleh HASYIM56"))
    print(row(""))
    print(row("Youtube  : https://youtube.com/@HASYIM56"))
    print(row("Instagram: https://instagram.com/hasyim56_modder"))
    print(row("Github   : https://github.com/HASYIM56"))
    print(line())
    pause()

# ====================================================
# MAIN FEATURES
# ====================================================

def start_translation():
    clear()
    show_header()
    print(line())
    print(row("TABEL INPUT TERJEMAHAN"))
    print(line())

    input_text = input(green("Masukkan teks yang mau diterjemahkan : ")).strip()
    if not input_text:
        print(green("\nTeks tidak boleh kosong."))
        pause()
        return

    while True:
        show_languages()
        target_lang = input(green("Masukkan bahasa target (atau ketik 'back'): ")).strip().lower()
        if target_lang == "back":
            return
        if target_lang in LANGUAGES:
            break
        print(green("\nKode bahasa salah!"))

    print(green("\nPILIH MODE TRANSLASI:"))
    print(green("1. Mode Normal (V1)"))
    print(green("2. Mode Slang/Informal (V2)"))

    mode_select = input(green("Pilih mode (1/2): ")).strip()

    mode_used = "v1"
    selected_mode = None

    if mode_select == "2":
        mode_used = "v2"
        while True:
            show_modes()
            selected_mode = input(green("Masukkan mode V2: ")).strip().lower()
            if selected_mode in TRANSLATE_MODES:
                break
            print(green("Kode mode salah!"))

    country_id = input(green("Masukkan ID negara (opsional): ")).strip()

    print(green("\nMemproses terjemahan...\n"))

    translated_text = (
        translate_v1(input_text, target_lang)
        if mode_used == "v1"
        else translate_v2(input_text, target_lang, selected_mode)
    )

    history.write_history(
        input_text,
        translated_text,
        target_lang,
        country_id,
        mode_used if mode_used == "v1" else selected_mode
    )

    clear()
    show_header()
    print(line())
    print(row("HASIL TERJEMAHAN"))
    print(line())
    print(row(f"Teks Asli     : {input_text}"))
    print(row(f"Bahasa Target : {target_lang} ({LANGUAGES[target_lang]})"))
    print(row(f"Mode          : {mode_used.upper()}"))
    if selected_mode:
        print(row(f"V2 Mode       : {selected_mode}"))
    print(row(f"ID Negara     : {country_id or '-'}"))
    print(line())
    print(row("OUTPUT:"))
    print(line())
    print(row(translated_text))
    print(line())

    pause()

def show_history():
    history.display_history(clear_func=clear, pause_func=pause)

# ====================================================
# MAIN MENU
# ====================================================

def main_menu():
    while True:
        clear()
        show_header()
        print(line())
        print(row("PROGRAM TERJEMAHAN MULTI-BAHASA"))
        print(line())
        print(row("1. Mulai Terjemahkan"))
        print(row("2. Lihat Riwayat Terjemahan"))
        print(row("3. Informasi Developer"))
        print(row("4. Keluar Program"))
        print(line())

        choice = input(green("\nPilih menu (1/2/3/4): ")).strip()

        if choice == "1":
            start_translation()
        elif choice == "2":
            show_history()
        elif choice == "3":
            show_developer_info()
        elif choice == "4":
            print(green("\nKeluar program..."))
            break
        else:
            print(green("\nInput tidak valid!"))
            pause()

# ====================================================
# RUN PROGRAM
# ====================================================

if __name__ == "__main__":
    clear()
    show_header()
    main_menu()

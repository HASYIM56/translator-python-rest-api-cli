import os
import datetime
import shutil

# ====================================================
# CONFIG
# ====================================================

HISTORY_DIR = "history_translate"
LOG_FILE = os.path.join(HISTORY_DIR, "h56_history.log")

# ====================================================
# INIT
# ====================================================

def ensure_history_dir():
    os.makedirs(HISTORY_DIR, exist_ok=True)

def get_terminal_width(default=60):
    try:
        width = shutil.get_terminal_size().columns
        return min(max(width, 50), 120)
    except:
        return default

W = get_terminal_width()

# ====================================================
# TABLE UTIL
# ====================================================

def line():
    return "+" + "-" * (W - 2) + "+"

def row(text=""):
    text = str(text)
    if len(text) > W - 4:
        text = text[:W - 7] + "..."
    return "| " + text.ljust(W - 4) + " |"

# ====================================================
# HISTORY CORE
# ====================================================

def write_history(original, translated, lang, country_id, mode):
    ensure_history_dir()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] | MODE={mode} | "
        f"TARGET={lang} | COUNTRY_ID={country_id or '-'} | "
        f"FROM={original} | TO={translated}\n"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def read_history():
    ensure_history_dir()
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def clear_history():
    ensure_history_dir()
    if os.path.exists(LOG_FILE):
        open(LOG_FILE, "w", encoding="utf-8").close()

# ====================================================
# DISPLAY HISTORY
# ====================================================

def display_history(clear_func=None, pause_func=None):
    while True:
        if clear_func:
            clear_func()

        print(line())
        print(row("RIWAYAT TERJEMAHAN"))
        print(line())
        print(row("Perintah:"))
        print(row(" - ketik 'del'  : Hapus semua history"))
        print(row(" - tekan Enter : Kembali ke menu"))
        print(line())

        logs = read_history()

        if not logs:
            print(row("Belum ada histori tersimpan"))
            print(line())
        else:
            for idx, log in enumerate(logs, 1):
                print(row(f"#{idx}"))
                parts = log.strip().split("|")
                for part in parts:
                    print(row(part.strip()))
                print(line())

        cmd = input("\nCommand > ").strip().lower()

        if cmd == "del":
            confirm = input("Yakin hapus SEMUA history? (y/n): ").lower()
            if confirm == "y":
                clear_history()
                print("\nHistory berhasil dihapus.")
                if pause_func:
                    pause_func()
            continue
        else:
            break

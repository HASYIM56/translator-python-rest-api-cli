import os
import datetime
import shutil

# ====================================================
# CONFIG
# ====================================================

HISTORY_DIR = "history_translate"
LOG_FILE = os.path.join(HISTORY_DIR, "h56_history.log")


def ensure_history_dir():
    """Pastikan folder histori ada"""
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


def display_history(clear_func=None, pause_func=None):
    if clear_func:
        clear_func()

    print(line())
    print(row("RIWAYAT TERJEMAHAN (STRUCTURED VIEW)"))
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

    if pause_func:
        pause_func()

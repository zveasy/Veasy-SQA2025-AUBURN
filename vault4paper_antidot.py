# vault4paper_antidot.py
import os
import shutil
import json

BACKUP_DIR = ".vault_backups"
LOG_FILE = ".vault4paper-log.json"


def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return {}


def restore_files(log_data):
    if not os.path.exists(BACKUP_DIR):
        print("Backup directory not found. Nothing to restore.")
        return

    for original_path, backup_path in log_data.items():
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, original_path)
            print(f"Restored: {original_path}")
        else:
            print(f"Missing backup for: {original_path}")


def main():
    print("Restoring all files modified by vault4paper.py...")
    log_data = load_log()

    if not log_data:
        print("No changes found to revert.")
        return

    restore_files(log_data)
    print("✅ All reversible changes from vault4paper have been restored.")


if __name__ == "__main__":
    main()


import os
import shutil
import json
import re

LOG_FILE = ".vault4paper-log.json"
BACKUP_DIR = ".vault_backups"

def backup_file(file_path):
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    backup_path = os.path.join(BACKUP_DIR, os.path.basename(file_path))
    shutil.copy2(file_path, backup_path)
    log_backup(file_path, backup_path)

def log_backup(original, backup):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            log_data = json.load(f)
    else:
        log_data = {}

    log_data[original] = backup
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

def replace_secrets_in_ansible():
    print("🔍 Scanning Ansible/ for secrets...")
    for root, _, files in os.walk("Ansible"):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()

                modified = False
                new_lines = []
                for line in lines:
                    if "password:" in line:
                        backup_file(file_path)
                        secret_value = line.split("password:")[1].strip()
                        print(f"✅ Replacing secret: {secret_value}")
                        new_lines.append("  password: {{ vault_secret }}\n")
                        modified = True
                    else:
                        new_lines.append(line)

                if modified:
                    with open(file_path, "w") as f:
                        f.writelines(new_lines)
                        print(f"🔐 Updated: {file_path}")

replace_secrets_in_ansible()

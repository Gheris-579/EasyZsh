import json
import os
import getpass

CONFIG_FILE = 'config.json'


def load_settings():
    if not os.path.exists(CONFIG_FILE):
        # RECUPERA IL NOME REALE DEL SISTEMA
        system_user = getpass.getuser()

        default = {
            "user_name": system_user,  # <--- Ora salva il nome vero!
            "is_zsh_installed": False,
            "last_update": "Mai",
            "selected_theme": "robbyrussell"
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default, f, indent=4)
        return default

    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

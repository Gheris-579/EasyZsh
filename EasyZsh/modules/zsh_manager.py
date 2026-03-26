# <-- Gestisce tutto ciò che riguarda la shell Zsh, Oh My Zsh e i plugin.
import os
import re
import time
import subprocess
from pathlib import Path
from datetime import datetime
import shutil
import getpass


import modules.art as art
import modules.core as core
import modules.config_manager as config_manager




# NUMERO 3
def install_zsh():
    username = getpass.getuser()
    # Nota: installzsh_banners deve essere il nome esatto in art.py
    core.run_task(
        "installzsh_banners",
        ["sudo", "apt", "install", "zsh", "-y"],
        "Installation complete. Verification in progress..."
    )
    core.run_task(
        "installzsh_banners",
        ["zsh", "--version"],
        "Zsh is ready!"
    )

    # Cambio della shell di default
    core.run_task(
        "installzsh_banners",
        ["sudo", "chsh", "-s", "/usr/bin/zsh", username],
        "Shell changed! Remember to restart your session."
    )

    # AGGIORNAMENTO DEL JSON (Il tocco da Pro)
    config_manager.update_setting("is_zsh_installed", True)

    print(f"""\n
    ============= ⚠️ Logout and login are required after this command. Verify: ==========\n
        After opening the terminal, you will see some options.

        1 → continue with the setup
        2 → create an empty .zshrc file
        0 → exit

        {art.Re}You need to choose (2).{art.Wh}

        Then check that everything is correct with this command:
        {art.Gr}echo $SHELL{art.Wh}

        Correct output:
        {art.Gr}/usr/bin/zsh{art.Wh}

        If everything is correct, run the program again for the next setup steps.
    """)
    input("\nPress Enter to return to the menu...")

# NUMERO 4
def install_oh_my_zsh():
    # 1. Mostra il banner specifico dai tuoi 11
    art.clear()
    print(art.banners_zshplugin)  # Il banner che hai scelto

    print(f"""{art.Blu}
    !Do you want to overwrite it with the Oh My Zsh template? [Y/n]!{art.Wh}
    {art.Gr}Recommended choice for first-time setup: press Y.{art.Wh}
    {art.Re}Choose n only if you already have a custom .zshrc file.{art.Wh}
    """)

    input(f"{art.Gr}When you have finished reading the message above, press Enter.  {art.Wh} --> ")

    try:
        # 2. Comando "Silent" (RUNZSH=no impedisce a Zsh di aprirsi subito chiudendo lo script)
        cmd = 'RUNZSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
        subprocess.run(cmd, shell=True, check=True)

        # 3. Aggiorna la memoria del programma
        config_manager.update_setting("oh_my_zsh_installed", True)

        print("\n✅ Oh My Zsh installed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error during installation: {e}")

    time.sleep(2)
    input("\nPress Enter to return to the menu...")

# NUMERO 5
def install_zsh_autosuggestions():
    # 1. Pulisce e mostra il banner specifico (da art.py)
    art.clear()
    print(art.banners_autosuggestions)

    # 2. Trova il percorso corretto dei plugin di Oh My Zsh
    zsh_custom = os.environ.get("ZSH_CUSTOM", os.path.expanduser("~/.oh-my-zsh/custom"))
    plugin_path = os.path.join(zsh_custom, "plugins", "zsh-autosuggestions")

    # 3. Controllo: il plugin è già presente?
    if os.path.exists(plugin_path):
        print(f"\n⚠️ The 'zsh-autosuggestions' plugin is already installed in: {plugin_path}")
        time.sleep(2)
        return

    print("🚀 Cloning the zsh-autosuggestions plugin...")

    try:
        subprocess.run(
            [
                "git",
                "clone",
                "https://github.com/zsh-users/zsh-autosuggestions",
                plugin_path
            ],
            check=True
        )
        print("\n✅ Plugin installed successfully!")

        # Aggiorna il JSON per ricordarsi che il plugin è presente
        config_manager.update_setting("autosuggestions_installed", True)

    except subprocess.CalledProcessError:
        print("\n❌ Error installing plugin.")

    time.sleep(2)


# NUMERO 6
def install_syntax_highlighting():
    # 1. Grafica e Banner (da art.py)
    art.clear()
    print(art.banners_zshsyntax_highlighter)

    # 2. Percorsi dinamici per Oh My Zsh
    zsh_custom = os.environ.get("ZSH_CUSTOM", os.path.expanduser("~/.oh-my-zsh/custom"))
    plugin_path = os.path.join(zsh_custom, "plugins", "zsh-syntax-highlighting")

    # 3. Controllo anti-errore (Se esiste già, non clonare)
    if os.path.exists(plugin_path):
        print("\n⚠️ The 'zsh-syntax-highlighting' plugin is already installed.")
        time.sleep(2)
        return

    print("🚀 Syntax Highlighting installation in progress...")

    try:
        subprocess.run(
            [
                "git",
                "clone",
                "https://github.com/zsh-users/zsh-syntax-highlighting",
                plugin_path
            ],
            check=True
        )
        print("\n✅ Syntax Highlighting installed successfully!")

        # 4. Aggiorna la memoria del programma
        config_manager.update_setting("syntax_highlighting_installed", True)

    except subprocess.CalledProcessError:
        print("\n❌ Error while downloading the plugin.")

    time.sleep(2)
    input("\nPress Enter to return to the menu...")

# NUMERO 7
def backup_zshrc():
    # 1. Pulisce e mostra il banner (da art.py)
    art.clear()
    print(art.banners_zshplugin)

    zshrc_path = Path.home() / ".zshrc"

    if zshrc_path.exists():
        # 2. Crea un timestamp leggibile (es: 2023-10-27_14-30-05)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_path = Path.home() / f".zshrc.backup-{timestamp}"

        try:
            # 3. Copia mantenendo i metadati (permessi, date)
            shutil.copy2(zshrc_path, backup_path)
            print(f"\n✅ Backup created successfully: {backup_path}")
            print("You can now safely edit the .zshrc file.")
        except Exception as e:
            print(f"\n❌ Error during backup: {e}")
    else:
        print("\n⚠️ .zshrc file not found. Nothing to back up.")

    input("\nPress Enter to return to the menu...")

#  NUMERO 8
def setup_user_zsh():
    art.clear()
    print(art.banners_zshplugin)

    user_home = Path.home()
    user_zshrc = user_home / ".zshrc"
    user_ohmyzsh = user_home / ".oh-my-zsh"
    user_plugins_dir = user_ohmyzsh / "custom" / "plugins"

    # ---------- CHECK BASE ----------
    if not user_zshrc.exists():
        print("❌ USER .zshrc not found. Install Zsh first.")
        input("\nPress Enter to return to menu...")
        return

    if not user_ohmyzsh.exists():
        print("❌ USER Oh My Zsh not found. Install Oh My Zsh first.")
        input("\nPress Enter to return to menu...")
        return

    try:
        content = user_zshrc.read_text(encoding="utf-8")

        # ---------- PLUGINS ----------
        new_plugins = "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)"

        if "plugins=(git)" in content:
            content = content.replace("plugins=(git)", new_plugins)
        elif "plugins=(" in content:
            content = re.sub(r"plugins=\([^)]+\)", new_plugins, content, count=1)
        elif "zsh-autosuggestions" not in content and "zsh-syntax-highlighting" not in content:
            content += f"\n{new_plugins}\n"

        # ---------- THEME ----------
        if 'ZSH_THEME="robbyrussell"' in content:
            content = content.replace('ZSH_THEME="robbyrussell"', 'ZSH_THEME=""')

        # ---------- CUSTOM PROMPT ----------
        prompt_block = f"""
# --- EasyZsh Custom Prompt ---
autoload -U colors && colors
setopt PROMPT_SUBST
PROMPT='%F{art.Re}┌─[%f%F{art.Wh}%n@%m%f%F{art.Cy}]─[%f%F{art.Ye}%~%f%F{art.Cy}]%f
%F{art.Blu}└──╼ %f$ '
# -----------------------------
"""

        if "EasyZsh Custom Prompt" not in content:
            content += "\n" + prompt_block

        # ---------- SAVE ----------
        user_zshrc.write_text(content, encoding="utf-8")

        print("✅ USER configuration completed.")
        print(f"📂 Updated file: {user_zshrc}")
        print("🚀 Restart the terminal or run: source ~/.zshrc")
        input("\nPress Enter to return to menu...")

    except subprocess.CalledProcessError as e:
        print(f"❌ Command error: {e}")
    except Exception as e:
        print(f"❌ Critical error:")


# NUMERO 9
def setup_zsh_plugin_root():
    art.clear()
    print(art.banners_zshroot)
    print("\n=== ROOT ZSH SETUP ===")

    if os.geteuid() != 0:
        print("❌ This function must be run as root.")
        return

    root_home = Path("/root")
    root_zshrc = root_home / ".zshrc"
    root_zprofile = root_home / ".zprofile"
    root_history = root_home / ".zsh_history"
    root_ohmyzsh = root_home / ".oh-my-zsh"

    zsh_path = shutil.which("zsh")
    git_path = shutil.which("git")
    curl_path = shutil.which("curl")

    if not zsh_path:
        print("❌ zsh is not installed.")
        return

    if not git_path:
        print("❌ git is not installed.")
        return

    if not curl_path:
        print("❌ curl is not installed.")
        return

    print(f"✓ zsh found: {zsh_path}")
    print(f"✓ git found: {git_path}")
    print(f"✓ curl found: {curl_path}")

    # Installa Oh My Zsh per root se manca
    if not root_ohmyzsh.exists():
        print("• Oh My Zsh for root not found, attempting to install it...")
        try:
            install_cmd = (
                'export RUNZSH=no; '
                'export CHSH=no; '
                'export KEEP_ZSHRC=yes; '
                'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
            )

            subprocess.run(
                ["bash", "-c", install_cmd],
                check=True,
                cwd="/root"
            )
            print("✓ Oh My Zsh installed for root.")
        except Exception as e:
            print(f"⚠️ Automatic Oh My Zsh installation failed: {e}")
            print("• Continuing with basic configuration without Oh My Zsh.")
    else:
        print("✓ Oh My Zsh is already installed for root.")

    # Crea .zshrc se manca
    if not root_zshrc.exists():
        try:
            root_zshrc.write_text("", encoding="utf-8")
            print("✓ ROOT .zshrc created.")
        except Exception as e:
            print(f"❌ Error creating /root/.zshrc: {e}")
            return
    else:
        print("✓ ROOT .zshrc found.")

    # Se c'è Oh My Zsh, prepara plugin custom
    if root_ohmyzsh.exists():
        custom_plugins = root_ohmyzsh / "custom" / "plugins"
        autosug_dir = custom_plugins / "zsh-autosuggestions"
        syntax_dir = custom_plugins / "zsh-syntax-highlighting"

        try:
            custom_plugins.mkdir(parents=True, exist_ok=True)
            print("✓ Root plugin folder ready.")
        except Exception as e:
            print(f"⚠️ Error creating root plugin folder: {e}")

        if not autosug_dir.exists():
            try:
                subprocess.run(
                    ["git", "clone", "https://github.com/zsh-users/zsh-autosuggestions", str(autosug_dir)],
                    check=True
                )
                print("✓ zsh-autosuggestions installed for root.")
            except Exception as e:
                print(f"⚠️ Error installing root autosuggestions: {e}")
        else:
            print("✓ zsh-autosuggestions is already installed for root.")

        if not syntax_dir.exists():
            try:
                subprocess.run(
                    ["git", "clone", "https://github.com/zsh-users/zsh-syntax-highlighting", str(syntax_dir)],
                    check=True
                )
                print("✓ zsh-syntax-highlighting installed for root.")
            except Exception as e:
                print(f"⚠️ Error installing root syntax-highlighting: {e}")
        else:
            print("✓ zsh-syntax-highlighting is already installed for root.")

    # Scrivi configurazione finale
    if root_ohmyzsh.exists():
        zshrc_content = f'''# =========================
# ROOT ZSH CONFIG
# =========================

export ZSH="{root_ohmyzsh}"
ZSH_THEME="robbyrussell"

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

HISTSIZE=5000
SAVEHIST=5000
HISTFILE=~/.zsh_history

setopt autocd
setopt hist_ignore_dups
setopt share_history

PROMPT='%F{art.Cy}┌─[%f%F{art.Wh}%n@%m%f%F{art.Cy}]─[%f%F{art.Ye}%~%f%F{art.Cy}]%f
%F{art.Gr}└──╼ %f$ '
'''
    else:
        zshrc_content = '''# =========================
# ROOT ZSH CONFIG
# =========================

autoload -Uz compinit
compinit

HISTSIZE=5000
SAVEHIST=5000
HISTFILE=~/.zsh_history

setopt autocd
setopt hist_ignore_dups
setopt share_history

PROMPT='%F{art.Cy}┌─[%f%F{art.Wh}%n@%m%f%F{art.Cy}]─[%f%F{art.Ye}%~%f%F{art.Cy}]%f
%F{art.Gr}└──╼ %f$ '
'''

    try:
        root_zshrc.write_text(zshrc_content, encoding="utf-8")
        print("✓ ROOT .zshrc written successfully.")
    except Exception as e:
        print(f"❌ Error writing ROOT .zshrc: {e}")
        return

    if not root_zprofile.exists():
        try:
            root_zprofile.write_text(
                "# Root zprofile\nexport SHELL=/usr/bin/zsh\n",
                encoding="utf-8"
            )
            print("✓ ROOT .zprofile created.")
        except Exception as e:
            print(f"⚠️ Error creating ROOT .zprofile: {e}")
    else:
        print("✓ ROOT .zprofile already exists.")

    if not root_history.exists():
        try:
            root_history.touch()
            print("✓ ROOT .zsh_history created.")
        except Exception as e:
            print(f"⚠️ Error creating ROOT .zsh_history: {e}")
    else:
        print("✓ ROOT .zsh_history already exists.")

    try:
        subprocess.run(
            ["chsh", "-s", zsh_path, "root"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("✓ Root shell set to zsh.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Unable to automatically change the root shell: {e.stderr.strip()}")

    print("✓ Root Zsh setup completed.")
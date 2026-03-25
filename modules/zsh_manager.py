# <-- Gestisce tutto ciò che riguarda la shell Zsh, Oh My Zsh e i plugin.
import os
import time
import subprocess
from pathlib import Path
from datetime import datetime
import shutil
import getpass
# IMPORTANTE: Usa il percorso completo partendo dalla cartella principale
import modules.art as art
import modules.core as core
import modules.config_manager as config_manager





def install_zsh():              # NUMERO 3
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


def install_oh_my_zsh():            # NUMERO 4
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


def install_zsh_autosuggestions():          # NUMERO 5
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



def install_syntax_highlighting():          # NUMERO 6
    # 1. Grafica e Banner (da art.py)
    art.clear()
    print(art.banners_zshsyntax_highlighter)

    # 2. Percorsi dinamici per Oh My Zsh
    zsh_custom = os.environ.get("ZSH_CUSTOM", os.path.expanduser("~/.oh-my-zsh/custom"))
    plugin_path = os.path.join(zsh_custom, "plugins", "zsh-syntax-highlighting")

    # 3. Controllo anti-errore (Se esiste già, non clonare)
    if os.path.exists(plugin_path):
        print("\n⚠️ Il plugin 'zsh-syntax-highlighting' è già presente.")
        time.sleep(2)
        return

    print("🚀 Installazione Syntax Highlighting in corso...")

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
        print("\n✅ Syntax Highlighting installato con successo!")

        # 4. Aggiorna la memoria del programma
        config_manager.update_setting("syntax_highlighting_installed", True)

    except subprocess.CalledProcessError:
        print("\n❌ Errore durante il download del plugin.")

    time.sleep(2)
    input("\nPremi Invio per tornare al menu...")


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
            print(f"\n✅ Backup creato con successo: {backup_path}")
            print("Ora puoi modificare il file .zshrc in sicurezza.")
        except Exception as e:
            print(f"\n❌ Errore durante il backup: {e}")
    else:
        print("\n⚠️ File .zshrc non trovato. Nulla da salvare.")

    input("\nPremi Invio per tornare al menu...")


def setup_zsh_plugin():
    art.clear()
    print(art.banners_zshplugin)

    zshrc_path = Path.home() / ".zshrc"

    if not zshrc_path.exists():
        print("❌ Errore: File .zshrc non trovato.")
        time.sleep(2)
        return

    print("🛡️  SICUREZZA: Questa operazione modificherà il tuo file .zshrc.")
    conferma = input("👉 Hai già eseguito un backup (Opzione 8)? [y/N]: ").lower()

    if conferma != 'y':
        print("\n⚠️ Operazione annullata. Fai prima un backup.")
        time.sleep(2)
        return

    content = zshrc_path.read_text()

    # --- 1. CONFIGURAZIONE PLUGINS ---
    new_plugins = "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)"
    if "plugins=(git)" in content:
        content = content.replace("plugins=(git)", new_plugins)

    # --- 2. CONFIGURAZIONE PROMPT PERSONALIZZATO ---
    custom_prompt = """
# --- EasyZsh Custom Prompt ---
autoload -U colors && colors
setopt PROMPT_SUBST
PROMPT='%F{cyan}┌─[%f%F{green}%n@%m%f%F{cyan}]─[%f%F{yellow}%~%f%F{cyan}]%f
%F{cyan}└──╼ %f$ '
# -----------------------------
"""
    if "EasyZsh Custom Prompt" not in content:
        # Disattiviamo il tema di Oh My Zsh (altrimenti il prompt non cambia)
        content = content.replace('ZSH_THEME="robbyrussell"', 'ZSH_THEME=""')
        # Aggiungiamo il prompt in fondo al file
        content += custom_prompt

    # --- 3. SALVATAGGIO FINALE ---
    try:
        zshrc_path.write_text(content)
        print(f"\n✨ Plugin e Prompt configurati con successo!")
        print(f"🎨 Tema Oh My Zsh disattivato per mostrare il nuovo stile.")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio: {e}")

    print(f"\n🚀 Per attivare, riavvia il terminale o scrivi: source ~/.zshrc")
    input("\n====================== Ottimo lavoro! Premi Invio ====================== ")

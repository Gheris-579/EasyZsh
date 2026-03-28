# <-- Funzioni di sistema (apt, update)
import subprocess
import modules.art as art


def run_task(banner_name, command, success_message):
    art.clear()
    print(getattr(art, banner_name)) # Prende il banner da art.py
    print(f"\n🚀 Running: {' '.join(command)}\n")
    try:
        subprocess.run(command, check=True)
        print(f"\n✅ {success_message}")
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"\n❌ Errore: {e}")
        input("\nPress Enter to return to the menu...")


def update_system():
    run_task(
        "bannersys",
        ["sudo", "apt", "update"],
        "Updated package lists."
    )
    run_task(
        "bannersys",
        ["sudo", "apt", "full-upgrade", "-y"],
        "System updated successfully!"
    )
    art.clear()

# Funzione 2: Pulizia (AutoRemove)
def system_cleanup():
    run_task(
        "bannersremove",
        ["sudo", "apt", "autoremove", "-y"],
        "Unnecessary packages successfully removed."
    )
    run_task(
        "bannersremove",
        ["sudo", "apt", "autoclean"],
        "Clean packet cache."
    )
    art.clear()



def update_easyzsh():
    art.clear()
    print(art.banners_autoupdate)
    # La cartella dove install.sh ha clonato il progetto
    install_dir = Path.home() / ".easyzsh"

    if not install_dir.exists():
        print("❌ Error: Installation folder ~/.easyzsh not found.")
        return

    print("Checking for updates on GitHub...")
    try:
        # Esegue git pull nella cartella del tool
        subprocess.run(["git", "-C", str(install_dir), "pull"], check=True)
        print("\n✅ EasyZsh updated to the latest version!")
        print("Restart the program to see the changes.")
    except Exception as e:
        print(f"\n❌ Error during the update: {e}")

    input("\nPress Enter to return to the menu...")

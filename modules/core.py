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
    # Questa è la funzione che avevi scritto tu
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
        "Junk packages successfully removed."
    )
    run_task(
        "bannersremove",
        ["sudo", "apt", "autoclean"],
        "Clean packet cache."
    )
    art.clear()
# ⚡ EasyZsh 

> **Transform your terminal into a professional workstation with a single command.**  
> An interactive Python manager for Debian/Ubuntu-based distributions (Parrot OS, Kali Linux, Mint).

---

## 🚀 Why EasyZsh?
Manually configuring Zsh, Oh My Zsh, and plugins every time you install a new system is tedious. EasyZsh automates the entire process through an intuitive numbered menu and eye-catching banners.

### 🔥 What does EasyZsh handle for you?
- ✅ System Maintenance: Update, full upgrade, and cleanup from one place.
- ✅ Essential Dependencies: Installs git, curl, and required base packages automatically.
- ✅ Zsh Setup: Installs Zsh and prepares it for daily use.
- ✅ Oh My Zsh Installation: Sets up Oh My Zsh automatically in unattended mode.
- ✅ User Zsh Configuration: Configures your user `.zshrc` with plugins, custom prompt, and improved defaults.
- ✅ Root Zsh Configuration: Automatically relaunches with sudo when needed and configures root Zsh separately.
- ✅ Productivity Plugins: Adds `zsh-autosuggestions` and `zsh-syntax-highlighting` for a better terminal experience.
- ✅ Backup Protection: Creates a safety backup of `.zshrc` before every important change.
- ✅ Smart Config Memory: Stores preferences in `config.json` to remember your setup.
- ✅ Error-Aware Setup: Verifies files, paths, and dependencies before applying changes.

---

## 📥 Quick Installation (One-Liner)
No need to download anything manually. Paste this into your terminal and press Enter:

```bash
curl -sSL https://raw.githubusercontent.com/Gheris-579/EasyZsh/main/EasyZsh/install.sh | bash
```
After installation, restart your terminal and simply type:
```bash
easyzsh
```

# 🛠️ Requirements
- OS: Ubuntu, Debian, Parrot OS, Kali Linux, Pop!_OS.
- Python: 3.x (the installation script checks this for you).

# 📂 Complete Project Structure
- **easyzsh.py:** Il file principale (Main) che l'utente lancia per aprire il menu.
- **install.sh:** The Bash script used for quick installation through the `curl` command.
- **LICENSE:** The MIT license that protects the project’s source code.
- **README.md:** The presentation page containing instructions, screenshots, and project information.
- **config.json:** The file, created automatically, that stores the username and Zsh installation status.
- **modules/__init__.py:** The required empty file that tells Python the folder contains modules.
- **modules/core.py:** The “engine” that contains `run_task` and the `apt` system commands.
- **modules/zsh_manager.py:** The “specialist” responsible for installing Oh My Zsh, plugins, and the custom prompt.
- **modules/art.py:** Your “art gallery” containing the 11 ASCII banners and color codes (`Re`, `Gr`, `Blu`).
- **modules/config_manager.py:** The manager that reads and writes data to the JSON configuration file.
- **modules/ui_utils.py:** (If created) The file that contains UI helper functions such as `clear()` or `show_header()`.



# 📸 Menu Preview
<img width="1169" height="704" alt="image" src="https://github.com/user-attachments/assets/c941f364-9368-4fe1-b1c6-a0689f2d07cd" />




